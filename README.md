# prefetch
CLI tool that measures latency of cloud streaming speech-to-text APIs. It simulates a realtime audio stream and primitive speech command parsing to measure the amount of time required for an API to provide the client with enough responses to begin actual command processing like playing a song or ordering a burrito.

## Supported treaming speech-to-text API vendors
There are plans to eventually support latency measurements for all major STT vendors including Google Cloud, AWS, Azure.

## Usage
Set location of your project credentials file to `GOOGLE_APPLICATION_CREDENTIALS` enrivonment variable. Then run `python cli.py`. Available options are:

```shell
  -i, --input TEXT          Audio WAV file
  -p, --pattern TEXT        Pattern to match the transcript against, string or a file path
  -l, --language_code TEXT  Language code, defaults to 'en-US'
```

Example command produced using speech synthesis is provided in the `sound` folder. Command to run the program would then look like this:

```shell
python cli.py -i sound/book-tickets-en.wav -p "book tickets from Seattle to Tokyo on June 7th"
```
