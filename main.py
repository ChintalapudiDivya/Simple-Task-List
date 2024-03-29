import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random

# Initialize an empty task list
tasks = pd.DataFrame(columns=['description', 'priority', 'status'])

# Load pre-existing tasks from a CSV file (if any)
try:
    tasks = pd.read_csv('C:/Users/hp/Downloads/basic/tasks.csv')
except FileNotFoundError:
    pass

# Function to save tasks to a CSV file
def save_tasks():
    tasks.to_csv('tasks.csv', index=False)

# Function to add a task to the list
def add_task(description, priority):
    global tasks  # Declare tasks as a global variable
    new_task = pd.DataFrame({'description': [description], 'priority': [priority], 'status': ['To Do']})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()

# Function to remove a task by description
def remove_task(description):
    tasks = tasks[tasks['description'] != description]
    save_tasks()

# Function to list all tasks
def list_tasks():
    if tasks.empty:
        print("No tasks available.")
    else:
        print(tasks)

# Function to prioritize a task by description
def prioritize_task(description, priority):
    tasks.loc[tasks['description'] == description, 'priority'] = priority
    save_tasks()

# Function to recommend a task based on machine learning
def recommend_task():
    if not tasks.empty:
        # Get tasks with 'To Do' status
        todo_tasks = tasks[tasks['status'] == 'To Do']
        
        if not todo_tasks.empty:
            # Choose a random task with 'To Do' status
            random_task = random.choice(todo_tasks['description'])
            print(f"Recommended task: {random_task}")
        else:
            print("No tasks available for recommendations.")
    else:
        print("No tasks available for recommendations.")

# Main menu
while True:
    print("\nTask Management App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Prioritize Task")
    print("5. Recommend Task")
    print("6. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        priority = input("Enter task priority (Low/Medium/High): ").capitalize()
        add_task(description, priority)
        print("Task added successfully.")

    elif choice == "2":
        description = input("Enter task description to remove: ")
        remove_task(description)
        print("Task removed successfully.")

    elif choice == "3":
        list_tasks()

    elif choice == "4":
        description = input("Enter task description to prioritize: ")
        priority = input("Enter new task priority (Low/Medium/High): ").capitalize()
        prioritize_task(description, priority)
        print("Task prioritized successfully.")

    elif choice == "5":
        recommend_task()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option.")