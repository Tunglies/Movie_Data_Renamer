import os
import re
from pathlib import Path
from types import NoneType


DEBUG = True

SINGLE = [
    re.compile(i) for i in [
        "([A-Z]+-[0-9]+)",
        "[0-9]+-[0-9]+",

        "(?<=@)(.*)",
        "(?<=\])(.*)",

        "(.*)(?=-C)",
        "(.*)(?=\.)",

        "(?<=1H)(.*)",
        "(.*)(?=HHB)"
        "(?<=1)(.*)(?=HHB)",
        "([A-Z]+[\d]+)"
    ]
]

DOUBLE = [
    re.compile(i) for i in [
        "([A-Z]+)+([0-9]+)",
        "([A-Za-z]+)-0*([1-9]\d{2,})"
    ]
]

MEDIA_TYPES = (".mp4", ".mkv", ".wmv", ".avi")


def debug(*msg: str):
    if DEBUG:
        print(*msg)


def is_media_extension(extension: str) -> bool:
    return extension in MEDIA_TYPES


def format_file_name(name: str) -> str:
    temp = name.upper()
    debug(f"[ Input ] {temp}")
    for rule in SINGLE:
        search = rule.search(temp)
        if type(search) != NoneType:
            temp = search.group()
            debug(f"<<< Base >>> {temp}")
    debug(f"<<< SINGLE >>> {temp}")

    for rule in DOUBLE:
        search = rule.search(temp)
        if type(search) != NoneType:
            prefix, suffix = search.groups()
            temp = f"{prefix}-{suffix}"
    debug(f"<<< DOUBLE >>> {temp}")

    temp = temp.upper()
    debug(f"[ Output ] {temp}")
    return temp


class Media:
    def __init__(self, file_path: str):
        self.source_path: Path = Path(file_path).absolute()
        self.source_dir: Path = None
        self.source_name: str = None
        self.extension: str = None
        self.target_name: str = None
        self.target_dir: Path = None
        self.target_path: Path = None

    def source_check(self):
        if not self.source_path.is_file():
            self.source_path = None
        return self

    def extension_check(self):
        if self.source_path:
            self.source_dir = self.source_path.parent
            self.extension = self.source_path.suffix.lower()
        if not self.extension in MEDIA_TYPES:
            self.source_path = self.source_dir = self.extension = None
        return self

    def extract_file_name(self):
        if self.source_path:
            self.source_name = self.source_path.name.split(self.extension)[0]
        return self

    def format_file_name(self):
        if self.source_name:
            self.target_name = format_file_name(self.source_name)
            self.target_dir = self.source_dir
        return self

    def combine_target_path(self):
        if self.target_name:
            self.target_path = self.target_dir.joinpath(
                f"{self.target_name}{self.extension}")
        return self

    def rename_file(self):
        if not self.source_path != self.target_path:
            return self
        try:
            os.rename(self.source_path, self.target_path)
        except Exception as e:
            debug(e)


def run(file):
    (Media(file).source_check().extension_check().extract_file_name(
    ).format_file_name().combine_target_path().rename_file())


if __name__ == "__main__":
    for file in Path(root=__file__).glob("*.*"):
        run(file)