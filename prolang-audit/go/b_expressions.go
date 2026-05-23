package main

import "fmt"

func sideEffectCheck(label string, result bool) bool {
	fmt.Println("   evaluating", label)
	return result
}

func computePair() (int, int) {
	return 7, 11
}

func example1ArithmeticPrecedence() {
	value := 2 + 3*4
	grouped := (2 + 3) * 4
	// Multiplication has higher precedence than addition unless parentheses override it.
	fmt.Println("1. arithmetic precedence:", value, grouped)
}

func example2BooleanShortCircuit() {
	// The right operand is skipped because the left operand already decides the result.
	result := sideEffectCheck("left", false) && sideEffectCheck("right", true)
	fmt.Println("2. short circuit result:", result)
}

func example3TernaryWorkaround() {
	score := 85
	remark := "fail"
	// Go has no ternary operator, so selection stays as an explicit if statement.
	if score >= 75 {
		remark = "pass"
	}
	fmt.Println("3. ternary workaround:", remark)
}

func example4AugmentedAssignment() {
	total := 10
	// Augmented operators update numeric state without repeating the left-hand side.
	total += 5
	total *= 2
	total -= 4
	fmt.Println("4. augmented assignment:", total)
}

func example5MultipleAssignment() {
	first, second := computePair()
	// Multiple assignment works naturally with multi-value returns.
	first, second = second, first
	fmt.Println("5. multiple assignment:", first, second)
}

func example6BitwiseOperations() {
	leftShift := 3 << 2
	mask := 14 & 7
	// Go keeps bitwise operators explicit and strongly typed.
	fmt.Println("6. bitwise operations:", leftShift, mask, 5^3)
}

func example7StringInterpolation() {
	language := "Go"
	examples := 7
	// fmt.Sprintf is the standard-library formatting mechanism instead of dedicated syntax.
	message := fmt.Sprintf("7. string interpolation: %s shows %d examples", language, examples)
	fmt.Println(message)
}

func main() {
	example1ArithmeticPrecedence()
	example2BooleanShortCircuit()
	example3TernaryWorkaround()
	example4AugmentedAssignment()
	example5MultipleAssignment()
	example6BitwiseOperations()
	example7StringInterpolation()
}
