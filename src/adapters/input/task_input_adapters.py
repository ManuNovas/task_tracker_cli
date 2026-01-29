from src.ports.input.task_input_ports import TaskInputPort


class TaskInputAdapter:
    input_port: TaskInputPort

    def __init__(self):
        self.input_port = TaskInputPort()

    def task_not_found(self, id: int):
        print(f"Task {str(id)} doesn't exists")

    def main(self, argv: list[str]):
        argl = len(argv)
        if argl < 2:
            print("You should specify a command")
            return 1
        command = argv[1]
        if command == "add" and argl == 3:
            description = argv[2]
            task = self.input_port.add(description)
            print(f"Added task with ID {str(task.id)}")
        elif command == "update" and argl == 4:
            id = int(argv[2])
            description = argv[3]
            task = self.input_port.update(id, description)
            if task is not None:
                print(f"Updated task with ID {str(task.id)}")
            else:
                self.task_not_found(id)
        elif command == "delete" and argl == 3:
            id = int(argv[2])
            task = self.input_port.delete(id)
            if task is not None:
                print(f"Deleted task with ID {str(task.id)}")
            else:
                self.task_not_found(id)
        elif command == "mark-in-progress" and argl == 3:
            id = int(argv[2])
            task = self.input_port.mark_in_progress(id)
            if task is not None:
                print(f"Marked task {id} in progress")
            else:
                self.task_not_found(id)
        elif command == "mark-done" and argl == 3:
            id = int(argv[2])
            task = self.input_port.mark_done(id)
            if task is not None:
                print(f"Marked task {id} done")
            else:
                self.task_not_found(id)
        elif command == "list":
            status = argv[2] if len(argv) > 2 else None
            tasks = self.input_port.list(status)
            for task in tasks:
                print(f"{task["id"]}. {task["description"]} - {task["status"]}")
        else:
            print("Unknown command or not enough args to execute")
        return 0
