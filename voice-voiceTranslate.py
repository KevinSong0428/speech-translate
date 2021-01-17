import speech_recognition as sr
from googletrans import Translator
import pyttsx3  # text to speech
import googletrans
import tkinter as tk

# initialize var
r = sr.Recognizer()
m = sr.Microphone()
engine = pyttsx3.init()


en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
kor_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0"
ch_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-HK_TRACY_11.0"
es_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. o for male, 1 for female
engine.setProperty('rate', 125)  # changing rate to 150 (default is 200)


def startConversion(lang, dst_lang):
    with m as source:
        audio = r.listen(source)
        text = r.recognize_google(audio, language = lang)
        print("INPUT: " + text)
    translator = Translator()
    if (dst_lang == "en-US"):
        # wants to translate to english
        engine.setProperty('voice', en_voice_id)
    else:
        if (dst_lang == "korean"):
            # wants to translate to korean
            engine.setProperty('voice', kor_voice_id)
        elif (dst_lang == "spanish"):
            # wants to translate to spanish
            engine.setProperty('voice', es_voice_id)
        elif (dst_lang == "chinese (traditional)"):
            # wants to translate to spanish
            engine.setProperty('voice', ch_voice_id)
    result = translator.translate(text, dest=dst_lang)
    engine.say(result.text)
    engine.runAndWait()
    print("OUTPUT: " + result.text)

# initialize GUI: Translator
gui = tk.Tk(className="Translator")
gui.geometry("400x300")

# language choices to pick from (available to translate to and from
LANGUAGE = ['English', '中文', '한국어', 'Español']

sourceLang = tk.StringVar(gui)
destLang = tk.StringVar(gui)

# # default value in drop down menu will be English
sourceLang.set(LANGUAGE[0])
destLang.set(LANGUAGE[0])

drop1 = tk.OptionMenu(gui, sourceLang, *LANGUAGE)
drop2 = tk.OptionMenu(gui, destLang, *LANGUAGE)

drop1.pack()
drop2.pack()

# https://cloud.google.com/speech-to-text/docs/languages <-- input langauge list
# print(googletrans.LANGUAGES) <-- output language list
# if want to add more langauges, find on both list, make list and download language on computer to get the voice ID
# for voice in voices:
#     print(" - ID: %s" % voice.id)

def checkLang(lang, var):
    # input, output language
    # audio and translator input is different so must a variable to distinguish
    if (lang == "English"):
        list1 = ["en-US", "English"]
        return list1[var]
    if (lang == "中文"):
        list1 = ["yue-Hant-HK", "chinese (traditional)"]
        return list1[var]
    if (lang == "한국어"):
        list1 = ["ko", "korean"]
        return list1[var]
    if (lang == "Español"):
        return "spanish"


def convert():
    global srcLang, dstLang
    # get dropdown selected as inputs
    srcLang = checkLang(sourceLang.get(), 0)
    dstLang = checkLang(destLang.get(), 1)
    startConversion(srcLang, dstLang)


startConvert = tk.Button(gui, text="Convert", padx=10, pady=5, fg="white", bg="#263D42",
                         command=convert)

startConvert.pack()

gui.mainloop()


'''
def startConversion(path='sample.wav', lang="en-US", dst_lang='en-US'):
    with sr.AudioFile(path) as source:
        print('Fetching File: ' + path)
        audio_text = r.record(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            # convert wav file to text in that language
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text, language=lang)
            print(text)

        except:
            print('Sorry.. run again...')

    translator = Translator()
    if (dst_lang == "en-US" or dst_lang == ''):
        # wants to translate to english
        result = translator.translate(text)
        engine.setProperty('voice', en_voice_id)
        engine.say(result.text)
        engine.runAndWait()
        print(result.text)
    else:
        if (dst_lang == "korean" or dst_lang == "ko"):
            # wants to translate to korean
            result = translator.translate(text, dest=dst_lang)
            engine.setProperty('voice', kor_voice_id)
            engine.say(result.text)
            engine.runAndWait()
            print(result.text)
        elif (dst_lang == "spanish" or dst_lang == "es"):
            # wants to translate to spanish
            result = translator.translate(text, dest=dst_lang)
            engine.setProperty('voice', es_voice_id)
            engine.say(result.text)
            engine.runAndWait()
            print(result.text)



def main():
    startConversion("KOR_001.wav", "ko-KR", '')
    print("\n")
    startConversion("KOR_002.wav", "ko-KR", '')
    print("\n")
    startConversion("BBN.wav", '', 'korean')
    print("\n")
    startConversion("KOR_001.wav", "ko-KR", 'spanish')


if __name__ == "__main__":
    main()
'''

# # default english
# engine.say("Hello")
# engine.runAndWait()
#
# # korean voice
# engine.setProperty('voice', kor_voice_id)
# engine.say("난 아주 많이 당신을 사랑합니다")
# engine.runAndWait()
#
# chinese (cantonese) voice
# engine.setProperty('voice', ch_voice_id)
# engine.say("我非常爱你")
# engine.runAndWait()

# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print(" - Rate: %s" % engine.getProperty('rate'))

# file = sr.AudioFile("BBN.wav")
# with file as source:
#     audio = r.record(source)
# print(r.recognize_google(audio))


# with m as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
#     audio = m # not audio data so there will be error
#     r.recognize_google(audio)
#     print(r.recognize_google(audio))
