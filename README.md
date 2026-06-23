# Fundamental-Booster
This Project Fundamental Booster is Basic Python project that boost your Basic understanding Regarding to Python language

# 🚀 Interactive Personal Data Collector

A lightweight, educational command-line application built in Python designed to demonstrate core programming fundamentals. This project serves as a **Fundamental Booster** by interacting with users to collect personal information, perform runtime type inspection, and explore Python object identities.

---

## 🚀 Key Features

### Dynamic Interactive CLI

Provides an intuitive step-by-step user experience for collecting personal information through the command line.

### Strict Data-Type Enforcement

Automatically converts and validates multiple primitive data types including:

* String (`str`)
* Integer (`int`)
* Float (`float`)

### Runtime Type Inspection

Utilizes Python's built-in `type()` function to display the actual datatype of each user input.

### Object Identity Analysis

Demonstrates Python's internal object model by displaying unique object identifiers using `id()`.

### Automated Birth Year Calculation

Calculates an approximate birth year using the provided age value.

---

## 🛠️ Tech Stack & Concepts Covered

### Language

* Python 3.x

### Core Concepts Demonstrated

* Standard Input/Output Handling (`input()`, `print()`)
* Type Casting (`int()`, `float()`)
* Runtime Type Inspection (`type()`)
* Object Identity Resolution (`id()`)
* Formatted String Literals (f-Strings)
* Variable Assignment
* Arithmetic Operations
* Console Application Development

---

## 📦 Getting Started

### Prerequisites

Ensure Python 3.x is installed on your system.

Verify installation:

```bash
python --version
```

---

### Installation

Clone the repository:

```bash
git clone https://github.com/Dixit2307/Interactive-Personal-Data-Collector.git
```

Navigate to the project directory:

```bash
cd Interactive-Personal-Data-Collector
```

---

### Execute the Program

```bash
python "project 1 Fundamentel Booster.py.py"
```

---

## 🖥️ Sample Output

```text
Welcome to Interactive Personal Data Collecter program

Please Enter your name: Dixit
Please Enter your Age: 20
Please Enter your height in meters: 1.75
Please Enter your favourite number: 7

Thank you! for your information.

here is your information we collect

Name: Dixit (Type: <class 'str'>)
Age: 20 (Type: <class 'int'>)
Height: 1.75 (Type: <class 'float'>)
Favourite: 7 (Type: <class 'int'>)

your birth year is approximately (2006 based on your age of 20)

Thank you for using the personal Data collector. Goodbye!
```

---

## 🧠 Architectural Highlights

### 1. Runtime Type Safety

User input received from the terminal is initially treated as a string.

```python
age = int(input("Enter Age: "))
height = float(input("Enter Height: "))
```

This project demonstrates explicit type conversion to enable numerical computation.

---

### 2. Object Identity Inspection

Python variables reference objects in memory.

```python
print(id(name))
print(id(age))
```

The `id()` function returns a unique identifier for an object during its lifetime, helping beginners understand Python's object model.

---

### 3. String Formatting

The project uses modern f-strings for readable output formatting.

```python
print(f"Name: {name}")
```

---

## 📂 Project Structure

```text
Interactive-Personal-Data-Collector/
│
├── project 1 Fundamentel Booster.py.py
├── README.md
│
└── assets/
    ├── screenshots/
    └── demo/
```

---

## 📈 Future Enhancements

* Input Validation
* Exception Handling
* CSV Export Support
* JSON Data Storage
* SQLite Integration
* Tkinter GUI Version
* Flask Web Application
* Automated Unit Testing

---

## 👨‍💻 Author

### Dixit Maru

**AI/ML | Data Science | Data Analytics Student**

🔗 GitHub: https://github.com/Dixit2307

🔗 LinkedIn: https://www.linkedin.com/in/dixit-maru-04383240b/

---

## ⭐ Support

If you found this project useful:

* Star the repository
* Fork the project
* Share feedback
* Suggest improvements

---

### Built with ❤️ using Python
