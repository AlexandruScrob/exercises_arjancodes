from functools import partial
import logging
from iot.devices import SmartSpeakerDevice
from iot_controller import power_speaker, get_status

from iot.service import IOTService
from gui import SmartApp


def main():
    logging.basicConfig(level=logging.INFO)

    # create a IOT service
    service = IOTService()

    # create the smart speaker
    smart_speaker = SmartSpeakerDevice()
    speaker_id = service.register_device(smart_speaker)

    power_speaker_fn = partial(power_speaker, service=service, speaker_id=speaker_id)
    get_status_fn = partial(get_status, service=service)

    app = SmartApp(power_speaker_fn, get_status_fn)
    app.mainloop()


if __name__ == "__main__":
    main()
