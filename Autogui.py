import tkinter as tk
from tkinter import messagebox
import requests
window=tk.Tk()
window.title('神武辅助')
window.geometry('500x300')
window.geometry('+500+800')
#window.geometry('400x100+500+800')
var = tk.StringVar()
l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.grid(row=0,column=1)
on_hit = False
def download():
    URL='http://www.uustv.com/'
    name=entry.get()
    name=name.strip()
    if name=='':
        messagebox.showinfo('提示：','请输入名字')
    else:
        data={
            'word':name,
            'size':60,
            'fonts':1.ttf,
            'fontcolor':#000000
        }
        r=requests.post(url.data)
        print(r)
        print(name)
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')
b=tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.grid(row=0,column=0)
entry=tk.Entry(window,font=('微软雅黑',20))
entry.grid(row=1,column=1)
label=tk.Label(window,text='签名', font=('华文行楷',20),fg='red')
label.grid(row=1,column=0)
b1=tk.Button(window, text='设计签名', width=15, height=2, command=download)
b1.grid(row=2,column=0)
window.mainloop()
