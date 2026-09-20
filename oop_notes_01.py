"""
Cambridge International AS & A Level Computer Science (9618)
Paper 4: Practical Programming Paradigm (OOP)

File: oop_notes_01.py
Instructor: Tr. Wai Lin Htet
Description: Educational code demonstrations covering classes, constructor delegation,
             encapsulation, polymorphism, aggregation, and operator overloading.
"""

import math


# ==============================================================================
# 1. CORE INHERITANCE & METHOD OVERRIDING
# ==============================================================================

class Parent:
    """Base class demonstrating fundamental constructor logic and method definition."""

    def __init__(self, value: int):
        self.value = value

    def display(self) -> str:
        return f"Value: {self.value}"


class Child(Parent):
    """Derived class demonstrating super() delegation and method overriding (Polymorphism)."""

    def __init__(self, value: int, extra: str):
        super().__init__(value)
        self.extra = extra

    def display(self) -> str:
        # Overrides Parent.display()
        return f"Value: {self.value}, Extra: {self.extra}"


# ==============================================================================
# 2. HIERARCHICAL INHERITANCE: DEVICES
# ==============================================================================

class Phone:
    """Superclass representing a basic telecommunication device."""

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def make_call(self, number: str) -> str:
        return f"Calling {number} from {self.brand} {self.model}..."

    def send_text(self, number: str, message: str) -> str:
        return f"Sending '{message}' to {number}"

    def device_info(self) -> str:
        return f"Basic Phone: {self.brand} {self.model}"


class Smartphone(Phone):
    """Subclass adding platform-specific capabilities."""

    def __init__(self, brand: str, model: str, os_name: str, storage_gb: int):
        super().__init__(brand, model)
        self.os_name = os_name
        self.storage_gb = storage_gb
        self.installed_apps = []

    def install_app(self, app_name: str) -> str:
        self.installed_apps.append(app_name)
        return f"Installed {app_name} on {self.model}."

    def device_info(self) -> str:
        # Polymorphic override
        return (
            f"Smartphone: {self.brand} {self.model} "
            f"running {self.os_name} ({self.storage_gb}GB)"
        )


# ==============================================================================
# 3. MULTI-LEVEL INHERITANCE: COMPUTERS
# ==============================================================================

class Computer:
    """Base level of a multi-tiered inheritance hierarchy."""

    def __init__(self, cpu: str, ram_gb: int):
        self.cpu = cpu
        self.ram_gb = ram_gb

    def power_on(self) -> str:
        return "System booting up..."

    def specs(self) -> str:
        return f"CPU: {self.cpu}, RAM: {self.ram_gb}GB"


class Laptop(Computer):
    """Second-tier class introducing battery and mobility attributes."""

    def __init__(self, cpu: str, ram_gb: int, battery_mah: int, weight_kg: float):
        super().__init__(cpu, ram_gb)
        self.battery_mah = battery_mah
        self.weight_kg = weight_kg

    def check_battery(self) -> str:
        return f"Battery capacity: {self.battery_mah} mAh"

    def specs(self) -> str:
        # Reuses the base class representation and appends new metrics
        return f"{super().specs()}, Weight: {self.weight_kg}kg"


class MacBook(Laptop):
    """Terminal derived class with vendor-specific functions."""

    def __init__(self, model_name: str, chip: str, ram_gb: int, battery_mah: int, weight_kg: float):
        super().__init__(cpu=chip, ram_gb=ram_gb, battery_mah=battery_mah, weight_kg=weight_kg)
        self.model_name = model_name
        self.os_name = "macOS"

    def use_airdrop(self, file_name: str) -> str:
        return f"Sending {file_name} via AirDrop from {self.model_name}."

    def specs(self) -> str:
        return (
            f"{self.model_name} ({self.os_name}) - "
            f"Chip: {self.cpu}, RAM: {self.ram_gb}GB, Weight: {self.weight_kg}kg"
        )


# ==============================================================================
# 4. POLYMORPHISM & ABSTRACT INTERFACE
# ==============================================================================

