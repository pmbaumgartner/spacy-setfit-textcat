import re
from pathlib import Path
from typing import Union

import spacy
import typer
from setfit import SetFitClassifier


def main(template: Path, input_cfg: Path):
    """input_cfg is second so that it can be passed through find -exec"""
    cfg = Path(input_cfg).read_text()
    template = Path(template).read_text()
    section_start, section_end = template.find("["), template.find("]") + 1
    section_str = template[section_start:section_end]
    section_str_re = re.escape(section_str)
    section_regex = re.compile(fr"({section_str_re}[\s\S]*?)\[.+\]")
    replaced_cfg = re.sub(section_regex, template, cfg)
    Path(input_cfg).write_text(replaced_cfg)


if __name__ == "__main__":
    typer.run(main)
