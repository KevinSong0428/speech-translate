import speech_recognition as sr
from googletrans import Translator
import pytesseract
import pyttsx3  # text to speech
from textblob import TextBlob
import googletrans

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

print(googletrans.LANGUAGES)

# initialize var
r = sr.Recognizer()
m = sr.Microphone()
engine = pyttsx3.init()

en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
kor_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0"
ch_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-HK_TRACY_11.0"
es_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male, 1 for female

engine.setProperty('rate', 125)  # changing rate to 150 (default is 200)


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
        lang = TextBlob(text)
        lang = lang.detect_language()
        result = translator.translate(text, src = lang)
        engine.setProperty('voice', en_voice_id)
        engine.say(result.text)
        engine.runAndWait()
        print(result.text)
    else:
        if (dst_lang == "korean" or dst_lang == "ko"):
            # wants to translate to korean
            result = translator.translate(text, dest = dst_lang)
            engine.setProperty('voice', kor_voice_id)
            engine.say(result.text)
            engine.runAndWait()
            print(result.text)
        elif (dst_lang == "spanish" or dst_lang == "es"):
            # wants to translate to spanish
            result = translator.translate(text, dest = dst_lang)
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


# only available for languages with 2 gender for voice
def change_voice():
    voice = engine.getProperty('voices')
    if engine.getProperty('voice') == voice[0].id:
        # changing voice to female
        engine.setProperty('voice', voice[1].id)
    else:
        # changing voice to male
        engine.setProperty('voice', voice[0].id)

# # default english
# engine.say("Hello")
# engine.runAndWait()
#
# # change_voice()
#
# # korean voice
# engine.setProperty('voice', kor_voice_id)
# engine.say("난 아주 많이 당신을 사랑합니다")
# engine.runAndWait()
#
# # chinese (cantonese) voice
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


# print(googletrans.LANGUAGES)

'''
result. ..src: 
The source language
dest: Destination language, which is set to English (en)
origin: Original text, that is 'Mitä sinä teet' in our example
text: Translated text, that will be 'what are you doing?' in our case
pronunciation: Pronunciation of the translated text
'''

# with m as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
#     audio = m # not audio data so there will be error
#     r.recognize_google(audio)
#     print(r.recognize_google(audio))
