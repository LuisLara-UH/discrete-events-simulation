from person import Female, Male
from random_variables_simulation import uniform
from variables_simulation import *
from sortedcontainers import SortedList
from event import Birth, BirthDay, Desease, Event

class Environment:
    def __init__(self, women_amount: int, men_amount: int, duration: int) -> None:
        self.poblation: list = []
        self.events: SortedList = SortedList(key= lambda x: x.date)
        self.actual_date = 0
        self.duration = duration
        self.initialize_poblation(women_amount, men_amount)
        self.initialize_events()

    def initialize_poblation(self, women_amount: int, men_amount: int):
        for _ in range(women_amount):
            self.poblation.append(Female(len(self.poblation), uniform(0, 100)))

        for _ in range(men_amount):
            self.poblation.append(Male(len(self.poblation), uniform(0, 100)))

    def initialize_events(self):
        for person in self.poblation:
            next_birthday: Event = BirthDay(uniform(0, 12), person) 
            self.events.add(next_birthday)

            desease: Desease = Desease((person.desease_age * 12) - person.actual_age, person)
            self.events.add(desease)

    def simulate(self):
        while self.events and self.actual_date <= self.duration:
            next_event = self.events.pop(0)
            self.actual_date = next_event.date
            chained_events = next_event.execute(self.poblation)
            next_event.print_event()

            for event in chained_events:
                self.events.add(event)