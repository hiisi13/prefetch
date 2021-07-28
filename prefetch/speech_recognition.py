import re
import time
from typing import Tuple

import numpy as np
import soundfile as sf

from prefetch.vendors.google.client import StreamingClient


current_time_ms = lambda: int(round(time.time() * 1000))


class SpeechRecognitionRunner:
    def __init__(self) -> None:
        self.closed = False

    def match_command(
        self, filename: str, pattern: str, language_code: str
    ) -> Tuple[str, int]:
        info = sf.info(filename)
        client = StreamingClient(info.samplerate, language_code)
        for transcript in client.recognize(
            self.generate_request_stream(filename, info.samplerate)
        ):
            match = re.match(pattern, transcript)
            if match:
                self.closed = True
                return transcript, current_time_ms() - self.command_end_ts
        return None, None

    def generate_request_stream(self, filename: str, samplerate: int):
        chunk_size = int(samplerate / 10)
        samples_per_ms = int(samplerate / 1000)

        try:
            pre_silence = np.random.choice(
                [*range(chunk_size, samples_per_ms * 2000 + 1, chunk_size)], 1
            )[0]
            pre_silence_sent = 0
            while pre_silence_sent <= pre_silence:
                yield np.zeros(chunk_size, dtype="int16").tobytes()
                pre_silence_sent += chunk_size
                time.sleep(0.1)

            with sf.SoundFile(filename, mode="r") as wav:
                while wav.tell() < wav.frames:
                    sound_for_recognition = wav.read(chunk_size, dtype="int16")

                    if sound_for_recognition.shape[0] < chunk_size:
                        last_chunk_size = sound_for_recognition.shape[0]
                        sound_for_recognition = np.concatenate(
                            (
                                sound_for_recognition,
                                np.zeros(
                                    chunk_size - sound_for_recognition.shape[0],
                                    dtype="int16",
                                ),
                            )
                        )
                        self.command_end_ts = (
                            current_time_ms()
                            - (chunk_size - last_chunk_size) / samples_per_ms
                        )
                    else:
                        self.command_end_ts = current_time_ms()

                    yield sound_for_recognition.tobytes()
                    time.sleep(0.1)

                while not self.closed:
                    yield np.zeros(chunk_size, dtype="int16").tobytes()
                    time.sleep(0.1)
        except Exception as e:
            print(e)
