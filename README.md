# prefetch
CLI tool that measures latency of cloud streaming speech-to-text APIs. It simulates a realtime audio stream and primitive speech command parsing to measure the amount of time required for an API to provide the client with enough responses to begin actual command processing like playing a song or ordering a burrito.

## Supported treaming speech-to-text API vendors
There are plans to eventually support latency measurements for all major STT vendors including Google Cloud, AWS, Azure.
