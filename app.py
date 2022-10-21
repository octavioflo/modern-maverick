import argparse
import logging
from typing import Dict, List
from attack_cases.attacks import open_directory_files, open_files, Attacks
from tools.tool_mapper import launch_attack
from output.cli import Cli
import sys


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
    parser.add_argument(
        "-v", "--version", help="Displays the version of Modern Maverick"
    )

    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    if args.file is not None and args.directory is not None:
        print("[!] Error, choose either a file or a directory.")
        sys.exit(0)
    if args.file is not None:
        report_content: Dict = open_files(args.file)
    if args.directory is not None:
        open_directory_files(args.directory)

    c = Cli()
    attack_content = list(report_content.values())
    attacks: List[Attacks] = [Attacks(**items) for items in attack_content]
    for attack in attacks:
        attack_output = launch_attack(attack.tool, attack.command, attack.output)
        c.add_table_rows(
            attack.title, attack.tool, attack_output.is_true, attack.description
        )
    c.print_table()


if __name__ == "__main__":
    main()
