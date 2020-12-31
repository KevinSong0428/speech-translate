from googletrans import Translator
import cv2
import pytesseract
from mss import mss
from PIL import Image
import numpy as np
from langdetect import detect
from cdifflib import CSequenceMatcher

#pytesseract code

# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

# https://askubuntu.com/questions/793634/how-do-i-install-a-new-language-pack-for-tesseract-on-16-04
# custom_config = r'-l eng + kor + chi-sim + chi-tra --psm 6'
# page segmentation modes:
'''
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.
'''
# custom_config = r'-l kor + eng --psm 5'


# print(pytesseract.get_languages(config=''))

# print(googletrans.LANGUAGES)

# certain monitor size
# mon = {'top': 100, 'left': -960, 'width': 960, 'height': 775}
# img = mss().grab(mon)
# img = Image.frombytes('RGB', (img.width, img.height), img.rgb)

# temporary --> just use PNG file as img
# img = cv2.imread("TTN.JPG")
# img = cv2.imread("ttn1.PNG")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cv2.imshow("result", np.array(img))
# cv2.imshow("result", img)
# cv2.waitKey(0)

# print(pytesseract.image_to_string(img))

# text = pytesseract.image_to_string(img, config = custom_config)
# complete = ''
# acc = ''
# for i in range(len(text)):
#     if (text[i] != '\n'):
#         if (text[i] != ' ' ):
#             acc += text[i]
#     else:
#         complete += acc + '\n'
#         # print(acc)
#         acc = ''
#
# print(complete)


# text input code --> audio to text --> translated text

file = open("lyrics.txt", encoding="utf8")
lines = file.readlines()
for line in lines:
    print(line)
print('\n')
for line in lines:
    translator = Translator()
    result = translator.translate(line)
    print(result.text)


# translated = "이밤그날의반딧불을\n당신의창가까이보낼게요\n음사랑한다는말이에요"
# print(translator.translate(translated).text)

# ratio = CSequenceMatcher(None, translated, text).ratio()
# print(ratio)
# translated = text.translate(text)
# print(translated)

# box = pytesseract.image_to_data(img, lang='kor')
# for x, b in enumerate(box.splitlines()):
#     b = b.split()[-1]
#     print(b)
#     lang = detect(b)
#     print(lang)
#     if (lang == 'ko'):
#         print(b)

# text = text.translate(text)
# print(text)

# lang = detect('사랑')

# if (lang == 'ko'): # ko == korean
#     print("HI")

# translator = Translator()
# result = translator.translate(text)
# print(result.text)

'''
result. ..src: 
The source language
dest: Destination language, which is set to English (en)
origin: Original text, that is 'Mitä sinä teet' in our example
text: Translated text, that will be 'what are you doing?' in our case
pronunciation: Pronunciation of the translated text
'''

# goal: have translation over the word (if not over then on top of the word)