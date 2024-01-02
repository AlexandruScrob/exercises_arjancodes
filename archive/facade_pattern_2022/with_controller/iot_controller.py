import logging
from iot.service import IOTService
from network.connection import Connection
from message.helper import Message as Msg


def power_speaker(on: bool, service: IOTService, speaker_id: str) -> None:
    msg = "switch_on" if on else "switch_off"

    logging.info(f"Sending message to speaker {speaker_id}: {on}.")

    # create a connection to the smart speaker
    speaker_ip, speaker_port = service.get_device(speaker_id).connection_info()
    speaker_connection = Connection(speaker_ip, speaker_port)

    # construct a message
    message = Msg("SERVER", speaker_id, msg)

    # send the message
    speaker_connection.connect()
    speaker_connection.send(message.b64)
    speaker_connection.disconnect()

    logging.info(f"Message sent to speaker: {msg}.")


def get_status(service: IOTService) -> str:
    logging.info("Display status for IOT devices.")
    status = "".join(
        f"{device_id}: {device.status_update()}"
        for device_id, device in service.devices().items()
    )

    logging.info(f"Status: {status}")
    return status
