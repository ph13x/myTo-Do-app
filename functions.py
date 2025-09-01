import streamlit as st
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a Text file and return the list
    of todos.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write todos to filepath
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)