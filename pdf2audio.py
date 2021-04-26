import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfFileReader(open('test1.pdf', 'rb'))
speaker = pyttsx3.init()
for num in range(pdfreader.numPages):
    text = pdfreader.getPage(num).extractText()
    speaker.say(Text)
    speaker.runAndWait()
speaker.stop()
