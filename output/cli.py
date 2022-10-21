from turtle import color
from typing import List
from termcolor import colored
from rich.console import Console
from rich.table import Table


class Cli:
    def __init__(self) -> None:
        self.console = Console()
        self.table = Table(show_header=True, header_style="bold blue", show_lines=True)
        self.table.add_column("Test Case")
        self.table.add_column("Tool")
        self.table.add_column("Test Result", justify="right")
        self.table.add_column("Description")

    def print_table(self) -> None:
        self.console.print(self.table)

    def _pass_fail_result(self, test_result: bool) -> str:
        return (
            "[bold green]PASSED[/bold green]"
            if test_result
            else "[bold red]FAILED[/bold red]"
        )

    def add_table_rows(
        self, test_case: str, tool: str, test_result: bool, description: str
    ) -> None:
        result = self._pass_fail_result(test_result)
        self.table.add_row(test_case, tool, result, description)
