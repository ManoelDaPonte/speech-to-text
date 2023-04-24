import azure.cognitiveservices.speech as speechsdk
import os
import sys

def set_speech_service():
    # Set up the Speech service client object
    speech_key = os.environ['AZURE_SPEECH_TOKEN']
    service_region = "westeurope"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "fr-FR" # set the language to French
    speech_timeout = speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs
    speech_config.set_property(speech_timeout, "10000")
    speech_config.set_profanity(speechsdk.ProfanityOption.Raw) # disable profanity filtering
    return speech_config

def exec_speech_service(speech_config, audio_file):
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_recognizer.recognize_once()
    return result

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python script.py audio_file")
        sys.exit(1)

    audio_file = sys.argv[1]

    if not os.path.isfile(audio_file):
        print(f"Error: {audio_file} is not a valid file")
        sys.exit(1)
    
    result = exec_speech_service(set_speech_service(), audio_file)
    print(result.text)