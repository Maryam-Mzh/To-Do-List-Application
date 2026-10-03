# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:59:27 2026

@author: Maryam
"""
import csv


class Task:
    """Represent a single task."""

    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority


class ToDoList:
    """Manage a list of tasks."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list."""
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, name):
        """Remove a task by name."""
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print("Task removed successfully.")
                return

        print("Task not found.")

    def show_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- To-Do List ---")

        for i, task in enumerate(self.tasks, start=1):
            print(f"\nTask {i}")
            print("Name:", task.name)
            print("Description:", task.description)
            print("Priority:", task.priority)

    def save_to_csv(self, filename):
        """Save all tasks to a CSV file."""
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["Name", "Description", "Priority"])

            for task in self.tasks:
                writer.writerow([
                    task.name,
                    task.description,
                    task.priority
                ])

        print("Tasks saved successfully.")

    def load_from_csv(self, filename):
        """Load tasks from a CSV file."""
        try:
            with open(filename, encoding="utf-8") as file:
                reader = csv.reader(file)

                next(reader, None)

                for row in reader:
                    name = row[0]
                    description = row[1]
                    priority = row[2]

                    task = Task(name, description, priority)
                    self.tasks.append(task)

            print("Tasks loaded successfully.")

        except FileNotFoundError:
            print("No saved file found. Starting with an empty list.")