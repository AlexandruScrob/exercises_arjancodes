import logging
from pathlib import Path

log_path = Path(__file__).parent.resolve()


def main() -> None:
    # logging.basicConfig(level=logging.INFO)

    # with formatting
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        # to filename
        filename=f"{log_path}/basic.log",
    )

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")


if __name__ == "__main__":
    main()
