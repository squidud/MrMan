import speech_recognition as sr

# Function to listen and transcribe speech
def listen_and_transcribe():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening... Press 'Q' to stop.")
        recognizer.adjust_for_ambient_noise(source)  # Adjusting for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        transcribed_text = recognizer.recognize_google(audio)
        return transcribed_text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Main function
def main():
    text = ""  # Initialize variable to store transcribed text
    listening = False  # Initialize listening flag

    while True:
        key = input("Press 'Enter' to start/stop listening, or 'Q' to quit: ").strip().upper()
        
        if key == "Q":
            break  # Exit the loop if 'Q' is pressed

        if not listening:
            listening = True
            text += listen_and_transcribe() + " "
            print("Speech to text conversion started...")
        else:
            listening = False
            print("Speech to text conversion stopped...")

    print("Final Transcribed Text:")
    print(text)

if __name__ == "__main__":
    main()
