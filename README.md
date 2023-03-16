# Transcribe multiple MP3 files to text

This is a simple script that transcribes multiple MP3 files to text using the OpenAI Whisper API.

This script uses the large-v2 OpenAI model. The large-v2 model is a 1.5B parameter model that is trained on a variety of text datasets, including Wikipedia, Reddit, and Common Crawl. It is the largest model OpenAI has released to date.

You need to have an OpenAI API key to use this script. You can get one here: https://platform.openai.com/account/api-keys. After you have a key, save it to your local drive in a JSON file named `keys.json`. 

Example JSON key file:

`{"openai_api_key": "YOUR_API_KEY"}`

Save the JSON file to `C:/tmp/keys.json`, or modify the script if you prefer a different location.

**Note**: OpenAI Whisper has a 25Mb limitation for the file size. If your mp3 file is larger than 25Mb, you will need to split the file into smaller files. This is the main reason the script expects multiple mp3 files.

OpenAI Whisper is not a free service, however, it is very affordable. You can find the pricing here: https://openai.com/pricing/.

As an example, I transcribed an hour of audio for about $0.35 USD.

Why use OpenAI Whisper, instead of other transcription services?
Yes, there are many other transcription services available and many are free or already included in other subscription services you have, for example Microsoft 365 apps. However, the OpenAI Whisper service is very accurate and is very affordable. I find that the transcription is more accurate than other services, and the cost is very reasonable and worth the additional cost for the accuracy it provides.

## Requirements

1. Python 3.6 or higher
2. Windows OS (I haven't tested it on other OS's)
3. OpenAI API key 
4. MP3 files to transcribe

## Usage

1. Install the OpenAI Python package:

    `pip install openai`

2. Copy the script into your environment, including the `tape.sm.png` file.

3. Run the script

4. Follow the instructions in the GUI

Screenshot of the GUI:

![Screenshot of the GUI](https://github.com/HaroldMitts/transcriber/blob/main/Screenshot.png)