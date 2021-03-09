import tkinter as tk
window=tk.Tk()
window.title('神武辅助')
window.geometry('500x300')
window.geometry('+500+800')
#window.geometry('400x100+500+800')
var = tk.StringVar()
l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')
b=tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()
Label=tk.Label(window,text='签名', font=('华文行楷',20))
Label.pack()
window.mainloop()
