import pyttsx3
import PyPDF2
book = open('c:/Users/Dell/Desktop/NLP-Text to Speech/Audio_book/file.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(book)

num_pages = pdf_reader.numPages
print(num_pages)
pageObj = pdf_reader.getPage(0)
print(pageObj.extractText())

play = pyttsx3.init()
print('Playing Audio Book')
for num in range(0,num_pages):
    page = pdf_reader.getPage(num)
    data= page.extractText()
    play.say(data)
    play.runAndWait()