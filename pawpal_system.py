from dataclasses import dataclass
from datetime import datetime


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        pass


@dataclass
class Task:
    title: str
    time: datetime
    priority: int
    completed: bool = False


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = None


class Scheduler:
    def __init__(self):
        self.tasks = []