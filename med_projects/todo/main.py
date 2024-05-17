def get_todo():
    todos = []
    try:
        with open("todos.txt", "r") as f:
            for i in f:
                todos.append(i.strip())
    except FileNotFoundError:
        pass  # If the file doesn't exist, we start with an empty list
    return todos

def append_todo(todo):
    with open("todos.txt", "a") as f:
        f.write(todo + '\n')  # Append the new todo item to the file

def write_todos(todos):
    with open("todos.txt", "w") as f:
        for todo in todos:
            f.write(todo + '\n')  # Write each todo item to the file

while True:
    title = input("Enter the choice (type 'exit' to quit):\n")
    title = title.strip()
    
    if title.startswith("add"):
        todo = title[4:].strip()  # Get the todo item text after "add"
        append_todo(todo)  # Append the new todo to the file
        print("Todo added.")

    elif title.startswith("show"):
        todos = get_todo()
        for n, i in enumerate(todos):
            print(f"{n + 1} - {i}")  # Print the todos with numbering

    elif title.startswith("edit"):
        try:
            n = int(title[5:]) - 1  # Get the index of the todo to edit
            todos = get_todo()
            if 0 <= n < len(todos):
                new_todo = input("Enter the new todo: ").strip()
                todos[n] = new_todo  # Update the todo item at the specified index
                write_todos(todos)  # Write the updated list back to the file
                print("Todo updated.")
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Please enter a valid todo number.")
        except IndexError:
            print("Invalid todo number.")

    elif title.startswith("done"):
        try:
            n = int(title[5:]) - 1  # Get the index of the todo to remove
            todos = get_todo()
            if 0 <= n < len(todos):
                todos.pop(n)  # Remove the todo item at the specified index
                write_todos(todos)  # Write the updated list back to the file
                print("Todo marked as done and removed.")
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Please enter a valid todo number.")
        except IndexError:
            print("Invalid todo number.")

    elif title.lower() == "exit":
        print("Bye!")
        break

    else:
        print("Invalid choice. Please enter 'add', 'show', 'edit', 'done', or 'exit'.")