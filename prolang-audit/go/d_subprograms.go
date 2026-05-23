package main

import "fmt"

func factorial(number int) int {
	if number <= 1 {
		return 1
	}
	return number * factorial(number-1)
}

func sumAll(values ...int) int {
	total := 0
	for _, value := range values {
		total += value
	}
	return total
}

func quotientAndRemainder(dividend, divisor int) (int, int) {
	return dividend / divisor, dividend % divisor
}

func mapInts(values []int, transform func(int) int) []int {
	result := make([]int, len(values))
	for index, value := range values {
		result[index] = transform(value)
	}
	return result
}

func filterInts(values []int, predicate func(int) bool) []int {
	result := []int{}
	for _, value := range values {
		if predicate(value) {
			result = append(result, value)
		}
	}
	return result
}

func reduceInts(values []int, reducer func(int, int) int, initial int) int {
	total := initial
	for _, value := range values {
		total = reducer(total, value)
	}
	return total
}

func example1FirstClassFunctions() {
	greet := func(name string) string {
		return fmt.Sprintf("hello, %s", name)
	}
	// Function values can be stored in variables and invoked later.
	fmt.Println("1. first-class function:", greet("Go"))
}

func example2Closures() {
	makeMultiplier := func(factor int) func(int) int {
		return func(value int) int {
			return value * factor
		}
	}
	timesThree := makeMultiplier(3)
	// The inner function closes over factor from the outer scope.
	fmt.Println("2. closure:", timesThree(5))
}

func example3Recursion() {
	// Go supports direct recursion with compile-time signature checking.
	fmt.Println("3. recursion:", factorial(5))
}

func example4VariadicParameters() {
	// A trailing ...T parameter collects any number of arguments into a slice.
	fmt.Println("4. variadic parameters:", sumAll(1, 2, 3, 4))
}

func example5MultipleReturnValues() {
	quotient, remainder := quotientAndRemainder(17, 5)
	// Native multi-return is part of the language rather than tuple packing.
	fmt.Println("5. multiple return values:", quotient, remainder)
}

func example6HigherOrderFunctions() {
	numbers := []int{1, 2, 3, 4}
	doubled := mapInts(numbers, func(value int) int { return value * 2 })
	filtered := filterInts(numbers, func(value int) bool { return value%2 == 0 })
	total := reduceInts(numbers, func(left, right int) int { return left + right }, 0)
	// Higher-order behavior comes from passing function literals into helper routines.
	fmt.Println("6. higher-order functions:", doubled, filtered, total)
}

func example7AnonymousFunctions() {
	square := func(value int) int {
		return value * value
	}
	// Anonymous function literals provide lightweight ad hoc behavior.
	fmt.Println("7. anonymous function:", square(6))
}

func main() {
	example1FirstClassFunctions()
	example2Closures()
	example3Recursion()
	example4VariadicParameters()
	example5MultipleReturnValues()
	example6HigherOrderFunctions()
	example7AnonymousFunctions()
}
