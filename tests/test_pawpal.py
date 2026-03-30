from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion():
    task = Task("Feed", datetime.now(), 1)
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Max", "Dog")
    task = Task("Walk", datetime.now(), 1)

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sorting_tasks():
    owner = Owner("Amine")
    pet = Pet("Max", "Dog")
    owner.add_pet(pet)

    t1 = Task("Low Priority", datetime.now(), 1)
    t2 = Task("High Priority", datetime.now(), 3)

    pet.add_task(t1)
    pet.add_task(t2)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_tasks()

    assert sorted_tasks[0].priority >= sorted_tasks[1].priority


def test_recurring_task_creation():
    task = Task("Daily Feeding", datetime.now(), 2, frequency="daily")

    new_task = task.mark_complete()

    assert new_task is not None
    assert new_task.time.date() == (task.time + timedelta(days=1)).date()


def test_conflict_detection():
    owner = Owner("Amine")
    pet = Pet("Max", "Dog")
    owner.add_pet(pet)

    same_time = datetime.now().replace(second=0, microsecond=0)

    t1 = Task("Task1", same_time, 1)
    t2 = Task("Task2", same_time, 2)

    pet.add_task(t1)
    pet.add_task(t2)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) > 0