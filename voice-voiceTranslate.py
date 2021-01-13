import speech_recognition as sr
from googletrans import Translator
import pytesseract
import pyttsx3  # text to speech
from textblob import TextBlob
import googletrans

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# prints all languages to translate to and from
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

'''
with m as source:
    audio = r.listen(source)
# https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134
    # cantonese
    # print(r.recognize_google(audio, language = 'yue-Hant-HK')) https://cloud.google.com/speech-to-text/docs/languages
    # print(r.recognize_google(audio, language = 'zh-yue')) https://www.science.co.il/language/Locale-codes.php
    # korean
    # print(r.recognize_google(audio, language = 'ko'))
'''


# noinspection PyRedundantParentheses
def startConversion(lang="en-US", dst_lang='en-US'):
    with m as source:
        audio = r.listen(source)
        text = r.recognize_google(audio, language=lang)
        print(text)

    translator = Translator()
    if (dst_lang == "en-US" or dst_lang == ''):
        # wants to translate to english
        lang = TextBlob(text)
        lang = lang.detect_language()
        result = translator.translate(text, src=lang)
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
        elif (dst_lang == 'chinese (traditional)' or dst_lang == 'zh-tw'):
            # wants to translate to spanish
            result = translator.translate(text, dest=dst_lang)
            engine.setProperty('voice', ch_voice_id)
            engine.say(result.text)
            engine.runAndWait()
            print(result.text)


def main():
    language = input("What language do you speak? ")
    translate = input("What language do you want to translate to? ")
    english = {'english', 'en', 'eng', 'English', 'Eng'}
    korean = {'korean', 'ko', 'Korean', 'kor'}
    cantonese = {'canto', 'cantonese', 'Cantonese', 'zh-tw', 'chinese (traditional)', 'chinese'}
    spanish = {'spanish', 'Spanish', 'espanol', 'Espanol'}
    if (language in english):
        language = 'en-US'
    elif (language in korean):
        language = 'ko'
    elif (language in cantonese):
        language = 'yue-Hant-HK'
    elif (language in spanish):
        language = 'spanish'
    if (translate in english):
        translate = 'en-US'
    elif (translate in korean):
        translate = 'korean'
    elif (translate in cantonese):
        translate = 'chinese (traditional)'
    elif (translate in spanish):
        translate = 'spanish'
    print('lang: ' + language + ' trans: ' + translate + '\n')
    startConversion(language, translate)


if __name__ == "__main__":
    main()



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
        lang = TextBlob(text)
        lang = lang.detect_language()
        result = translator.translate(text, src=lang)
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
