# -*- coding: utf-8 -*- 

'''
CGI脚本从表单中获取person和howmany字段，使用这些数据创建动态生成的结果页面
'''

import cgi

reshtml = '''Content-Type: text/html\n
<html><head><title>Friends CGI Demo</title></head>
<body><h3>Friedns list for: <i>%s<i></h3>
Your name is:<b>%s</b>
You have <b>%s</b> friends.</body></html>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(reshtml % (who, who, howmany))