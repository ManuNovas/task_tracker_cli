from sys import argv

from src.adapters.input.task_input_adapters import TaskInputAdapter

adapter = TaskInputAdapter()
adapter.main(argv)
