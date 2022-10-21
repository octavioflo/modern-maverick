# import nmap
import logging
import subprocess
from tools.tool import Tool
from typing import List


class NmapException(Exception):
    pass


class Nmap(Tool):
    def __init__(self, commands, output) -> None:
        self.commands = commands
        self.output = output
        # check if the tool is installed. if installed then execute the rest of the commands.
        if self.is_installed():
            self.version()
            self.command_outputs = self.run_tool()
            self.is_true = self.validate_test(self.command_outputs)

    def is_installed(self):
        """Determines whether a tool is installed.
        If not installed, will try and install the tool."""
        return True

    def version(self):
        """Determines what version of the tool is running."""
        return subprocess.Popen(
            ["nmap", "--version"], stdout=subprocess.PIPE
        ).stdout.read()

    def run_tool(self):
        """Runs the tool from the installed path"""
        return [
            str(subprocess.Popen(command.split(), stdout=subprocess.PIPE).stdout.read())
            for command in self.commands
        ]

    def validate_test(self, command_outputs: List[str]):
        return any(self.output in co for co in command_outputs)
