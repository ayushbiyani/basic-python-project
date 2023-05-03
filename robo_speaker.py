import os



if __name__ == '__main__' :
    print("Welecome to robospeaker created by ayush")
    while True :
        x = input("Enter what you want to say : ")
        if x == "robospeaker" :
            break
        command = f" PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"
        os.system(command)