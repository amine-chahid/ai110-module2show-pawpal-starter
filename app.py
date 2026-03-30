import streamlit as st
from datetime import datetime

# ✅ Step 1: Import backend (connection)
from pawpal_system import Owner, Pet, Task, Scheduler

st.title("🐾 PawPal+")

# ✅ Step 2: Session state (memory)
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Amine")
    st.session_state.scheduler = Scheduler(st.session_state.owner)

owner = st.session_state.owner
scheduler = st.session_state.scheduler

# -------------------------
# 🐶 Add Pet
# -------------------------
st.header("Add Pet")

pet_name = st.text_input("Pet Name")
pet_type = st.text_input("Pet Type")

if st.button("Add Pet"):
    if pet_name and pet_type:
        new_pet = Pet(pet_name, pet_type)
        owner.add_pet(new_pet)  # ✅ connect to backend
        st.success(f"{pet_name} added successfully!")
    else:
        st.warning("Please fill all fields")

# Show pets
if owner.pets:
    st.subheader("Your Pets")
    for pet in owner.pets:
        st.write(f"• {pet.name} ({pet.species})")

# -------------------------
# 📅 Add Task
# -------------------------
st.header("Add Task")

task_name = st.text_input("Task Name")
task_time = st.time_input("Task Time")
priority = st.slider("Priority", 1, 5, 3)

if st.button("Add Task"):
    if owner.pets:
        pet = owner.pets[0]  # simple version
        task_datetime = datetime.combine(datetime.today(), task_time)

        task = Task(task_name, task_datetime, priority)
        pet.add_task(task)  # ✅ connect to backend

        st.success("Task added successfully!")
    else:
        st.warning("Please add a pet first!")

# -------------------------
# 📋 Show Schedule
# -------------------------
st.header("Today's Schedule")

tasks = scheduler.sort_tasks()

if tasks:
    for task in tasks:
        status = "✅ Done" if task.completed else "⏳ Pending"
        st.write(
            f"• {task.title} at {task.time.strftime('%I:%M %p')} "
            f"(Priority {task.priority}) - {status}"
        )
else:
    st.write("No tasks yet.")

# ⚠️ Show conflicts in UI
conflicts = scheduler.detect_conflicts()

if conflicts:
    st.warning("⚠️ Scheduling Conflicts Detected!")
    for c in conflicts:
        st.write(c)