package main

import "fmt"

func approvalLabel(score int) string {
	if score < 0 {
		return "invalid"
	}
	if score < 75 {
		return "needs improvement"
	}
	return "approved"
}

func example1ForLoopRange() {
	values := make([]int, 0, 4)
	// range is Go's standard way to iterate across slices, arrays, maps, and strings.
	for index := range 4 {
		values = append(values, index*index)
	}
	fmt.Println("1. for loop with range:", values)
}

func example2ForConditionLoop() {
	count := 0
	outputs := []int{}
	// Go reuses for as its while-style loop by omitting init and post clauses.
	for count < 3 {
		outputs = append(outputs, count)
		count++
	}
	fmt.Println("2. for-condition loop:", outputs)
}

func example3IfElseIfElse() {
	value := 86
	result := ""
	// else if keeps mutually exclusive branches readable without nested blocks.
	if value >= 90 {
		result = "excellent"
	} else if value >= 75 {
		result = "passing"
	} else {
		result = "failing"
	}
	fmt.Println("3. if/else if/else:", result)
}

func example4Switch() {
	command := "archive"
	// switch gives Go a concise multi-branch control structure without fallthrough by default.
	switch command {
	case "archive":
		fmt.Println("4. switch:", "archive request")
	case "delete":
		fmt.Println("4. switch:", "delete request")
	default:
		fmt.Println("4. switch:", "unknown request")
	}
}

func example5BreakContinue() {
	visited := []int{}
	for number := range 6 {
		// continue skips odd values; break exits once a threshold is met.
		if number%2 == 1 {
			continue
		}
		if number == 4 {
			break
		}
		visited = append(visited, number)
	}
	fmt.Println("5. break and continue:", visited)
}

func example6NestedLoops() {
	pairs := [][2]int{}
	// Nested for-loops make the control hierarchy fully explicit.
	for row := range 2 {
		for column := range 3 {
			pairs = append(pairs, [2]int{row, column})
		}
	}
	fmt.Println("6. nested loops:", pairs)
}

func example7GuardClauses() {
	fmt.Println("7. guard clauses:", approvalLabel(-1), approvalLabel(80))
}

func main() {
	example1ForLoopRange()
	example2ForConditionLoop()
	example3IfElseIfElse()
	example4Switch()
	example5BreakContinue()
	example6NestedLoops()
	example7GuardClauses()
}
