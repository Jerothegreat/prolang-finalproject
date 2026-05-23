# Prolang Audit: Python vs. Go

This repository is a submission-ready "Language Implementation Audit" project comparing Python and Go across eight programming-language concept categories, performance benchmarks, and a small refactoring exercise.

## Requirements

- Python 3.10 or newer
- Go 1.22 or newer

## Project Structure

```text
prolang-audit/
├── README.md
├── PROLANG_FINAL_PROJ_COMPLETED.md
├── go.mod
├── python/
├── go/
├── benchmarks/
└── refactor/
```

## How to Run the Python Files

Run each concept file directly from the repository root:

```powershell
python python/A_data_types.py
python python/B_expressions.py
python python/C_control_structures.py
python python/D_subprograms.py
python python/E_adt_encapsulation.py
python python/F_oop.py
python python/G_concurrency.py
python python/H_exception_handling.py
```

## How to Run the Go Files

Each Go file is a standalone demo and should be run individually:

```powershell
go run go/a_data_types.go
go run go/b_expressions.go
go run go/c_control_structures.go
go run go/d_subprograms.go
go run go/e_adt_encapsulation.go
go run go/f_oop.go
go run go/g_concurrency.go
go run go/h_exception_handling.go
```

## Benchmarks

Run the Python benchmark analysis:

```powershell
python benchmarks/perf_analysis.py
```

Run the Go benchmark suite:

```powershell
go test ./benchmarks -bench . -run ^$
```

## Refactor Example

Run the original and cleaned versions:

```powershell
python refactor/smelly_code.py
python refactor/clean_code.py
```

## Go Vet

Because the `go/` folder intentionally contains multiple standalone `package main` demo files, vet them one file at a time:

```powershell
go vet go/a_data_types.go
go vet go/b_expressions.go
go vet go/c_control_structures.go
go vet go/d_subprograms.go
go vet go/e_adt_encapsulation.go
go vet go/f_oop.go
go vet go/g_concurrency.go
go vet go/h_exception_handling.go
```

## Main Deliverable

The full written audit is in [PROLANG_FINAL_PROJ_COMPLETED.md](PROLANG_FINAL_PROJ_COMPLETED.md).
