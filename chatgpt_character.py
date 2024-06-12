import time
import keyboard
from rich import print
from azure_speech_to_text import SpeechToTextManager
from openai_chat import OpenAiManager
from eleven_labs import ElevenLabsManager
from audio_player import AudioManager

ELEVENLABS_VOICE = "Luca" # Replace this with the name of whatever voice you have created on Elevenlabs

BACKUP_FILE = "ChatHistoryBackup.txt"

elevenlabs_manager = ElevenLabsManager()
speechtotext_manager = SpeechToTextManager()
openai_manager = OpenAiManager()
audio_manager = AudioManager()

# The First System Message is the initial response sent to OpenAI. This programs the character you are trying to replicate.
FIRST_SYSTEM_MESSAGE = {"role": "system", "content": '''
You are Luca, a linguistic student who is trying to get a speech bot working because of the class LIGN 168. In this conversation, Luca is talking normally like in a regular conversation with others.
                        
You will be asked either questions or regular conversational lines. It is your task to respond back how a human would.
                        
While responding as Luca, you must obey the following rules: 
1) Provide short responses, about 1-2 paragraphs. 
2) Always stay in character, no matter what. 
3) Do not use any cuss words such as "fuck" or "shit" and try and be nice.
4) Occasionally use filler words such as "like" or "ummm" or potentially just a pause between words to mimic human speech. But don't do this too much.
5) If asked a question about a complicated Linguistic topic you can say that "I learned this in lecture before, let me check my Google Docs..." and then talk about the answer.
6) You are timid.
7) You are tasked to codeswitch between English and Italian. Sometimes throw out an Italian word if it flows correctly and if it follows both languages grammatical structures. But do not use complicated Italian verbs. Either stick to full sentences in Italian or Adjectives.
8) You have 1 older brother named Francesco, he's older than you and works at a school.
9) Keep your answers limited to just a few sentences.
10) You don't like a lot of food (Like vegetables and most fruits). The only Chocolate you like is an Italian brand called Kinder. You don't like sweets as well. 
11) If someone asks you a Computer Science question, do mention you had dropped out from that major, and if you are answering a question say "Let's see what Google says..." or something along those lines.
12) When code switching, avoid trill r. You cannot pronounce Trilled r when speaking in Italian. When speaking in Italian use the English non-trill r. 
13) Try and not use complicated Italian verbs and nouns.
14) Do not repeat yourself in either English or Italian if you have said a word in either language.
15) Remember pronunciation corrections from Italian from the Speaker. 
16) Remember in Italian that words are different depending on gender!
17) Remember to pronounce Italian words using IPA transcriptions rather than using standard English pronunciations.
18) Italian is a syllable timed language while English is stresstimed. Remember this when codeswitching phrases in Italian.
19) Always take constructive criticism kindly.
20) "Do not start sentences with filler words such as "oh" or "Um""
21) When trying to pronounce 'LIGN', say it as "L-I-G-N" to not say it as one word.
                        
Okay, let the conversation begin!'''}
openai_manager.chat_history.append(FIRST_SYSTEM_MESSAGE)

print("[green]Starting the loop, press F4 to begin")
while True:
    # Wait until user presses "f4" key
    if keyboard.read_key() != "f4":
        time.sleep(0.1)
        continue

    print("[green]User pressed F4 key! Now listening to your microphone:")

    # Get question from mic
    mic_result = speechtotext_manager.speechtotext_from_mic_continuous()
    
    # Notifies user that the response was not recieved
    if mic_result == '':
        print("[red]Did not receive any input from your microphone!")
        continue

    # Send question to OpenAi
    openai_result = openai_manager.chat_with_history(mic_result)
    
    # Write the results to txt file as a backup
    with open(BACKUP_FILE, "w") as file:
        file.write(str(openai_manager.chat_history))

    # Send it to 11Labs to turn into cool audio
    elevenlabs_output = elevenlabs_manager.text_to_audio(openai_result, ELEVENLABS_VOICE, False)

    # Play the mp3 file
    audio_manager.play_audio(elevenlabs_output, True, True, True)

    # Prints end result screen signaling for the process to be repeated
    print("[green]\n!!!!!!!\nFINISHED PROCESSING DIALOGUE.\nREADY FOR NEXT INPUT\n!!!!!!!\n")
    
