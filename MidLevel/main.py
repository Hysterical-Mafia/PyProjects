# CLI ToDo List


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self):
        print("D")

    def remove_task(self):
        print("Do")

    def view_tasks(self):
        print("Don")

    def complete_tasks(self):
        print("Done")

    def quit_task(self):
        print("H")


    def get_options(self):
        return {
            "1": self.add_task,
            "2": self.remove_task,
            "3": self.view_tasks,
            "4": self.complete_tasks,
            "5": self.quit_task,
            "6": "placeholder",
        }


    def print_menu(self):
        descriptions = {
            "1": "Add a task",
            "2": "Remove a task",
            "3": "View tasks",
            "4": "Complete a task",
            "5": "Quit the program",
            "6": "Placeholder task",
        }
        for i in descriptions:
            print(f"{i} : {descriptions[i]}")


def main():
    manager = TaskManager()
    manager.print_menu()
    options = manager.get_options()
    choice = input("Choose a Task (1-6)")
    if choice in options:
        options[choice]()
    else:
        print("Invalid Choice")


main()
