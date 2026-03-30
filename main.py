from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


# Create owner
owner = Owner("Amine")

# Create pets
dog = Pet("Max", "Dog")
cat = Pet("Luna", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks

same_time = datetime.now().replace(second=0, microsecond=0)

task1 = Task("Feed Max", same_time, 2)
task2 = Task("Walk Max", same_time, 1)
task3 = Task("Feed Luna", same_time, 3)

dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)

# Create scheduler
scheduler = Scheduler(owner)

# Print schedule
print("\n🐾 Today's Schedule:\n")

for task in scheduler.sort_tasks():
    status = "✅ Done" if task.completed else "⏳ Pending"
    print(f"• {task.title} at {task.time.strftime('%I:%M %p')} (Priority {task.priority}) - {status}")
# -------------------------
# 🔍 Test Filtering
# -------------------------
print("\n✅ Pending Tasks:")

pending = scheduler.filter_tasks(completed=False)

if pending:
    for t in pending:
        print(f"• {t.title} - Pending")
else:
    print("No pending tasks")

# -------------------------
# 🔁 Test Recurring Task
# -------------------------
print("\n🔁 Testing Recurring Task:")

recurring_task = Task("Daily Feeding", datetime.now(), 2, frequency="daily")
dog.add_task(recurring_task)

new_task = recurring_task.mark_complete()
if new_task:
    dog.add_task(new_task)
    print(f"New recurring task created for: {new_task.time}")

# -------------------------
# ⚠️ Test Conflict Detection
# -------------------------
print("\n⚠️ Conflict Check:")

conflicts = scheduler.detect_conflicts()
for c in conflicts:
    print(c)  

print("\n✅ Pending Tasks:")
pending = scheduler.filter_tasks(completed=False)

if pending:
    for t in pending:
        print(f"• {t.title} - Pending")
else:
    print("No pending tasks found")    