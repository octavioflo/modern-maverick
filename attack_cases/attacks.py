from pydantic import BaseModel
from typing import Any, List
import yaml


def open_files(files: str) -> dict:
    with open(files) as f:
        return yaml.safe_load(f)


def open_directory_files(path: str):
    # files = [f for f in listdir(path) if isfile(join(path, f))]
    # for file in files:
    #     open_files(f"{path}/{file}")
    open_files(f"{path}/*.yml")


class Attacks(BaseModel):
    title: str
    description: str
    tool: str
    variables: Any
    command: List[str]
    output: str
