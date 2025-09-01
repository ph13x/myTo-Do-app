import streamlit as st
import functions
import uuid
todos = functions.get_todos()

def add_todos():
    new_todo = st.session_state["new todo"]
    todos.append(new_todo + "\n") 
    functions.write_todos(todos)


st.title("To-Do App")
st.subheader("Your todo list")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add To-Do...",
               on_change=add_todos, key="new todo")


