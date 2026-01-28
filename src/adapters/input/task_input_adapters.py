from src.ports.input.task_input_ports import TaskInputPort


class TaskInputAdapter:
    input_port: TaskInputPort

    def __init__(self):
        self.input_port = TaskInputPort()

    def main(self, argv: list[str]):
        command = argv[1]
        if command == "add":
            task = self.input_port.add(argv[2])
            print(f"Added task with ID {str(task.id)}")
