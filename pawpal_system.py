from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


@dataclass


@dataclass
class Task:
    title: str
    time: datetime
    priority: int
    completed: bool = False
    frequency: str = None  # "daily", "weekly", or None

    def mark_complete(self):
        """Mark task complete and generate next occurrence if recurring."""
        self.completed = True

        if self.frequency == "daily":
            return Task(
                self.title,
                self.time + timedelta(days=1),
                self.priority,
                frequency="daily"
            )

        if self.frequency == "weekly":
            return Task(
                self.title,
                self.time + timedelta(days=7),
                self.priority,
                frequency="weekly"
            )

        return None


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self):
        return self.owner.get_all_tasks()

    def sort_tasks(self):
        tasks = self.get_all_tasks()
        return sorted(tasks, key=lambda t: (t.time.strftime("%Y-%m-%d %H:%M"), -t.priority))

    def get_today_tasks(self):
        today = datetime.now().date()
        return [t for t in self.get_all_tasks() if t.time.date() == today]
    
    def detect_conflicts(self):
         """Detect tasks scheduled at the same time."""
         tasks = self.sort_tasks()
         conflicts = set()

         for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                 if tasks[i].time == tasks[j].time:
                    pair = tuple(sorted([tasks[i].title, tasks[j].title]))
                    conflicts.add(
                        f"⚠️ Conflict: {pair[0]} and {pair[1]} at {tasks[i].time.strftime('%H:%M')}"
                )

         return list(conflicts)
    
class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        return self.owner.get_all_tasks()

    def sort_tasks(self):
        return sorted(self.get_all_tasks(), key=lambda t: (-t.priority, t.time))

    def get_today_tasks(self):
        today = datetime.now().date()
        return [t for t in self.get_all_tasks() if t.time.date() == today]

    def filter_tasks(self, completed=None, pet_name=None):
        """Filter tasks by completion status or pet name."""
        tasks = self.get_all_tasks()

        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]

        if pet_name:
            tasks = [
                t for pet in self.owner.pets if pet.name == pet_name
                for t in pet.tasks
            ]

        return tasks

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time."""
        tasks = self.sort_tasks()
        conflicts = set()

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                if tasks[i].time == tasks[j].time:
                    pair = tuple(sorted([tasks[i].title, tasks[j].title]))
                    conflicts.add(
                        f"⚠️ Conflict: {pair[0]} and {pair[1]} at {tasks[i].time.strftime('%H:%M')}"
                    )

        return list(conflicts)