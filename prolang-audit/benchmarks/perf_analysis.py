"""Performance and memory analysis for Python examples.

This script uses the standard-library ``timeit`` module as the runnable
equivalent of IPython's ``%timeit`` magic so it can execute under
``python benchmarks/perf_analysis.py``.
"""

from __future__ import annotations

import asyncio
import gc
import sys
import timeit
import tracemalloc
from typing import Callable


def run_timeit(label: str, func: Callable[[], object], number: int) -> float:
    """Return the best average execution time per run."""
    gc.collect()
    timer = timeit.Timer(func)
    repeats = timer.repeat(repeat=5, number=number)
    best_average = min(repeats) / number
    print(f"{label}: {best_average:.8f} seconds per run")
    return best_average


def measure_peak_memory(func: Callable[[], object]) -> int:
    """Return peak memory usage in bytes while running func once."""
    tracemalloc.start()
    func()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


def build_with_loop() -> list[int]:
    """Build a list using a standard for-loop."""
    output: list[int] = []
    for value in range(10_000):
        # The append loop is explicit but pays repeated method-call overhead.
        output.append(value * 2)
    return output


def build_with_comprehension() -> list[int]:
    """Build a list using list-comprehension syntax."""
    # Comprehensions push the loop into a compact optimized expression form.
    return [value * 2 for value in range(10_000)]


def recursive_fibonacci(number: int) -> int:
    """Compute fibonacci recursively."""
    if number < 2:
        return number
    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)


def iterative_fibonacci(number: int) -> int:
    """Compute fibonacci iteratively."""
    left, right = 0, 1
    for _ in range(number):
        left, right = right, left + right
    return left


async def async_task(delay: float) -> float:
    """Sleep asynchronously and return the delay."""
    await asyncio.sleep(delay)
    return delay


async def run_parallel_asyncio() -> list[float]:
    """Run several coroutines concurrently."""
    # asyncio.gather overlaps waiting periods on one event loop.
    return await asyncio.gather(*(async_task(0.01) for _ in range(5)))


async def run_sequential_asyncio() -> list[float]:
    """Run the same coroutines sequentially."""
    results: list[float] = []
    for _ in range(5):
        # Sequential awaits preserve order but do not overlap idle time.
        results.append(await async_task(0.01))
    return results


def build_lookup_map() -> dict[int, int]:
    """Create a lookup dictionary."""
    return {value: value * 10 for value in range(10_000)}


def build_lookup_list() -> list[tuple[int, int]]:
    """Create a linear-search list."""
    return [(value, value * 10) for value in range(10_000)]


def linear_search(entries: list[tuple[int, int]], target: int) -> int:
    """Find a value by scanning a list."""
    for key, value in entries:
        if key == target:
            return value
    raise ValueError("target not found")


def benchmark_list_comprehension_vs_loop() -> None:
    """Compare comprehension and append-loop timing."""
    print("\n1. List comprehension vs standard for-loop")
    run_timeit("   list comprehension", build_with_comprehension, number=200)
    run_timeit("   append loop", build_with_loop, number=200)


def benchmark_list_vs_generator_memory() -> None:
    """Compare memory footprints with sys.getsizeof."""
    print("\n2. list vs generator memory footprint")
    list_object = [value * 2 for value in range(1_000)]
    generator_object = (value * 2 for value in range(1_000))
    # sys.getsizeof shows the container object size held by each representation.
    print("   list size:", sys.getsizeof(list_object), "bytes")
    print("   generator size:", sys.getsizeof(generator_object), "bytes")


def benchmark_iterative_vs_recursive_fibonacci() -> None:
    """Compare fibonacci time and peak memory."""
    print("\n3. iterative vs recursive fibonacci")
    run_timeit("   iterative fibonacci(20)", lambda: iterative_fibonacci(20), number=2_000)
    run_timeit("   recursive fibonacci(20)", lambda: recursive_fibonacci(20), number=100)
    iterative_peak = measure_peak_memory(lambda: iterative_fibonacci(25))
    recursive_peak = measure_peak_memory(lambda: recursive_fibonacci(25))
    print("   iterative peak memory:", iterative_peak, "bytes")
    print("   recursive peak memory:", recursive_peak, "bytes")


def benchmark_asyncio_parallel_vs_sequential() -> None:
    """Compare parallel and sequential asyncio execution."""
    print("\n4. asyncio.gather parallel vs sequential execution")
    run_timeit(
        "   asyncio.gather",
        lambda: asyncio.run(run_parallel_asyncio()),
        number=10,
    )
    run_timeit(
        "   sequential await",
        lambda: asyncio.run(run_sequential_asyncio()),
        number=10,
    )


def benchmark_dict_lookup_vs_linear_search() -> None:
    """Compare dictionary lookup with list scanning."""
    print("\n5. dict lookup O(1) vs linear list search O(n)")
    lookup_map = build_lookup_map()
    lookup_list = build_lookup_list()
    target = 9_999
    run_timeit("   dict lookup", lambda: lookup_map[target], number=200_000)
    run_timeit(
        "   linear list search",
        lambda: linear_search(lookup_list, target),
        number=1_000,
    )


def main() -> None:
    """Run all required Python benchmark comparisons."""
    benchmark_list_comprehension_vs_loop()
    benchmark_list_vs_generator_memory()
    benchmark_iterative_vs_recursive_fibonacci()
    benchmark_asyncio_parallel_vs_sequential()
    benchmark_dict_lookup_vs_linear_search()


if __name__ == "__main__":
    main()
