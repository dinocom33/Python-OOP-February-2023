from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task Name: {new_task.name} - Due Date: {new_task.due_date} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            curr_task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        curr_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for curr_task in self.tasks:
            if curr_task.completed:
                self.tasks.remove(curr_task)
                removed_tasks += 1

        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        tasks = '\n'.join(map(lambda t: t.details(), self.tasks))
        return f"Section {self.name}:\n" \
               f"{tasks}"
