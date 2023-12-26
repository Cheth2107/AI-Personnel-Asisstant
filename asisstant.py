import os
import time
import google.cloud
import pyttsx3
import playsound
from gtts import gTTS
import openai
import pyaudio
import speech_recognition as sr

api_key = "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"
lang = 'en'

openai.api_key = api_key
guy = ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        said = recognizer.recognize_google(audio)
        print(said)
        return said
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Speech Recognition error; {e}")
    return ""

def google_speech_to_text(audio_content):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcriptions = []
    for result in response.results:
        transcriptions.append(result.alternatives[0].transcript)

    return ' '.join(transcriptions)

while True:
    user_input = get_audio()

    if "Friday" in user_input:
        words = user_input.split()
        new_string = ' '.join(words[1:])
        print(new_string)

        # Assuming you have the audio content available in some variable (e.g., audio_content)
        # You would need to replace 'audio_content' with the actual audio content
        audio_content = ...  # Provide the actual audio content

        transcribed_text = google_speech_to_text(audio_content)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": transcribed_text}]
        )
        text = completion.choices[0].message['content']
        speak(text)

    if "stop" in user_input:
        break
