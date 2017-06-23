# -*- coding: utf-8 -*-


from functools import partial as pto
from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror


'''
偏函数（pfa）可以有效地‘冻结’那些预先确定的参数来缓存函数参数，然后在运行时，当获得
需要的剩余参数后，可以将它们解冻，传递到最终的参数中，从而使用最终确定的所有参数去调用函数。
本例使用交通路标，严重级别标志为白底红字，警告级别为黄底黑字，通知级别为白底黑字。
'''


WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter' : CRIT,
    'railroad crossing' : WARN,
    '55\nspeed limit' : REGU,
    'wrong way' : CRIT,
    'merging traffic' : WARN,
    'one way' : REGU,
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='yellow')
ReguButton = pto(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signType.title(), 
                                                             eachSign,
                                                             '.upper()' if signType == CRIT else '.title()')
    eval(cmd)

top.mainloop()



