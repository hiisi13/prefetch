from typing import List, NamedTuple


class VoiceCommand(NamedTuple):
    id: str
    wav: str
    regex: str
    match_alternatives: bool


class ScenarioLoader:
    def load_scenario(self, path: str) -> List[VoiceCommand]:
        pass