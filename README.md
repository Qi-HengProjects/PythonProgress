# Expense Tracker Core Engine

An object-oriented expense tracking engine built with pure Python. This project transitions away from basic monolithic scripting by implementing a decoupled architecture, strict business invariants, and custom serialization workflows.

## Architectural Overview

This system is built using **Domain-Driven Design (DDD)** principles and is split into distinct layers to ensure a strict **Separation of Concerns**:

* **Domain Layer (`Expense`, `ExpenseCategory`):** Utilizes type-safe, immutable dataclasses paired with Python `Enum` structures to define the absolute core business truths.
* **State / Repository Layer (`ExpenseRepository`):** Acts as the single source of truth for in-memory data management. It manages collections using $O(1)$ dictionary lookups and functions as the primary gatekeeper for runtime modifications.
* **Persistence Layer (`JSONStorageController`):** A dedicated Data Access Object (DAO) responsible for translating memory states into text-based streams. It handles custom serialization and hydration pipelines for non-primitive types (`Decimal` and `date`) without relying on heavy external frameworks.
* **Presentation Layer (`main`):** A lightweight Command Line Interface (CLI) that orchestrates user inputs, manages primitive-to-rich type formatting boundaries, and captures propagated business logic exceptions cleanly.

---

## 🧭 System Data Flow
[ Disk: JSON Text ] ◄──► [ Storage Controller (Serialization) ] ◄──► [ Repository (In-Memory RAM) ] ◄──► [ User Interface CLI ]


1.  **Bootstrapping:** On startup, raw JSON strings are pulled from disk, hydrated into rich domain objects by the controller, and mapped into the repository's internal state.
2.  **Commit Lifecycle:** On exit, the repository hands a snapshot list of live domain objects to the controller. The controller strips complex objects down to string primitives and writes them atomically back to the file system.

---

## 🛠️ Core Engineering Features

* **Financial Precision:** Uses Python's `Decimal` type instead of floating-point numbers to eliminate binary floating-point rounding errors.
* **State Integrity & Auto-Incrementation:** Implements defensive tracking on loaded files to ensure newly generated entity IDs never overwrite or corrupt existing historical data.
* **Input Gatekeeping:** Enforces data invariants (e.g., prohibiting negative amounts or empty strings) at the domain layer boundary, throwing safe exceptions before corrupt data can touch live state memory.

---

## 🚀 Future Roadmap

Because the backend engine is completely decoupled from the data storage format and presentation interface, this project is prepared for the following upgrades:
* [ ] Swap out the `JSONStorageController` for an `SQLiteStorageController` to allow database row queries without modifying the repository layer.
* [ ] Expose the repository methods over an HTTP network layer using a web framework like **FastAPI**.
* [ ] Connect the core engine to a desktop Graphical User Interface (GUI) via **Tkinter** 
