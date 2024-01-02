from pathlib import Path

from bs4 import BeautifulSoup
from experiment import Experiment
from xml_adapter import XMLConfig


PATH: str = str(Path(__file__).parent)


def main() -> None:
    with open(f"{PATH}/config.xml", encoding="utf8") as file:
        config = file.read()

    bs = BeautifulSoup(config, "xml")
    adapter = XMLConfig(bs)
    experiment = Experiment(adapter)
    experiment.run()


if __name__ == "__main__":
    main()
