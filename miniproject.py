from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from tkinter.ttk import Combobox
from gtts import gTTS
import PyPDF2
import pyttsx3
import easyocr
import webbrowser
import os
import clipboard
from playsound import playsound

#image to text
def image2text():
    def extract_text():
        filepath = filedialog.askopenfilename(title='Open Image File', filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if not filepath:
            return
        reader = easyocr.Reader(['en'])
        result = reader.readtext(filepath)

        extracted_text = ''
        for res in result:
            extracted_text += res[1] + ' '

        text_display.delete(1.0, END)  
        text_display.insert(END, extracted_text)
        
    def cls1():
         text_display.delete(1.0, END)
    
    def select():
        text_display.tag_add('sel','1.0','end')
        text_display.tag_config('sel',foreground='brown')     
     
    ocrwindow = Tk()
    ocrwindow.title('Image Text Extractor')
    ocrwindow.geometry("1000x580+200+80")
    ocrwindow.configure(bg='#BF8DEB')
    ocrwindow.resizable(False,False)

    extract_button = Button(ocrwindow, text='Extract Text', command=extract_text)
    extract_button.pack(pady=30)

    text_display = Text(ocrwindow, height=50, width=30,font='TimesNewRoman 20', bg='white',relief= GROOVE, wrap= WORD,bd=0)
    text_display.place(x=30,y=150,width=940,height=180)
    
    clear_btn = Button(ocrwindow,text = "Clear",command= cls1)
    clear_btn.pack(padx=80,pady=100)
    
    copy_b=Button(ocrwindow,text='copy',command=lambda:text_display.event_generate("<<Copy>>"))
    copy_b.pack(padx=50,pady=100)
    
    select_all=Button(ocrwindow,text='Select All',command=select)
    select_all.pack(padx=10,pady=100)
    
    ocrwindow.mainloop()
    
#textreader
tts= pyttsx3.init()
def texts():
    
    def speaknow():
        text= text_box.get(1.0,END)
        gender= gender_box.get()
        speed = speed_box.get()
        voices = tts.getProperty('voices')
        
        def setvoice():
            if gender=='Male':
                tts.setProperty('voice',voices[0].id)
                tts.say(text)
                tts.runAndWait()
                
            else:
                tts.setProperty('voice', voices[1].id)
                tts.say(text)
                tts.runAndWait()
            
        if(text):
                if(speed == 'Fast'):
                    tts.setProperty('rate',250)
                    setvoice()
                elif (speed == 'Medium'):
                    tts.setProperty('rate',150)
                    setvoice()
                else:
                    tts.setProperty('rate',60)
                    setvoice()
    def  download():
        text= text_box.get(1.0,END)
        gender= gender_box.get()
        speed = speed_box.get()
        voices = tts.getProperty('voices')
        
        def setvoice():
            if gender=='Male':
                tts.setProperty('voice',voices[0].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                tts.save_to_file(text,'text.mp3')
                tts.runAndWait()
                
            else:
                tts.setProperty('voice', voices[1].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                tts.save_to_file(text,'text.mp3')
                tts.runAndWait()
            
        if(text):
                if(speed == 'Fast'):
                    tts.setProperty('rate',250)
                    setvoice()
                elif (speed == 'Medium'):
                    tts.setProperty('rate',150)
                    setvoice()
                else:
                    tts.setProperty('rate',60)
                    setvoice()
    
    def cls1():
         text_box.delete(1.0, END)
                       
        
    import tkinter as tk
    gttswindow = Tk()
    gttswindow.title('Text-to-Speech')
    gttswindow.geometry("1000x580+200+80")
    gttswindow.configure(bg='#9384D1')
    gttswindow.resizable(False,False)

    #Upper Frame
    upper_frame= Frame(gttswindow, bg='#FFDCB6', width=1200,height=130)
    upper_frame.place(x=0,y=0)

    #Title
    Label(upper_frame,text='Text to Speech Converter', font='TimesNewRoman 40 bold',
        bg='#FFDCB6', fg='black').place(x=200,y=35)


    #Text box input
    text_box = Text(gttswindow, font='TimesNewRoman 20', bg='white',relief= GROOVE, wrap= WORD,bd=0)
    text_box.place(x=30,y=150,width=940,height=180)

    #Gender Selection
    gender_box= Combobox(gttswindow,values=['Male','Female'], font=' TimesNewRoman 12', state='r',width=15)
    gender_box.place(x=310,y=350)
    gender_box.set('Male')

    #Speed Selection
    speed_box = Combobox(gttswindow,values=['Fast','Medium','Slow'], font= 'TimesNewRoman 12',state='r',width=15)
    speed_box.place(x=540,y=350)
    speed_box.set('Medium')

    #Play Button
    play_btn= Button(gttswindow,text='Play',compound=LEFT, bg='white',width=10,font='TimesNewRoman 14 bold',
                    borderwidth = '0.1c',command= speaknow)
    play_btn.place(x=430,y=400)
    
    #Save Button
    save_btn=Button(gttswindow,text='Save',compound=LEFT,bg='white',width=10,font='TimesNewRoman 14 bold',
                    borderwidth = '0.1c',command= download)
    save_btn.place(x=430,y=500)
    
    #clear
    clear_btn = Button(gttswindow, compound=RIGHT,text = "Clear",bg='white',width=10,font='TimesNewRoman 14 bold',
                    borderwidth = '0.1c',command= cls1)
    clear_btn.place(x=430,y=450)


    gttswindow.mainloop() 
    
 #pdfreader
def readers():
    def read_pdf_and_speak():
        filepath = filedialog.askopenfilename(title='Open PDF file', filetypes=[("PDF File", "*.pdf")])
        if not filepath:
            return

   
        with open(filepath, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            text = ''
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

   
            speak = pyttsx3.init()
   
            speak.say(text)
            speak.runAndWait()

    readerwindow = Tk()
    readerwindow.title('PDF Text-to-Speech Converter')
    readerwindow.geometry("1000x580+200+80")
    readerwindow.configure(bg='#9EC9E6')
    readerwindow.resizable(False,False)

    convert_button =Button(readerwindow, text='Read PDF and Speak', command=read_pdf_and_speak)
    convert_button.pack(pady=20)


    readerwindow.mainloop()
        

        
def conta(event):
    webbrowser.open("https://github.com/Reethika12")  

window = Tk()
window.title('All in One')
window.geometry('500x500')

heading_label = ttk.Label(window, text='Find everything you want', font=('Helvetica', 25),foreground='lightgrey',background='purple')
heading_label.pack(pady=20)

c_button = ttk.Button(window, text='Image to Text', command=image2text, width=25)
c_button.pack(pady=10)

f_button = ttk.Button(window, text='Textreader', command=texts, width=25)
f_button.pack(pady=10)

g_button = ttk.Button(window, text='Pdfreader', command=readers, width=25)
g_button.pack(pady=10)

contact_us_button = ttk.Button(window, text='Contact us',width=25)
contact_us_button.bind("<Button-1>", conta)
contact_us_button.pack(pady=10)

exit_button = ttk.Button(window, text='Exit', command=quit, width=25)
exit_button.pack(pady=10)

window.configure(bg='#B7EDEE')    
window.eval('tk::PlaceWindow . center')

window.mainloop()     