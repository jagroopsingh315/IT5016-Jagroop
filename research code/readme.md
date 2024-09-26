**** Student Management System ****

Overview:

The Student Management System (SMS) is a Python program that helps manage student information, course enrollments, and grades. It uses object-oriented programming (OOP) principles to encapsulate related data and behavior, making the code organized and reusable.

Features:

Add students and courses
Enroll students in courses
Assign grades to students
Calculate and display GPA for each student
Print detailed student information including enrolled courses and grades.

Code Structure:

The main components of the system include:
StudentManagementSystem: The core class that manages students and courses.
Student: Represents a student and handles enrollment and grade management.
Course: Represents a course and manages enrolled students and their grades.

Usage:

Follow the prompts in the command line to interact with the system. You can:
Add a student
Add a course
Enroll a student in a course
View student information.

Software Design Principles:

1. Single Responsibility Principle (SRP)
Each class in the system has a single responsibility:

StudentManagementSystem is responsible for managing the overall operations of the student and course management.
Student is responsible for managing student-specific data and logic.
Course is responsible for managing course-specific data and logic.
This separation ensures that each class is easy to understand, maintain, and modify.

2. Open/Closed Principle (OCP)
The system is designed to be extendable without modifying existing code. For example, if new features need to be added (like a new grading system), new methods or classes can be introduced without altering the existing codebase, thus adhering to this principle.

Other Principles:
Single Responsibility Principle: Each class has a single responsibility. For example, the Student class is solely responsible for managing student data and behaviors, while the Course class handles course-related functionalities.
Open/Closed Principle: The system is designed to be extendable. New features (e.g., additional student attributes or course types) can be added without modifying existing code.
