from google.cloud import speech


class StreamingClient:
    def __init__(self, sample_rate: int, language_code: str) -> None:
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,
            language_code=language_code,
            model="command_and_search",
        )
        self.streaming_config = speech.StreamingRecognitionConfig(
            config=config, interim_results=True, single_utterance=True
        )
        self.client = speech.SpeechClient()

    def recognize(self, audio_generator):
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )
        responses = self.client.streaming_recognize(self.streaming_config, requests)
        for t in self.listen_print_loop(responses):
            yield t

    def listen_print_loop(self, responses):
        for response in responses:
            if not response.results:
                continue

            result = response.results[0]
            if not result.alternatives:
                continue

            yield result.alternatives[0].transcript
