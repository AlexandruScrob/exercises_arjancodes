import logging

from iot_facade import IOTFacade


def power_speaker(on: bool, iot: IOTFacade) -> None:
    logging.info(f"Powering speaker: {on}.")
    iot.power_speaker(on)
    logging.info("Message sent to speaker.")


def get_status(iot: IOTFacade) -> str:
    logging.info("Display status for IOT devices.")
    status = iot.get_status()
    logging.info(f"Status: {status}")
    return status
