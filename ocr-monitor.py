import cv2
import pytesseract
import webbrowser
from mss import mss
from PIL import Image
import numpy as np

# ctrl left click pytesseract to see functions of pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

# Monitor window size
# mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
# personal custom monitor window size looking for website
mon = {'top': 100, 'left': -675, 'width': 275, 'height': 830}

found = False

while not found:
    img = mss().grab(mon)
    img = Image.frombytes('RGB', (img.width, img.height), img.rgb)
    cv2.imshow("Result", np.array(img))
# level    page_num    block_num    par_num    line_num    word_num    left    top_width    height    conf    text
    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()[-1]
            if ('playstation.com' in b):
                webbrowser.open('https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816')
                found = True
    cv2.waitKey(1)

'''

# use cv2 image read to get test image
img = cv2.imread('test.jpg')

# have to convert RGB to BGR values
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# will print any text out
print(pytesseract.image_to_string(img))


# splits apart the image into text
# level    page_num    block_num    par_num    line_num    word_num    left    top_width    height    conf    text
boxes = pytesseract.image_to_data(img)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if ('Kevin' in b[-1]):
            webbrowser.open('https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816')

# open img window called 'Result'
cv2.imshow("Result", img)

# delay infinity
cv2.waitKey(0)

'''