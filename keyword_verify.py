# -*- encoding:utf-8 -*-
import requests as r
import Tkinter as tk
urls = ['http://www.sougo.com/']
def get():
    requested_vals = []
    for i in urls:
        url = r.get(i)
        url.encoding = 'utf-8'
        requested_vals.append(url.text)
    return requested_vals
def submit(word):
    requested_vals = get()
    cnt = 0
    for i in requested_vals:
        cnt += i.count(word)
    if(cnt == 0):
        return '0%'
    elif(cnt == 1):
        return '20%'
    elif(cnt == 2):
        return '40%'
    elif(cnt == 3):
        return '60%'
    elif(cnt == 4):
        return '80%'
    else:
        return '≥99%'
def f(x):
    print(x)
def main():
    base = tk.Tk()
    var = tk.StringVar()
    var.set('')
    Label1 = tk.Label(base,textvariable=var)
    entry1 = tk.Entry(base)
    button = tk.Button(base,text = 'Submit',command = lambda:var.set(submit(entry1.get())))
    button.grid(column = 0,row = 0)
    entry1.grid(column = 1,row = 0)
    Label1.grid(column = 1,row = 1)
    tk.mainloop()
if(__name__ == '__main__'):
    main()
