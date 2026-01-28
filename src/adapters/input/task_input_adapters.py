from src.ports.input.task_input_ports import TaskInputPort


class TaskInputAdapter:
    input_port: TaskInputPort

    def __init__(self):
        self.input_port = TaskInputPort()

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
                print(f"Task {id} doesn't exists")
        else:
            print("Unknown command or not enough args to execute")
