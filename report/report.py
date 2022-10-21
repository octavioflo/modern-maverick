"""This should define an ABC class that will determine the report types. 
The report types I'm expecting to create should be junit, json, and html. 

"""
import datetime
import json


class JSON:
    def __init__(self, test_results: list[dict[str, str]], report_name: str) -> None:
        self.json_report = {
            "version": "0.1.0",
            "time_created": datetime.datetime.now().strftime("%Y-%m-%d:%H:%M:%S"),
            "tests": [],
        }
        for test_result in test_results:
            self.add_results(test_result)
        self.save_report(report_name)

    def add_results(self, test_result) -> None:
        self.json_report["tests"].append(test_result)

    def save_report(self, report_name: str) -> None:
        with open(report_name, "w") as f:
            f.write(json.dumps(self.json_report, indent=4))


class Junit:
    def __init__(self) -> None:
        pass


class Html:
    def __init__(self) -> None:
        pass
