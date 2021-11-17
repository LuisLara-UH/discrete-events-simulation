from typing_extensions import Self


from events_simulation import desease_age

class Person:
    def __init__(self, male: bool) -> None:
        self.is_male: bool = male
        self.desease_age = desease_age(self.is_male)