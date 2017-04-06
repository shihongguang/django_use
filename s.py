#coding=utf-8
import os
import sys


if os.name == "posix":
    pass
else:
    raise("not linux system")

#接收传入的参数
name, xm, app = sys.argv

#当前路径
abspath = os.path.abspath(".")
#项目路径
base_path = os.path.join(abspath, xm)
#项目中的项目设置路径
xm_path = os.path.join(base_path, xm)
#app路径
app_path = os.path.join(base_path, app)
#静态文件路径
static_path = os.path.join(base_path, "static")
#模板路径
templates_path = os.path.join(base_path, "templates")

#要执行的系统命令
adjure_xm = "django-admin startproject " + xm
adjure_app = "python manage.py startapp " + app  

def main():
    #创建项目
    os.system(adjure_xm)
    #切换项目目录
    os.chdir(base_path)
    #创建app
    os.system(adjure_app)
    create_templates()
    create_staic()
    create_app_con()

    print("\nok\n")
#创建模板目录
def create_templates():
    templates_dir = "templates/" + app
    os.makedirs(templates_dir)

#创建静态目录以及内部结构
def create_staic():
    os.mkdir("static")
    os.chdir(static_path)

    os.mkdir("css")
    os.mkdir("js")
    os.mkdir("images")

    #项目图片储存目录
    media_dir = "media/" + xm
    os.makedirs(media_dir)

def create_app_con():
    #app创建urls.py
    os.chdir(app_path)
    os.system("touch uwsgi.ini")

    ac = "    url(r'%s', include('%s')),\n"%("^", app+".urls")
    os.chdir(xm_path)
    with open("urls.py","r") as f:
        list_urls_con = f.readlines()
        list_urls_con.insert(-2,ac)

    with open("urls.py","w") as p:

        for temp in list_urls_con:
            p.write(temp)


    os.chdir(app_path)

    ulist= ['from django.conf.urls import include, url\n',
            'from django.contrib import admin\n',
            'from . import views\n',
            '\n',
            'urlpatterns = [\n',
            "    url(r'^$', views.index),\n",
            ']\n']

    with open("urls.py","w") as p:
        p.write("".join(ulist))


    uwsgi = ['[uwsgi]\n',
             'socket=127.0.0.1:8000\n',
             '#http=127.0.0.1:8000\n',
             'chdir=\n',
             'wsgi-file=\n',
             'processes=4\n',
             'threads=2\n',
             'master=True\n',
             'pidfile=uwsgi.pid\n',
             'daemonize=uswgi.log']

    with open("uwsgi.ini","w") as p:
        p.write("".join(uwsgi))


    view = ['from django.http import HttpResponse\n',
            '\n\n',
            'def index(request):\n',
            '    return HttpResponse("index")']

    with open("views.py","r") as f:
        views = f.readlines()
    views.extend(view)
    with open("views.py","w") as p:
        p.write("".join(views))

main()