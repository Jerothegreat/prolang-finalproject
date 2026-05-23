package main

import (
	"errors"
	"fmt"
	"log"
)

var errConfigUnavailable = errors.New("config service unavailable")

type validationError struct {
	message string
}

// Error satisfies the built-in error interface.
func (v validationError) Error() string {
	return v.message
}

type missingReviewerError struct {
	field string
}

// Error satisfies the built-in error interface.
func (m missingReviewerError) Error() string {
	return fmt.Sprintf("%s is required", m.field)
}

type temporaryStorageError struct {
	service string
}

// Error satisfies the built-in error interface.
func (t temporaryStorageError) Error() string {
	return fmt.Sprintf("%s temporarily unavailable", t.service)
}

type demoResource struct {
	name string
}

func openResource(name string) *demoResource {
	fmt.Println("6. defer pattern: open", name)
	return &demoResource{name: name}
}

func (r *demoResource) close() {
	fmt.Println("6. defer pattern: close", r.name)
}

func parseCount(rawValue string) (int, error) {
	switch rawValue {
	case "5":
		return 5, nil
	case "7":
		return 7, nil
	default:
		return 0, missingReviewerError{field: "count"}
	}
}

func readConfig() error {
	return errConfigUnavailable
}

func loadAuditSettings() error {
	if err := readConfig(); err != nil {
		return fmt.Errorf("unable to load audit settings: %w", err)
	}
	return nil
}

func validateState(shouldFail bool) {
	if shouldFail {
		panic("fatal validation mismatch")
	}
}

func lowLevelOperation() error {
	return validationError{message: "database write failed"}
}

func midLevelOperation() error {
	return lowLevelOperation()
}

func example1DeferRecoverFinallyAnalogue() {
	defer func() {
		// defer always runs, and recover can intercept a panic in the same goroutine.
		if recovered := recover(); recovered != nil {
			fmt.Println("1. defer/recover:", recovered)
		}
		fmt.Println("1. defer/recover: cleanup executed")
	}()
	panic("panic used to simulate exceptional control flow")
}

func example2CustomErrorType() {
	err := validationError{message: "invalid audit state"}
	// Custom structs let Go encode domain context in typed error values.
	fmt.Println("2. custom error:", err)
}

func example3WrappingAndUnwrapping() {
	err := loadAuditSettings()
	// errors.Is walks wrapped error chains built with %w.
	fmt.Println("3. wrapping:", err, "is config error:", errors.Is(err, errConfigUnavailable))
}

func example4PanicRecover() {
	defer func() {
		if recovered := recover(); recovered != nil {
			fmt.Println("4. panic/recover:", recovered)
		}
	}()
	// panic aborts the normal flow until a deferred recover handles it.
	validateState(true)
}

func example5MultipleErrorTypes() {
	for _, rawValue := range []string{"5", "oops", "7"} {
		count, err := parseCount(rawValue)
		if err == nil {
			fmt.Println("5. parsed value:", count)
			continue
		}
		var missing missingReviewerError
		var temporary temporaryStorageError
		// errors.As lets one block distinguish among concrete wrapped error types.
		switch {
		case errors.As(err, &missing):
			fmt.Println("5. multiple error types:", missing.Error())
		case errors.As(err, &temporary):
			fmt.Println("5. multiple error types:", temporary.Error())
		default:
			fmt.Println("5. multiple error types:", err)
		}
	}
}

func example6DeferPattern() {
	resource := openResource("report-file")
	defer resource.close()
	// defer gives Go deterministic cleanup similar to a context-manager exit hook.
	fmt.Println("6. defer pattern: inside")
}

func example7PropagationVsLogging() {
	if err := midLevelOperation(); err != nil {
		// Callers usually decide whether to log, wrap, or return the error again.
		log.Printf("7. propagation handled at top level: %v", err)
	}
}

func main() {
	example1DeferRecoverFinallyAnalogue()
	example2CustomErrorType()
	example3WrappingAndUnwrapping()
	example4PanicRecover()
	example5MultipleErrorTypes()
	example6DeferPattern()
	example7PropagationVsLogging()
}
