from typing import List
import click
from scenario import ScenarioLoader, VoiceCommand
from speech_recognition import SpeechRecognitionRunner


@click.command()
@click.option('--scenario', '-s', type=str)
def prefetch(scenario):
    commands: List[VoiceCommand] = ScenarioLoader().load_scenario(scenario)
    summary = SpeechRecognitionRunner().run_scenario(commands)

    # print summary


if __name__ == '__main__':
    prefetch()