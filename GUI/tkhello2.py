# coding: utf-8


import tkinter


'''
Button
'''
top = tkinter.Tk()
quit = tkinter.Button(top, text='Hello World!', command=top.quit)
quit.pack()
tkinter.mainloop()