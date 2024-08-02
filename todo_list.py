"""
To-Do List Application

A simple terminal-based application to manage to-do items.
Features include adding, reading, editing, deleting, marking as finished,
and saving/loading tasks from a file.

"""


class ToDoItem:
    def __init__(self, task=None, finished=False):
        self.task = task
        self.finished = finished

    def __str__(self):
        status = "Finished" if self.finished else "Not Finished"
        return f"{self.task} [{status}]"


class ToDoList:
    def __init__(self):
        self.todo_list = []

    def add_new_todo(self, task):
        self.todo_list.append(ToDoItem(task))
        self.save_to_file()
        print("Task has been added successfully..!")

    def save_to_file(self, filename="todo_list.txt"):
        with open(filename, 'w') as file:
            for item in self.todo_list:
                file.write(f"{item.task},{item.finished}\n")

    def load_from_file(self, filename="todo_list.txt"):
        try:
            with open(filename, 'r') as file:
                self.todo_list = []
                for line in file:
                    task, finished = line.strip().split(',')
                    self.todo_list.append(ToDoItem(task, finished == 'True'))

        except FileNotFoundError:
            pass

    def read_todo(self):
        print("*" * 20, "YOUR TODOS", "*" * 20)
        for i in range(len(self.todo_list)):
            print(i + 1, ": ", self.todo_list[i])
        if not self.todo_list:
            print("add some works...")

    def edit_todo(self, index, new_task):
        try:
            if self.todo_list[index]:
                self.todo_list[index].task = new_task
                print("Task has been updated Successfully..!")

        except IndexError:
            print("Invalid task number!")

    def delete_todo(self, index):
        try:
            if self.todo_list[index]:
                self.todo_list.pop(index)
                print("Task has been deleted Successfully..!")
        except IndexError:
            print("Invalid task number!")

    def mark_as_finished(self, index):
        try:
            if self.todo_list[index]:
                self.todo_list[index].finished = True
                print("Task has been finished Successfully..!")
        except IndexError:
            print("Invalid task number!")

    def clear_all(self, filename="todo_list.txt"):
        self.todo_list = []
        with open(filename, 'w') as file:
            pass
        print("All tasks cleared and file content deleted successfully!")


def main():
    todo_list = ToDoList()
    todo_list.load_from_file()

    while True:
        todo_list.read_todo()
        print("\nPlease choose an option:")
        print("1. Add To-Do Item")
        print("2. Edit To-Do Item")
        print("3. Delete To-Do Item")
        print("4. Clear all Todos")
        print("5. Mark as Finished")

        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task details: ")
            todo_list.add_new_todo(task)
        elif choice == "2":
            index = int(input("Select a task to edit (number): ")) - 1
            new_task = input("Enter the new task details: ")
            todo_list.edit_todo(index, new_task)
        elif choice == "3":
            index = int(input("Select a task to delete (number): ")) - 1
            todo_list.delete_todo(index)
        elif choice == "4":
            option = input("THIS WILL CLEAR ALL OF YOUR TODOS...\n Enter \"Y\" For Clearing \"N\" For going back :  ")
            if option == "Y" or option == "y":
                todo_list.clear_all()
            elif option == "N" or option == "n":
                pass
            else:
                print("invalid selection...!")

        elif choice == "5":
            index = int(input("Select a task to mark as finished (number): ")) - 1
            todo_list.mark_as_finished(index)
        elif choice == "6":
            todo_list.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
