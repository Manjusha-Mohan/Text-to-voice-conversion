import PyPDF2
import pyttsx3

def repeat():
    val = input(' Press c to read another:\n > ')

    if (val=='c'):
        read()
    return val

def getinput():
    text = input(' Enter text:\n > ')
    getsound(text)
    return

def voiceselection():
    s=input(" For Male voice - press 0  or For Female voice - press 1 \n > " )
    return s

def playbackspeed():
    print(" choose playback speed :")
    rate=input("  1. Slow \n  2. Normal \n  3. Fast\n  > ")
    if (rate == '1'):
        r = 90
    elif (rate == '2'):
        r = 150
    elif (rate == '3'):
        r = 220
    else:
        r = 150
    return r

def changevolume():
    v=input("Choose volume:\n 1. Low \n 2. Medium \n 3. High \n > ")
    if(v=='l'):
        i=0.65
    elif(v=='h'):
        i=-0.65
    else:
        i=0
    return i

def readpdf():
    path = input(' Enter path:\n > ')
    pdfFileObject = open(path, mode='rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    with open("new.txt", 'w') as pdf_out:
        for page in range(pdfReader.getNumPages()):
            data = pdfReader.getPage(page).extractText()
            pdf_out.write(data)
    file = open("new.txt", 'r')
    fread = file.read().replace('\n', '')
    getsound(fread)

def readtxt():
    path = input(' Enter path:\n > ')
    file = open(path, mode='rb')
    text = file.read()
    getsound(text)
    return

def saveaudio():
    flag=input(' Do you want to save this audio file:Y/N \n > ')
    if(flag=='y'):
        flag=1
    else:
        flag=0
    return flag

def getsound(text):
    s = int(voiceselection())
    r = int(playbackspeed())
    i = float(changevolume())
    f = int(saveaudio())

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    volume = engine.getProperty('volume')

    engine.setProperty('voice', voices[s].id)
    engine.setProperty('rate', r)
    engine.setProperty('volume', volume-i)

    if (f == 1):
        name = input('Save filename as: \n > ')
        engine.save_to_file(text, name+'.mp3')
        print('File saved as ',name+'.mp3 \n \n ')

    read = input(' Press enter to start reading\n > ')
    engine.say(text)
    engine.runAndWait()
    repeat()
    return

def readfile():

    print("Option 1 : Read PDF ")
    print("Option 2 : Read Text File")
    option = input(' Choose an option:\n > ')

    if option == '1':
        readpdf()
    elif option == '2':
        readtxt()
    else:
        print("*******Choose a valid option*******")
    return

def read():
    print("Option 1 : Read File")
    print("Option 2 : Read Input from User")
    option = input(' Choose an option:\n > ')

    if option == '1':
        readfile()
    elif option == '2':
        getinput()
    else:
        print("*******Choose a valid option*******")
    return

read()
