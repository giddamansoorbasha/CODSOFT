class ToDo:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        try:
            task = input("Enter the task: ")
            self.tasks.append(task)
            print("Task Added Successfully!")
        except Exception as e:
            print(f"Error : {e}")

    def delete_task(self):
        try:
            task_num = int(input("Enter the task no to delete: "))
            if task_num < 1 or task_num > len(self.tasks):
                print("Invalid task number.")
                return None
            del_task = self.tasks.pop(task_num-1)
            return del_task
        except Exception as e:
            print(f"Error : {e}")

    def update_task(self):
        try:
            task_num = int(input("Enter the task number: "))
            if task_num < 1 or task_num > len(self.tasks):
                print("Invalid task number.")
                return None
            new_task = input("Enter the new task: ")
            self.tasks[task_num-1] = new_task
            print("Task Updated Successfully!")
        except Exception as e:
            print(f"Error : {e}")
        
    def display_tasks(self):
        try:
            if not(self.tasks):
                print("No Tasks Found!")
                return
            print('\nS.no   Task\n')
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx})     {task}")
        except Exception as e:
            print(f"Error : {e}")

def main():
    try:
        todo = ToDo()
        print("\n-----Welcome to To-Do List-----")
        while True:
            print("\n===== TO-DO LIST MENU =====")
            choice = int(input("\n1) Add Task\n2) Delete Task\n3) Update Task\n4) Display Tasks\n5) Exit\n\nEnter Your Choice : "))
            if choice == 1:
                todo.add_task()
            elif choice == 2:
                print(f"Deleted Task : {todo.delete_task()}")
            elif choice == 3:
                todo.update_task()
            elif choice == 4:
                todo.display_tasks()
            elif choice == 5:
                print("Thank You, Bye!")
                break
            else:
                print("Invalid Input")
    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    main()
