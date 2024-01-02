from pathlib import Path

import json

from bs4 import BeautifulSoup
from functools import partial
from experiment import Experiment
from xml_adapter import get_from_bs


PATH: str = str(Path(__file__).parent)


def main() -> None:
    with open(f"{PATH}/config.xml", encoding="utf8") as file:
        config = file.read()

    bs = BeautifulSoup(config, "xml")
    get_from_bs_adapter = partial(get_from_bs, bs)
    experiment = Experiment(get_from_bs_adapter)
    experiment.run()


if __name__ == "__main__":
    main()
