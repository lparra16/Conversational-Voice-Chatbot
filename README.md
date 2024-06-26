# Conversational-Voice-Chatbot
Simple app that lets you have a verbal conversation with OpenAi's GPT 4. (Now works with GPT-4o and what was used for Luca Parra)
Written by DougDoug. Minor additions were added by Luca Parra. Original README written by DougDoug and updated by Luca Parra.
Original file is named Babagaboosh and the original GitHub is here: https://github.com/DougDougGithub/Babagaboosh

## SETUP:
1) This was written in Python 3.9.2. Install page here: https://www.python.org/downloads/release/python-392/

2) Run `pip install -r requirements.txt` to install all modules.

3) This uses the Microsoft Azure TTS, Elevenlabs, and OpenAi services. You'll need to set up an account with these services and generate an API key from them. Then add these keys as windows environment variables named AZURE_TTS_KEY, AZURE_TTS_REGION, ELEVENLABS_API_KEY, and OPENAI_API_KEY respectively.

4) This app originally used the GPT-4 model from OpenAi (Though with updates the GPT-4o model works (gpt-4-0613 being a turbo model)). As of this writing (June 12 2024), you need to pay $10 (Previously $1) to OpenAi in order to get access to the GPT-4o model API. So after setting up your account with OpenAi, you will need to pay for at least $1 in credits so that your account is given the permission to use the GPT-4o model when running my app. See here: https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4

5) Elevenlabs is the service used for Ai voices. Once you've made an Ai voice on the Elevenlabs website, open up chatgpt_character.py and replace the ELEVENLABS_VOICE variable with the name of your Ai voice.

## Using the App

1) Run `chatgpt_character.py'

2) Once it's running, press F4 to start the conversation, and Azure Speech-to-text will listen to your microphone and transcribe it into text.

3) Once you're done talking, press P. Then the code will send all of the recorded text to the Ai. Note that you should wait a second or two after you're done talking before pressing P so that Azure has enough time to process all of the audio.

4) Wait a few seconds for OpenAi to generate a response and for Elevenlabs to turn that response into audio. Once it's done playing the response, you can press F4 to start the loop again and continue the conversation.
