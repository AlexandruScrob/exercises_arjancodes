"""
Basic video exporting example
"""

from dataclasses import dataclass
import pathlib
from typing import Protocol, Type


# used protocol to simplify inheritance for the exporters
# simple clean way to create the exporters we need in the factory using dataclasses
# cons: uses more memory than tuples


class VideoExporter(Protocol):
    """Basic representation of video exporting codec."""

    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter:
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter:
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter:
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(Protocol):
    """Basic representation of audio exporting codec."""

    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter:
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter:
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


@dataclass
class MediaExporter:
    video: VideoExporter
    audio: AudioExporter


# TODO good use of __call__
@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audio_class: Type[AudioExporter]

    def __call__(self) -> MediaExporter:
        return MediaExporter(video=self.video_class(), audio=self.audio_class())


FACTORIES = {
    "low": MediaExporterFactory(H264BPVideoExporter, AACAudioExporter),
    "high": MediaExporterFactory(H264Hi422PVideoExporter, AACAudioExporter),
    "master": MediaExporterFactory(LosslessVideoExporter, WAVAudioExporter),
}


def read_exporter() -> MediaExporterFactory:
    """Constructs an exporter factory based on the user's preference."""

    # read the desired export quality
    while True:
        export_quality = input(
            f"Enter desired output quality ({', '.join(FACTORIES)}): "
        )

        try:
            return FACTORIES[export_quality]
        except KeyError:
            print(f"Unkown output quality option: {export_quality}.")


def do_export(exporter: MediaExporter) -> None:
    """Main function."""

    # prepare the export
    exporter.video.prepare_export("placeholder_for_video_data")
    exporter.audio.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    exporter.video.do_export(folder)
    exporter.audio.do_export(folder)


if __name__ == "__main__":
    # create the factory
    factory = read_exporter()

    # use the factory to create the media exporter
    media_exporter = factory()

    # perform the exporting job
    do_export(media_exporter)
