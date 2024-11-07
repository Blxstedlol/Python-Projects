import json
from colorama import Fore
import requests
current_version = 1.00

def Load():
    with open('list.json', 'r') as f:
        data = json.load(f)
    return data
def Save(data):
    with open('list.json', 'w') as f:
        json.dump(data, f, indent=4)
class Updating:
    @staticmethod
    def Check_For_Updates():
        pass
class ToDo:
    @staticmethod
    def Delete(task):
        data = Load()
        if "todo" not in data:
            print(f'{Fore.YELLOW}No Tasks Found!{Fore.RESET}')
            return
        for i, t in enumerate(data["todo"]):
            if t["task"] == task:
                del data["todo"][i]
                print(f'{Fore.CYAN}Deleted Task: {task}{Fore.RESET}')
                Save(data)
                return
        print('Task Not Found')
    @staticmethod
    def UpdateStatus(task, newstatus):
        data = Load()
        
        if "todo" in data:
            for t in data["todo"]:
                if t["task"] == task:
                    t["status"] = newstatus
                    Save(data)
                    print(f'{Fore.CYAN}Updated Task: {task}. to status: {newstatus}{Fore.RESET}')
                    return
        print(f'{Fore.YELLOW}Failed to Update Task Status{Fore.RESET}')
    @staticmethod
    def Add_ToDo(task, status):
        data = Load()
        if "todo" not in data:
            data["todo"] = []
        task_exists = any(t["task"] == task for t in data["todo"])
        if task_exists:
            print(f'{Fore.YELLOW} Task With the same name exists already{Fore.RESET}')
        else:
            data["todo"].append({"task": task, "status": status})
            print(f'{Fore.CYAN} Added Task: {task}')
        Save(data)
    @staticmethod
    def Menu():
        print(f"""
        Input the following numbers for the choices:
        1. Add a task.
        2. Remove a task.
        3. Update a tasks status.
        4. List all tasks.
            """)
        choice = input('--> ')
        if choice == '1':
            task_name = input('Task Name: ').lower()
            ToDo.Add_ToDo(task_name, 'incomplete')
            print('Task Added!')
        if choice == '2':
            task_name = input('Task Name: ').lower()
            ToDo.Delete(task_name)
            print('Task Removed!')
        if choice == '3':
            task_name = input('Task Name: ').lower()
            print("""
            1. Incomplete.
            2. In-Progress.
            3. Finished.
            4. Custom Status.
                """)
            
            choice = input('Enter Choice: ')
            if choice == '1':
                ToDo.UpdateStatus(task_name, 'Incomplete')
            if choice == '2':
                ToDo.UpdateStatus(task_name, 'In-Progress')
            if choice == '3':
                ToDo.UpdateStatus(task_name, 'Finished')
            if choice == '4':
                status = input('Custom Status: ')
                ToDo.UpdateStatus(task_name, status)
if __name__ == '__main__':
    ToDo.Menu()
    