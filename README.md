# Library Management System

This Python program demonstrates a simple library system with books, members, and an interactive menu.

## How to Run

From the `library_management` folder, run:

```text
python library_management.py
```

Choose an option from the menu to add books, register members, borrow or return books, and display the books.

## Classes and Functions

- `Book` stores a book's title, author, and availability.
- `Member` stores the name of a library member.
- `Library` manages the lists of books and members.
- `run_library_menu` handles user input and starts the menu.

## Object Oriented Programming Concepts

### Classes and objects

The program uses classes as plans for creating objects. `Book`, `Member`, and `Library` are classes. Each time the program adds a book or member, it creates an object from one of these classes.

### Attributes

Attributes are variables that belong to an object. A `Book` object has `title`, `author`, and `available` attributes. A `Member` object has a `name` attribute.

### Methods and functions

Methods are functions inside a class. The `Library` class has methods such as `add_book`, `borrow_book`, and `return_book`. The `run_library_menu` function reads the user's choices and calls these methods.

### Constructors

The `__init__` method is a constructor. It runs when a new `Book`, `Member`, or `Library` object is created and gives the object its starting values.

### Using objects together

The `Library` object stores lists of `Book` and `Member` objects. This shows how objects can be placed inside another object and used together.

### Validation

The program checks whether a book exists before borrowing or returning it. It also prevents a book that is already borrowed from being borrowed again. A future improvement would be to check that titles, authors, and member names are not empty.

## Thought Process

Object-oriented programming is useful because books, members, and libraries are separate real-world concepts. The program uses simple classes, objects, attributes, methods, and a menu so beginners can follow how information is stored and changed.