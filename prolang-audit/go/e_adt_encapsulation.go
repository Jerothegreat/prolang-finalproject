package main

import "fmt"

const taxRate = 0.12

func applyTax(amount float64) float64 {
	return amount * (1 + taxRate)
}

type account struct {
	owner   string
	balance float64
}

func newAccount(owner string, openingBalance float64) *account {
	return &account{owner: owner, balance: openingBalance}
}

func (a *account) deposit(amount float64) {
	a.balance += amount
}

func (a *account) getBalance() float64 {
	return a.balance
}

func (a *account) setBalance(newBalance float64) error {
	if newBalance < 0 {
		return fmt.Errorf("balance cannot be negative")
	}
	a.balance = newBalance
	return nil
}

type processor interface {
	process(amount float64) string
}

type cardProcessor struct{}

func (cardProcessor) process(amount float64) string {
	return fmt.Sprintf("processed %.2f", amount)
}

type immutablePoint struct {
	x int
	y int
}

func newImmutablePoint(x, y int) immutablePoint {
	return immutablePoint{x: x, y: y}
}

func (p immutablePoint) coordinates() (int, int) {
	return p.x, p.y
}

func example1CustomADT() {
	auditAccount := newAccount("Ari", 1000)
	auditAccount.deposit(250)
	// A struct plus methods forms a compact custom ADT in Go.
	fmt.Println("1. custom ADT:", auditAccount.owner, auditAccount.getBalance())
}

func example2PrivateFields() {
	auditAccount := newAccount("Bea", 500)
	// Lowercase fields stay unexported outside the package boundary.
	fmt.Println("2. unexported field:", auditAccount.balance)
}

func example3GettersSetters() {
	auditAccount := newAccount("Cal", 300)
	_ = auditAccount.setBalance(450)
	// Go uses explicit getter and setter methods rather than property syntax.
	fmt.Println("3. getters and setters:", auditAccount.getBalance())
}

func example4ModuleLevelEncapsulation() {
	taxed := applyTax(100)
	// Lowercase package-level names signal internal helpers and constants.
	fmt.Printf("4. module encapsulation: %.2f\n", taxed)
}

func example5InterfaceContract() {
	var payment processor = cardProcessor{}
	// Interfaces describe behavior contracts independently of concrete storage.
	fmt.Println("5. interface contract:", payment.process(199.99))
}

func example6ConstructorPattern() {
	auditAccount := newAccount("Dia", 725)
	// Factory-style constructors centralize initialization choices around a struct.
	fmt.Println("6. constructor pattern:", auditAccount.owner, auditAccount.getBalance())
}

func example7ImmutabilityPattern() {
	point := newImmutablePoint(4, 9)
	x, y := point.coordinates()
	// Go has no frozen struct, so immutability is a package-level discipline pattern.
	fmt.Println("7. immutability pattern:", x, y)
}

func main() {
	example1CustomADT()
	example2PrivateFields()
	example3GettersSetters()
	example4ModuleLevelEncapsulation()
	example5InterfaceContract()
	example6ConstructorPattern()
	example7ImmutabilityPattern()
}
