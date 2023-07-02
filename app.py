import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Transcribing...")
        transcription = r.recognize_google(audio, language="en")  # Change the language as needed
        print("Transcription:", transcription)
        return transcription
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from the speech recognition service:", str(e))

# Test the live speech-to-text conversion
transcribe_speech()
