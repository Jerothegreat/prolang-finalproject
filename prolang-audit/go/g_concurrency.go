package main

import (
	"context"
	"fmt"
	"runtime"
	"sync"
	"time"
)

func example1BasicGoroutine() {
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		// A goroutine launches concurrent work with lightweight runtime scheduling.
		fmt.Println("1. basic goroutine: worker executed")
	}()
	wg.Wait()
}

func example2Channels() {
	messageChannel := make(chan string)
	go func() {
		// Channels provide typed communication and synchronization between goroutines.
		messageChannel <- "from producer"
	}()
	fmt.Println("2. channels:", <-messageChannel)
}

func example3WaitGroupConcurrency() {
	var wg sync.WaitGroup
	results := make(chan string, 2)
	runJob := func(label string) {
		defer wg.Done()
		time.Sleep(10 * time.Millisecond)
		results <- label
	}
	wg.Add(2)
	go runJob("first")
	go runJob("second")
	wg.Wait()
	close(results)
	collected := []string{}
	for result := range results {
		collected = append(collected, result)
	}
	fmt.Println("3. goroutine + WaitGroup:", collected)
}

func example4Mutex() {
	var mu sync.Mutex
	counter := 0
	var wg sync.WaitGroup
	increment := func() {
		defer wg.Done()
		for range 200 {
			// Mutex protects the critical section around shared state.
			mu.Lock()
			counter++
			mu.Unlock()
		}
	}
	for range 3 {
		wg.Add(1)
		go increment()
	}
	wg.Wait()
	fmt.Println("4. mutex protection:", counter)
}

func runCounter(useLock bool) int {
	counter := 0
	var mu sync.Mutex
	var wg sync.WaitGroup
	worker := func() {
		defer wg.Done()
		for range 150 {
			if useLock {
				mu.Lock()
				current := counter
				runtime.Gosched()
				counter = current + 1
				mu.Unlock()
				continue
			}
			current := counter
			runtime.Gosched()
			counter = current + 1
		}
	}
	for range 4 {
		wg.Add(1)
		go worker()
	}
	wg.Wait()
	return counter
}

func example5RaceConditionAndFix() {
	unsafeTotal := runCounter(false)
	safeTotal := runCounter(true)
	// The unlocked version risks lost updates, while the mutex keeps increments consistent.
	fmt.Println("5. race condition vs fix:", unsafeTotal, safeTotal)
}

func example6FanOutFanIn() {
	jobs := make(chan int, 4)
	results := make(chan int, 4)
	var workers sync.WaitGroup
	worker := func() {
		defer workers.Done()
		for job := range jobs {
			// Fan-out spreads jobs across workers; fan-in collects all results into one channel.
			results <- job * job
		}
	}
	for range 2 {
		workers.Add(1)
		go worker()
	}
	for value := range 4 {
		jobs <- value
	}
	close(jobs)
	workers.Wait()
	close(results)
	collected := []int{}
	for result := range results {
		collected = append(collected, result)
	}
	fmt.Println("6. fan-out/fan-in:", collected)
}

func example7Cancellation() {
	ctx, cancel := context.WithCancel(context.Background())
	values := []int{}
	var mu sync.Mutex
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		tick := 0
		for {
			select {
			case <-ctx.Done():
				return
			default:
				mu.Lock()
				values = append(values, tick)
				mu.Unlock()
				tick++
				time.Sleep(5 * time.Millisecond)
			}
		}
	}()
	time.Sleep(20 * time.Millisecond)
	// context.WithCancel broadcasts a cooperative stop signal to dependent goroutines.
	cancel()
	wg.Wait()
	fmt.Println("7. cancellation:", len(values) > 0, "ticks:", len(values))
}

func main() {
	example1BasicGoroutine()
	example2Channels()
	example3WaitGroupConcurrency()
	example4Mutex()
	example5RaceConditionAndFix()
	example6FanOutFanIn()
	example7Cancellation()
}
