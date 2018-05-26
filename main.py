# coding=utf-8

from bs4 import BeautifulSoup
import requests
import re
#----------------------------
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('行列字典')
        self.create_main()

    #--------------functions--------------
    def find_the_word(self):
        link = 'http://www.array30.com/cgi-bin/lookup.py?character='+self.checkWord.get()
        r = requests.get(link)
        r.encoding = 'utf-8'
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.find_all('li'):
            self.create_label(i.string)

    def check_input_validate(self, event=None):
        for i in self.labelFrame.winfo_children():
            i.destroy()

        if len(self.checkWord.get()) == 1 and re.search(u'[\u4e00-\u9fff]', self.checkWord.get()):
            self.find_the_word()
            self.checkWord.set('')
        else:
            self.checkWord.set('請輸入一個中文字')

    #--------------interfaces--------------
    def create_main(self):
        self.labelFrame = tk.LabelFrame(self.window, text='結果', labelanchor='n')
        self.labelFrame.grid(row=0, columnspan=2, sticky='WE', padx=5)

        self.checkWord = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.checkWord).grid(column=0, row=1, pady=5, padx=5)
        ttk.Button(self.window, text='查字', command=self.check_input_validate).grid(column=1, row=1, pady=5, padx=5)
        self.window.bind('<Return>', self.check_input_validate)

    def create_label(self, content):
        ttk.Label(self.labelFrame, text=content).pack(pady=3)

#--------------main--------------
if __name__== '__main__' :
    app = App()
    app.window.mainloop()
    
