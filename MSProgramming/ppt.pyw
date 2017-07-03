# -*- coding: utf-8 -*-

'''
 本脚本会启动PowerPoint,并在幻灯片中将数据写入文本框中
'''
from tkinter import Tk
from time import sleep 
from tkinter.messagebox import showwarning
import win32com.client as win32 

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3,8)

def ppt():
    app = 'PowerPoint'
    ppt = win32.gencache.EnsureDispatch('%s.Application' % app)
    pres = ppt.Presentations.Add()
    ppt.Visible = True

    sl = pres.Slides.Add(1, win32.constants.ppLayoutText)
    sleep(1)
    sla = sl.Shapes[0].TextFrame.TextRange
    sla.Text = 'Python-to-%s Demo' % app
    sleep(1)
    slb = sl.Shapes[1].TextFrame.TextRange
    for i in RANGE:
        slb.InsertAfter('Line %d\r\n' % i)
        sleep(1)
    slb.InsertAfter("\r\nTh-th-th-that's all folks!\r\n")

    warn(app)
    pres.Close()
    ppt.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    ppt()
 

