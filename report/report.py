"""This should define an ABC class that will determine the report types. 
The report types I'm expecting to create should be junit, json, and html. 

"""
from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def base_report():
        """Builds the skeletion of the report."""


class JSON(Report):
    def base_report():
        return {
            "version": "0.1.0",
            "time_created": "time_here",
            "attack_cases": [],
        }


class Junit(Report):
    def base_report():
        pass


class Html(Report):
    def base_report():
        pass
