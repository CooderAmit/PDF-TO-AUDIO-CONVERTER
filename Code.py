#Amit Kumar



# importing the modules
import PyPDF2
import pyttsx3
#Declaring the total number of pages
n=int(input('Total number of pages'))
#Geting page number where he wants to start listening
i=int(input('Enter the page number where you want to start listening your pdf'))
#creating loop
while(i!=n):
# path of the PDF file
    Pdf_book = open('pdf_address.pdf', 'rb')

# creating a PdfFileReader object
    reading_pdf = PyPDF2.PdfReader(Pdf_book)
    pdf_pages = len(reading_pdf.pages)
    pdf_speaker = pyttsx3.init()

# the page with which you want to start
# this will read the page of nth page.
    choose_page=reading_pdf.pages[i]
    i=i+1

# extracting the text from the PDF
    pdf_text = choose_page.extract_text()

# reading the text
    pdf_speaker.say(pdf_text)
    pdf_speaker.runAndWait()


def textToVoice():
    eng = pyttsx3.init() #initialize an instance
    eng.say("This is a demonstration of how to convert text to voice using pyttsx3 library in python.") #say method for passing text to be spoken
    eng.runAndWait() #run and process the voice command
