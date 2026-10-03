# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:27:50 2026

@author: Maryam
"""

from Task import Task, ToDoList


todo = ToDoList()

filename = "tasks.csv"

todo.load_from_csv(filename)


while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Save tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter task name: ")
        description = input("Enter task description: ")

        print("\nSelect priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        priority_choice = input("Enter priority: ")

        if priority_choice == "1":
            priority = "High"

        elif priority_choice == "2":
            priority = "Medium"

        elif priority_choice == "3":
            priority = "Low"

        else:
            print("Invalid priority.")
            continue

        task = Task(name, description, priority)

        todo.add_task(task)

    elif choice == "2":

        name = input("Enter the name of the task to remove: ")

        todo.remove_task(name)

    elif choice == "3":

        todo.show_tasks()

    elif choice == "4":

        todo.save_to_csv(filename)

    elif choice == "5":

        todo.save_to_csv(filename)

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")