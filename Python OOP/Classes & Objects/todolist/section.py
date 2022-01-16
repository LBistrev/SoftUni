from todolist.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for t in self.tasks:
            if t.name == new_task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        filtered_tasks = [t for t in self.tasks if t.name == task_name]
        if filtered_tasks:
            task = filtered_tasks[0]
            task.completed = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        result = [t for t in self.tasks if t.completed]
        return f"Cleared {len(result)} tasks."

    # def clean_section(self):
    #     counter_deleted_tasks = 0
    #     for t in self.tasks:
    #         if t.completed:
    #             self.t.remove(task)
    #             counter_deleted_tasks += 1
    #     return f"Cleared {counter_deleted_tasks} tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for t in self.tasks:
            result += f"{t.details()}\n"

        return result
