from functools import partial
import logging

from iot_controller import power_speaker, get_status
from iot_facade import IOTFacade

from iot.service import IOTService
from gui import SmartApp


def main():
    logging.basicConfig(level=logging.INFO)

    # create a IOT service
    service = IOTService()

    # create the facade
    iot = IOTFacade(service)

    power_speaker_fn = partial(power_speaker, iot=iot)
    get_status_fn = partial(get_status, iot=iot)

    app = SmartApp(power_speaker_fn, get_status_fn)
    app.mainloop()


if __name__ == "__main__":
    main()
