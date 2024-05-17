
def get_todo():
    todos=[]
    with open("todos.txt", "r") as f:
        for i in f:
            todos.append(i.strip())
    return todos
    
def append_todo(todos):
    with open("todos.txt", "w") as f:
        for i in todos:
            f.write(i.strip()+"\n")

while True:
    title = input("enter the choice\n")
    title = title.strip()
    
    if title.startswith("add"):
        todo = title[4:]
        todos=get_todo()
        todos.append(todo + '\n')
        append_todo(todos)

    elif title.startswith("show"):
        todos = get_todo()
        for n, i in enumerate(todos):
            i = i.strip('\n')
            n = n + 1
            print(n, "-", i)

    elif title.startswith("edit"):
        try:
            n = int(title[5:])
            n = n - 1
            todos=get_todo()
            todos[n] = input("enter the new todo")
            append_todo()

        except ValueError:
            print("Enter a number following your command")
            continue

    elif title.startswith("done"):
        try:
            n = int(title[5:])
            todos=get_todo()
            todos.pop(n - 1)
            append_todo(todos)
            
        except ValueError or IndexError:
            print("Enter a number following your command")
            continue
    elif title.startswith("exit"):
        print("byee!!")
        break

    else:
        print("try again biach ")
