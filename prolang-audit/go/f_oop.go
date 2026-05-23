package main

import "fmt"

type report struct {
	title  string
	status string
}

func newReport(title string) *report {
	return &report{title: title, status: "draft"}
}

func (r *report) publish() {
	r.status = "published"
}

func (r report) describe() string {
	return fmt.Sprintf("%s [%s]", r.title, r.status)
}

type vehicle struct{}

func (vehicle) move() string {
	return "vehicle moves"
}

type car struct {
	vehicle
}

func (car) move() string {
	return "car drives"
}

type sender interface {
	send() string
}

type emailSender struct{}

func (emailSender) send() string {
	return "email sent"
}

type smsSender struct{}

func (smsSender) send() string {
	return "sms sent"
}

type archiver interface {
	archive() string
}

type stamper interface {
	stamp() string
}

type complianceReport struct{}

func (complianceReport) archive() string {
	return "archived"
}

func (complianceReport) stamp() string {
	return "2026-05-23"
}

type printableReport struct {
	title string
	pages int
}

// String returns the text form required by fmt.Stringer.
func (p printableReport) String() string {
	return fmt.Sprintf("%s (%d pages)", p.title, p.pages)
}

type secureReport struct {
	title      string
	accessCode string
}

func (s secureReport) canOpen(providedCode string) bool {
	return providedCode == s.accessCode
}

func notify(s sender) string {
	return s.send()
}

func example1StructWithMethods() {
	auditReport := newReport("Language Audit")
	auditReport.publish()
	// Methods attach behavior directly to structs through receivers.
	fmt.Println("1. struct with methods:", auditReport.describe())
}

func example2CompositionEmbedding() {
	driveable := car{}
	// Go models reuse through embedding and composition instead of inheritance.
	fmt.Println("2. composition and embedding:", driveable.move())
}

func example3MethodOverridingEquivalent() {
	base := vehicle{}
	derived := car{}
	// The outer type's method shadows the embedded method with the same name.
	fmt.Println("3. method shadowing:", base.move(), "vs", derived.move())
}

func example4Polymorphism() {
	// Interfaces let distinct concrete types satisfy a shared behavioral contract.
	fmt.Println("4. polymorphism:", notify(emailSender{}), notify(smsSender{}))
}

func example5MultipleInterfaceImplementation() {
	var archived archiver = complianceReport{}
	var stamped stamper = complianceReport{}
	// One concrete type can satisfy multiple interfaces at the same time.
	fmt.Println("5. multiple interfaces:", archived.archive(), stamped.stamp())
}

func example6StringerInterface() {
	reportValue := printableReport{title: "Status", pages: 10}
	// fmt.Stringer is Go's protocol-style hook for custom string formatting.
	fmt.Println("6. Stringer interface:", reportValue)
}

func example7Encapsulation() {
	reportValue := secureReport{title: "Restricted", accessCode: "1234"}
	// Methods expose controlled behavior while the struct keeps its internal fields together.
	fmt.Println("7. encapsulation:", reportValue.canOpen("0000"), reportValue.canOpen("1234"))
}

func main() {
	example1StructWithMethods()
	example2CompositionEmbedding()
	example3MethodOverridingEquivalent()
	example4Polymorphism()
	example5MultipleInterfaceImplementation()
	example6StringerInterface()
	example7Encapsulation()
}
