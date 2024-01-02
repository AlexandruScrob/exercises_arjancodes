from pathlib import Path

from bs4 import BeautifulSoup
from experiment import Experiment
from xml_adapter import XMLConfig


PATH: str = str(Path(__file__).parent)


def main() -> None:
    with open(f"{PATH}/config.xml", encoding="utf8") as file:
        config = file.read()

    # we're basically overriding the original BeautifulSoup get and it may lead
    # to unexcpected behavious
    # NOTE: not recommended with class based adapter
    # bs = BeautifulSoup(config, "xml")
    # bs.get ...
    adapter = XMLConfig(config, "xml")
    experiment = Experiment(adapter)
    experiment.run()


if __name__ == "__main__":
    main()
