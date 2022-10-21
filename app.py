import argparse
import logging
from typing import List
from attack_cases.attacks import open_directory_files, open_files, Attacks
from tools.tool_mapper import launch_attack
from output.cli import Cli
from report.report import JSON
import sys

# import pkg_resources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default=None,
        help="File location of the attack scenario report.",
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default=None,
        help="Directory location where the attack scenarios reports are stored.",
    )
    parser.add_argument(
        "-dd",
        "--debug",
        action="store_true",
        help="Turns on debug mode for more detailed information.",
    )
    # parser.add_argument(
    #     "--version",
    #     action="version",
    #     version=f'{pkg_resources.get_distribution("modern-maverick").version}',
    # )
    parser.add_argument(
        "--report_name",
        type=str,
        default="report.json",
        help="Choose what you would like to name the report.",
    )
    parser.add_argument(
        "-r",
        "--report",
        help="Choose the report format. JSON, JUnit, HTML",
    )

    args = parser.parse_args()
    # if args.version:
    #     print(pkg_resources.get_distribution("modern-maverick").version)
    #     sys.exit(0)
    if args.debug:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    if args.file is not None and args.directory is not None:
        print("[!] Error, choose either a file or a directory.")
        sys.exit(0)
    if args.file is not None:
        report_content: dict = open_files(args.file)
    if args.directory is not None:
        open_directory_files(args.directory)

    c = Cli()
    report_details = []
    attack_content = list(report_content.values())
    attacks: List[Attacks] = [Attacks(**items) for items in attack_content]
    for attack in attacks:
        attack_output = launch_attack(attack.tool, attack.command, attack.output)
        c.add_table_rows(
            attack.title, attack.tool, attack_output.is_true, attack.description
        )
        report_details.append(
            {
                "test_case": attack.title,
                "tool": attack.tool,
                "result": "passed" if attack_output.is_true else "failed",
                "description": attack.description,
            }
        )
    c.print_table()

    if args.report is None:
        JSON(report_details, args.report_name)


if __name__ == "__main__":
    main()
