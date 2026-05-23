package benchmarks

import (
	"strconv"
	"strings"
	"sync"
	"testing"
)

type lookupEntry struct {
	key   int
	value int
}

func buildWithoutPreallocation() []int {
	output := []int{}
	for value := range 10_000 {
		output = append(output, value)
	}
	return output
}

func buildWithPreallocation() []int {
	output := make([]int, 0, 10_000)
	for value := range 10_000 {
		output = append(output, value)
	}
	return output
}

func fanOutSquare(values []int) int {
	workers := 4
	chunkSize := len(values) / workers
	results := make(chan int, workers)
	var wg sync.WaitGroup

	for workerIndex := range workers {
		start := workerIndex * chunkSize
		end := start + chunkSize
		if workerIndex == workers-1 {
			end = len(values)
		}

		wg.Add(1)
		go func(part []int) {
			defer wg.Done()
			total := 0
			for _, value := range part {
				total += value * value
			}
			results <- total
		}(values[start:end])
	}

	wg.Wait()
	close(results)

	total := 0
	for result := range results {
		total += result
	}
	return total
}

func sequentialSquare(values []int) int {
	total := 0
	for _, value := range values {
		total += value * value
	}
	return total
}

func buildLookupMap() map[int]int {
	output := make(map[int]int, 10_000)
	for value := range 10_000 {
		output[value] = value * 10
	}
	return output
}

func buildLookupSlice() []lookupEntry {
	output := make([]lookupEntry, 0, 10_000)
	for value := range 10_000 {
		output = append(output, lookupEntry{key: value, value: value * 10})
	}
	return output
}

func linearSearch(entries []lookupEntry, target int) int {
	for _, entry := range entries {
		if entry.key == target {
			return entry.value
		}
	}
	return -1
}

func recursiveFibonacci(number int) int {
	if number < 2 {
		return number
	}
	return recursiveFibonacci(number-1) + recursiveFibonacci(number-2)
}

func iterativeFibonacci(number int) int {
	left, right := 0, 1
	for range number {
		left, right = right, left+right
	}
	return left
}

func concatenateWithPlus(parts []string) string {
	output := ""
	for _, part := range parts {
		output += part
	}
	return output
}

func concatenateWithBuilder(parts []string) string {
	var builder strings.Builder
	builder.Grow(len(parts) * 2)
	for _, part := range parts {
		builder.WriteString(part)
	}
	return builder.String()
}

func BenchmarkSliceAppendLoop(b *testing.B) {
	b.ReportAllocs()
	for range b.N {
		_ = buildWithoutPreallocation()
	}
}

func BenchmarkPreallocatedSlice(b *testing.B) {
	b.ReportAllocs()
	for range b.N {
		_ = buildWithPreallocation()
	}
}

func BenchmarkSequentialExecution(b *testing.B) {
	b.ReportAllocs()
	values := make([]int, 2_000)
	for index := range values {
		values[index] = index
	}
	b.ResetTimer()
	for range b.N {
		_ = sequentialSquare(values)
	}
}

func BenchmarkGoroutineFanOut(b *testing.B) {
	b.ReportAllocs()
	values := make([]int, 2_000)
	for index := range values {
		values[index] = index
	}
	b.ResetTimer()
	for range b.N {
		_ = fanOutSquare(values)
	}
}

func BenchmarkMapLookup(b *testing.B) {
	b.ReportAllocs()
	lookupMap := buildLookupMap()
	target := 9_999
	b.ResetTimer()
	for range b.N {
		_ = lookupMap[target]
	}
}

func BenchmarkLinearSliceScan(b *testing.B) {
	b.ReportAllocs()
	lookupSlice := buildLookupSlice()
	target := 9_999
	b.ResetTimer()
	for range b.N {
		_ = linearSearch(lookupSlice, target)
	}
}

func BenchmarkRecursiveFibonacci(b *testing.B) {
	b.ReportAllocs()
	for range b.N {
		_ = recursiveFibonacci(20)
	}
}

func BenchmarkIterativeFibonacci(b *testing.B) {
	b.ReportAllocs()
	for range b.N {
		_ = iterativeFibonacci(20)
	}
}

func BenchmarkStringConcatenation(b *testing.B) {
	b.ReportAllocs()
	parts := make([]string, 100)
	for index := range parts {
		parts[index] = strconv.Itoa(index)
	}
	b.ResetTimer()
	for range b.N {
		_ = concatenateWithPlus(parts)
	}
}

func BenchmarkStringBuilder(b *testing.B) {
	b.ReportAllocs()
	parts := make([]string, 100)
	for index := range parts {
		parts[index] = strconv.Itoa(index)
	}
	b.ResetTimer()
	for range b.N {
		_ = concatenateWithBuilder(parts)
	}
}
