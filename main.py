n='''
 ________________
( Di 28. Jan     )
( 18:00:02 CET   )
( 2020 Keep your )
( servers time   )
( in sync, use   )
( the ntpd       )
( package.       )
( https://help.u )
( buntu.com/11.1 )
( 0/serverguide/ )
( C/NTP.html     )
 ----------------
   o      
    o    
        ./\.
       |o_o |
       |:_/ |
      //   \ \
     
     (|     | )
    /'\_   _/`\
    
    \___)=(___/

'''


print(n)
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
#speak.Speak("Этот модуль импортирован, чтобы мы могли")

import io
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
 
        text = fake_file_handle.getvalue()
 
    # close open handles
    converter.close()
    fake_file_handle.close()
 
    if text:
        return text
 


import re
def remove_urls(vTEXT):# удаляет ссылки 
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)
import string
def clean(text):# удаляет символы .,/!";%:?*()_+'
    return "".join(l for l in text if l not in string.punctuation)

blabla = clean(remove_urls(extract_text_from_pdf('3.pdf')))
#print(blabla)
import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
#for voice in voices:
#    if voice.name == 'Aleksandr':
#tts.setProperty('voice', voice.id)
tts.setProperty('rate', 160)


#tts.say(blabla)
tts.save_to_file(blabla,"saved_file.mp3")
tts.runAndWait()


