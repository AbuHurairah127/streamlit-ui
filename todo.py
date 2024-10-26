import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Title and input box for new tasks
st.title("Basic To-Do App")
new_task = st.text_input("Enter a new task:", "")

# Add a new task
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task before adding.")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([8, 1])
        col1.write(f"{i + 1}. {task}")
        # Delete task button
        if col2.button("Delete", key=i):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()  # Refresh to reflect task removal
else:
    st.write("No tasks yet!")

