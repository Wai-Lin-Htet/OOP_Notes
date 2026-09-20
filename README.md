# Cambridge A-Level Computer Science (9618)
## Topic: Object-Oriented Programming (Paper 4 Reference)
**Instructor:** Tr. Wai Lin Htet  
**Module:** OOP Notes 1 — Core Principles, Inheritance & Aggregation

---

### 1. Key Terminology & Definitions

| Term | A-Level Syllabus Definition | Python Implementation |
| :--- | :--- | :--- |
| **Class** | A user-defined blueprint or template from which individual objects are created. | `class ClassName:` |
| **Object (Instance)** | An identifiable runtime entity containing state (attributes) and behavior (methods). | `my_obj = ClassName()` |
| **Attribute** | A variable belonging to a class or instance that represents an entity's internal state. | `self.__attribute_name` |
| **Method** | A procedure or function defined within a class that acts on object attributes. | `def method_name(self):` |
| **Constructor** | A special method called automatically when an object instance is instantiated. | `def __init__(self, ...):` |
| **Reference Parameter** | Explicit reference to the current object instance within its own methods. | `self` |

---

### 2. The Four Pillars of OOP

#### 1. Encapsulation
* **Concept:** Bundling data (attributes) and operations (methods) together while restricting direct access to the object's internal representation.
* **Exam Application:** Private attributes are indicated by prepending a double underscore (`self.__variable`). Access and mutations must happen via public getters and setters to protect data integrity.

#### 2. Inheritance
* **Concept:** Mechanism where a derived class (*subclass*) inherits attributes and behaviors from a base class (*superclass*).
* **Exam Application:** Promotes code reusability. In Python, subclasses call `super().__init__(...)` to delegate constructor initialization upward.

#### 3. Polymorphism
* **Concept:** The ability to present the same interface for differing underlying data types or classes.
* **Exam Application:** Typically demonstrated via **method overriding**, where a subclass provides its own specific implementation of a method defined in its superclass.

#### 4. Abstraction
* **Concept:** Hiding structural and procedural complexity while exposing only relevant interfaces.
* **Exam Application:** Base classes define interfaces (e.g., raising `NotImplementedError` or using Python's `abc` module), forcing subclasses to supply the implementation.

---

### 3. Magic (Dunder) Methods Reference

| Dunder Method | Purpose | Trigger Syntax |
| :--- | :--- | :--- |
| `__init__(self, ...)` | Constructor/Initializer | `obj = MyClass()` |
| `__str__(self)` | User-facing string conversion | `print(obj)` or `str(obj)` |
| `__repr__(self)` | Developer/debugging representation | `repr(obj)` |
| `__eq__(self, other)` | Equality comparison | `obj1 == obj2` |
| `__add__(self, other)` | Operator overloading for addition | `obj1 + obj2` |
| `__len__(self)` | Length container interrogation | `len(obj)` |
