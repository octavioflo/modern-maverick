from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def is_installed():
        """Determines whether a tool is installed."""

    @abstractmethod
    def version():
        """Determines what version of the tool is running."""

    @abstractmethod
    def run_tool():
        """Runs the tool from the installed path"""

    def validate_test():
        """Determines if the output is what the test case expected. Return a true or false based on the results."""


