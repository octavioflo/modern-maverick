from tools.nmap import Nmap
from tools.commandline import CommandLine
from typing import List


def launch_attack(tool: str, commands: List[str], output: str):
    tools_dict = {"nmap": Nmap(commands, output), "generic": CommandLine()}
    return tools_dict[tool]
