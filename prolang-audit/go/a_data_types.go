package main

import "fmt"

func example1PrimitiveTypes() {
	integerValue := 42
	floatValue := 3.14
	boolValue := true
	stringValue := "Go"
	// Go gives each variable a concrete static type at compile time.
	fmt.Println("1. primitive types:", integerValue, floatValue, boolValue, stringValue)
}

func example2PointerTypes() {
	counter := 10
	pointer := &counter
	// Go exposes pointers explicitly, so mutation through aliases is visible in code.
	*pointer++
	fmt.Println("2. pointer types:", counter, *pointer)
}

func example3StaticTyping() {
	var total int = 5
	// Reassigning a string here would fail to compile because total is statically typed.
	fmt.Printf("3. static typing: %d (%T)\n", total, total)
}

func example4TypeInference() {
	label := "audit"
	count := 7
	// The := operator infers a static type from the initializer expression.
	fmt.Printf("4. type inference: %s (%T), %d (%T)\n", label, label, count, count)
}

func example5Collections() {
	stages := []string{"plan", "implement", "verify"}
	scores := map[string]int{"python": 9, "go": 8}
	// Slices and maps are built-in reference-like collection types in Go.
	fmt.Println("5. collections:", stages, scores)
}

func example6NilHandling() {
	var numbers []int
	var lookup map[string]int
	// nil is Go's zero value for slice, map, pointer, channel, and function references.
	fmt.Println("6. nil handling:", numbers == nil, lookup == nil)
}

func example7ExplicitConversion() {
	wholeNumber := 123
	asFloat := float64(wholeNumber)
	asString := fmt.Sprintf("%.1f", asFloat)
	// Go requires explicit conversion even between numerically compatible types.
	fmt.Println("7. explicit conversion:", wholeNumber, asFloat, asString)
}

func main() {
	example1PrimitiveTypes()
	example2PointerTypes()
	example3StaticTyping()
	example4TypeInference()
	example5Collections()
	example6NilHandling()
	example7ExplicitConversion()
}