class Animal:
    """Abstract interface defining required behavior for concrete subclasses."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self) -> str:
        """Enforces implementation in subclasses (Interface Abstraction)."""
        raise NotImplementedError("Subclasses must implement abstract method speak()")

    def get_info(self) -> str:
        return f"{self.name} is {self.age} years old"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return "Woof"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


# ==============================================================================
# 5. DATA ENCAPSULATION, AGGREGATION & OPERATOR OVERLOADING
# ==============================================================================

class Point2D:
    """Represents a coordinate point demonstrating encapsulation and dunder methods."""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        # Strict defensive programming and type validation
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numeric (int or float).")
        
        # Private attributes (A-Level Encapsulation standard)
        self.__x = float(x)
        self.__y = float(y)

    # Getters
    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    # Setters
    def set_x(self, x: float):
        if not isinstance(x, (int, float)):
            raise TypeError("Coordinate must be numeric.")
        self.__x = float(x)

    def set_y(self, y: float):
        if not isinstance(y, (int, float)):
            raise TypeError("Coordinate must be numeric.")
        self.__y = float(y)

    def __str__(self) -> str:
        return f"<{self.__x}, {self.__y}>"

    def __repr__(self) -> str:
        return f"Point2D(x={self.__x}, y={self.__y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return False
        return self.__x == other.__x and self.__y == other.__y

    def __add__(self, other: "Point2D") -> "Point2D":
        if not isinstance(other, Point2D):
            raise TypeError("Addition requires another Point2D instance.")
        return Point2D(self.__x + other.__x, self.__y + other.__y)

    def scale(self, factor: float):
        self.__x *= factor
        self.__y *= factor

    def distance_to(self, other: "Point2D") -> float:
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)


class Polygon:
    """Demonstrates Aggregation: A Polygon 'has' many Point2D instances."""

    def __init__(self):
        self.__points: list[Point2D] = []

    def add_point(self, point: Point2D):
        if not isinstance(point, Point2D):
            raise TypeError("Item appended must be an instance of Point2D.")
        self.__points.append(point)

    def perimeter(self) -> float:
        if len(self.__points) < 2:
            return 0.0

        total = 0.0
        # Calculate distance across all adjacent vertices
        for i in range(len(self.__points) - 1):
            total += self.__points[i].distance_to(self.__points[i + 1])

        # Close polygon cycle: connect tail to head
        total += self.__points[-1].distance_to(self.__points[0])
        return total

    def __len__(self) -> int:
        return len(self.__points)

    def __str__(self) -> str:
        return " -> ".join(str(pt) for pt in self.__points)


# ==============================================================================
# MAIN EXECUTION GUARD (A-LEVEL PAPER 4 DRIVER PATTERN)
# ==============================================================================

if __name__ == "__main__":
    print("--- 1. Basic Inheritance ---")
    item = Child(10, "A")
    print(item.display())

    print("\n--- 2. Smartphone & Laptop Hierarchy ---")
    old_phone = Phone("Nokia", "3310")
    smart_phone = Smartphone("Apple", "iPhone 15", "iOS", 512)

    print(old_phone.make_call("123-4567"))
    print(smart_phone.make_call("979-7678"))
    print(smart_phone.install_app("Canvas"))
    print(old_phone.device_info())
    print(smart_phone.device_info())

    desktop = Computer("Intel i7", 32)
    generic_laptop = Laptop("AMD Ryzen 7", 16, 5000, 1.8)
    my_mac = MacBook("MacBook Air", "M4", 16, 5200, 1.24)

    devices: list[Computer] = [desktop, generic_laptop, my_mac]
    for dev in devices:
        print(dev.specs())

    print("\n--- 3. Polymorphism with Abstract Hierarchy ---")
    animals: list[Animal] = [
        Dog("Buddy", 3, "Labrador"),
        Cat("Kitty", 2)
    ]
    for animal in animals:
        print(f"{animal.get_info()} | Sound: {animal.speak()}")

    print("\n--- 4. Operator Overloading & Aggregation (Geometry) ---")
    p1 = Point2D(0, 0)
    p2 = Point2D(3, 4)
    p3 = Point2D(0, 0)

    print(f"p1: {p1}, p2: {p2}")
    print(f"p1 == p3: {p1 == p3}")
    print(f"Distance between p1 and p2: {p1.distance_to(p2)}")
    
    # Using __add__ overload
    p_sum = p1 + p2
    print(f"p1 + p2: {p_sum}")

    # Polygon Aggregation
    rectangle = Polygon()
    rectangle.add_point(Point2D(0, 0))
    rectangle.add_point(Point2D(3, 0))
    rectangle.add_point(Point2D(3, 4))
    rectangle.add_point(Point2D(0, 4))

    print(f"Polygon vertices ({len(rectangle)} points): {rectangle}")
    print(f"Perimeter: {rectangle.perimeter()}")
