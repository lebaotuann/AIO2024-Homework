# Section 1, Q2
from abc import ABC, abstractmethod


class Ward:
    """This class stores ward information."""

    def __init__(self, name: str):
        self.__name = name
        self.__people = []

    def add_person(self, person):
        """Add a person into a ward.

        Args:
            person (): A person.
        """
        self.__people.append(person)

    def describe(self):
        """Print ward information."""
        print(f"Ward Name: {self.__name}")
        for person in self.__people:
            person.describe()

    def count_doctor(self):
        """Count the number of doctors in the ward.

        Returns:
            int: The number of doctors in the ward
        """
        count = 0
        for p in self.__people:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_age(self):
        """Sort people by increasing age."""
        self.__people.sort(key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        """Calculate the average year of birth of teachers.

        Returns:
            int: The average year.
        """
        count = 0
        average = 0
        for p in self.__people:
            if isinstance(p, Teacher):
                average += p.yob
                count += 1
        return average / count


class Person(ABC):
    """This class stores person information."""

    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob  # year of birthday

    @property
    def yob(self):
        """Year of the birthday"""
        return self._yob

    @abstractmethod
    def describe(self):
        """Print person information."""


class Student(Person):
    """This class stores student information."""

    def __init__(self, name: str, yob: int, grade: str):
        self._grade = grade
        super().__init__(name, yob)

    def describe(self):
        """Print student information."""
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    """This class stores teacher information."""

    def __init__(self, name: str, yob: int, subject: str):
        self._subject = subject
        super().__init__(name, yob)

    def describe(self):
        """Print teacher information."""
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}"
        )


class Doctor(Person):
    """This class stores doctor information."""

    def __init__(self, name: str, yob: int, specialist: str):
        self._specialist = specialist
        super().__init__(name, yob)

    def describe(self):
        """Print doctor information."""
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}"
        )
