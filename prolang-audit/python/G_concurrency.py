"""Demonstrate Python concurrency patterns."""

import asyncio
import queue
import threading
import time


def example_1_threading_thread() -> None:
    """Show a basic thread."""

    def worker() -> None:
        """Print from a background thread."""
        # Python uses Thread objects to start concurrent OS-level threads.
        print("1. basic thread: worker executed")

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()


def example_2_queue_channel_equivalent() -> None:
    """Show queue.Queue as a thread-safe message channel."""
    message_queue: queue.Queue[str] = queue.Queue()

    def producer() -> None:
        """Put one message on the queue."""
        # queue.Queue coordinates hand-off between threads without manual locking.
        message_queue.put("from producer")

    thread = threading.Thread(target=producer)
    thread.start()
    thread.join()
    print("2. queue channel equivalent:", message_queue.get())


async def async_job(label: str, delay: float) -> str:
    """Sleep asynchronously and return a label."""
    await asyncio.sleep(delay)
    return label


async def run_asyncio_example() -> list[str]:
    """Run multiple coroutine tasks concurrently."""
    # asyncio.gather schedules coroutine work cooperatively on one event loop.
    return await asyncio.gather(async_job("first", 0.01), async_job("second", 0.01))


def example_3_async_await() -> None:
    """Show async/await with asyncio."""
    results = asyncio.run(run_asyncio_example())
    print("3. async/await:", results)


def example_4_lock() -> None:
    """Show a lock protecting shared state."""
    lock = threading.Lock()
    counter = {"value": 0}

    def increment() -> None:
        """Increment the shared counter safely."""
        for _ in range(200):
            # Lock serializes the critical section around the shared mutation.
            with lock:
                counter["value"] += 1

    threads = [threading.Thread(target=increment) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("4. lock protection:", counter["value"])


def run_race_condition(use_lock: bool) -> int:
    """Run a counter update workload with or without a lock."""
    counter = {"value": 0}
    lock = threading.Lock()

    def worker() -> None:
        """Increment using an intentionally racy read-modify-write pattern."""
        for _ in range(150):
            if use_lock:
                with lock:
                    current = counter["value"]
                    time.sleep(0)
                    counter["value"] = current + 1
            else:
                current = counter["value"]
                time.sleep(0)
                counter["value"] = current + 1

    threads = [threading.Thread(target=worker) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return counter["value"]


def example_5_race_condition_and_fix() -> None:
    """Show a race condition and then fix it."""
    unsafe_total = run_race_condition(use_lock=False)
    safe_total = run_race_condition(use_lock=True)
    # The unsafe version loses updates; the locked version preserves all increments.
    print("5. race condition vs fix:", unsafe_total, safe_total)


def example_6_fan_out_fan_in() -> None:
    """Show a simple fan-out and fan-in pattern with queues."""
    input_queue: queue.Queue[int | None] = queue.Queue()
    output_queue: queue.Queue[int] = queue.Queue()

    def worker() -> None:
        """Read work items and publish results."""
        while True:
            item = input_queue.get()
            if item is None:
                input_queue.task_done()
                return
            # Fan-out distributes inputs to workers; fan-in collects to one queue.
            output_queue.put(item * item)
            input_queue.task_done()

    threads = [threading.Thread(target=worker) for _ in range(2)]
    for thread in threads:
        thread.start()
    for value in range(4):
        input_queue.put(value)
    for _ in threads:
        input_queue.put(None)
    input_queue.join()
    results = sorted(output_queue.get() for _ in range(4))
    for thread in threads:
        thread.join()
    print("6. fan-out/fan-in:", results)


def example_7_cancellation() -> None:
    """Show cooperative cancellation using threading.Event."""
    stop_event = threading.Event()
    observed: list[int] = []

    def worker() -> None:
        """Work until cancellation is requested."""
        tick = 0
        while not stop_event.is_set():
            observed.append(tick)
            tick += 1
            time.sleep(0.005)

    thread = threading.Thread(target=worker)
    thread.start()
    time.sleep(0.02)
    # Event lets the main thread broadcast a cooperative stop signal.
    stop_event.set()
    thread.join()
    print("7. cancellation:", len(observed) > 0, "ticks:", len(observed))


def main() -> None:
    """Run all concurrency examples."""
    example_1_threading_thread()
    example_2_queue_channel_equivalent()
    example_3_async_await()
    example_4_lock()
    example_5_race_condition_and_fix()
    example_6_fan_out_fan_in()
    example_7_cancellation()


if __name__ == "__main__":
    main()
