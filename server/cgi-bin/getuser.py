#!coding:utf8
import cgi,cgitb
import urllib2
form=cgi.FieldStorage()
name=form.getvalue('user_name')
age=form.getvalue('user_age')
sex=form.getvalue('user_sex')
data=name
print "Content-type: text/html"

print

if name != None and len(name) > 0:
    print "<p id=name>%s</p>"%name
else:
    print "<p id=name>请输入相关信息</p>"
