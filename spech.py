from google_images_download import google_images_download
import speech_recognition as sr

#
from textblob import TextBlob
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
import tkinter as tk
from PIL import Image, ImageTk
import os
from pathlib import Path
#

#r1=sr.Recognizer()
#r2=sr.Recognizer()
r3=sr.Recognizer()
diziverb=["run","buy","go","sell","work","get","wear","see","drink"] #add any verb...
diziadj=["good","empty","hard","full","wet","thin","bad","happy","fat"]#add any adjective...
dizinoun=["car","apple","phone","tree","money","book","door","house"]#add any noun...
dizi2=[] # add word ...
print("""
-----------------------------------------------------
konuşmada geçen öğrenmek istediğiniz yapıları seçin:
 isimler..........................1
 sıfatlar.........................2
 fiiller..........................3
 ----------------------------------------------------
 """)
secim=input("öğrenmek istediğiniz kelime grubu : ")
if secim == "1":
    dizi2=dizinoun
elif secim == "2":
    dizi2=diziadj
elif secim == "3":
    dizi2=diziverb
else :
    print("hatalı seçim")
print(dizi2)
i=0
dizi1=[]

dizi3=[]
#
dizi4=[]
#
for i in range(len(dizi2)):
    dizi1.append(0)


#with sr.Microphone() as source:

     #print('speak')
     #audio = r3.listen(source)

#if 'car' in r3.recognize_google(audio):
#r3 = sr.Recognizer()
#    print('apple')

with sr.Microphone() as source:
    print('speak')
    audio = r3.listen(source)
    r3.adjust_for_ambient_noise(source, duration=0.2)
    audio = r3.listen(source)
    MyText = r3.recognize_google(audio)
    MyText = MyText.lower()
    print(MyText)
    for i in range(len(dizi2)):
        if dizi2[i] in r3.recognize_google(audio):
            dizi1[i] = dizi1[i] + 1
    for i in range(len(dizi2)):
        if dizi1[i] > 0:
            dizi3.append(dizi2[i])
    #for i in range(len(dizi3)):
        #print(dizi3[i])
    for i in range(len(dizi3)):
        if dizi3[i] in r3.recognize_google(audio):
            response = google_images_download.googleimagesdownload()
            arguments = {"keywords": dizi3[i], "limit": 1, "print_urls": True}
            paths = response.download(arguments)
            print(paths)

            #
            cümle1 = dizi3[i]
            text1 = TextBlob(cümle1)
            cevir1 = text1.translate(to="tr")
            # print(cevir1)
            dizi4.append(cevir1)
            #
            #
    for i in range(len(dizi4)):
        root = tk.Tk()
        root.title("{name1}".format(name1=dizi3[i]))
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, "{engg}\n{trr}".format(engg=dizi3[i], trr=dizi4[i]))
        with os.scandir("C:/Users/ent95/PycharmProjects/untitled/venv/Include/downloads/{name}/".format(name=dizi3[i])) as entries:
            for entry in entries:
                filename1 = entry.name
        im = Image.open("C:/Users/ent95/PycharmProjects/untitled/venv/Include/downloads/{name}/{filenamee}".format(name=dizi3[i],filenamee=filename1))
        photo = ImageTk.PhotoImage(im)
        cv = tk.Canvas(root, width=3000, height=1000)
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(10, 10, image=photo, anchor='nw')
        root.mainloop()
        #
    #if 'car' in r3.recognize_google(audio):
        #response = google_images_download.googleimagesdownload()
        #arguments = {"keywords": "car", "limit": 1, "print_urls": True}
        #paths = response.download(arguments)
        # print complete paths to the downloaded images
        #print(paths)

    try:
        get= r3.recognize_google(audio)
        print(get)

        #wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))
