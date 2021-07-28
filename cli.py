import click
from prefetch.speech_recognition import SpeechRecognitionRunner


@click.command()
@click.option("--input", "-i", type=str, help="Audio WAV file")
@click.option(
    "--pattern",
    "-p",
    type=str,
    help="Pattern to match the transcript against, string or a file path",
)
@click.option(
    "--language_code",
    "-l",
    type=str,
    default="en-US",
    help="Language code, defaults to 'en-US'",
)
def prefetch(input: str, pattern: str, language_code: str):
    transcript, latency = SpeechRecognitionRunner().match_command(
        input, pattern, language_code
    )
    print(f"transcript={transcript} latency={latency}")


if __name__ == "__main__":
    prefetch()
