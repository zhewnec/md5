import json
import sqlite3
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def md5(request):
    text = request.GET.get("a")
    value = filter(text)
    text = [value]
    return render(request, "hello.html", {"text": json.dumps(text)})

"""
def home(request):
    return render(request, "index.html")
"""

def filter(value):
    if value.strip() == "":
        return "请输入MD5值"

    elif value.isalnum() and value.islower() and len(value) == 32:
        """
        然后就进行数据库密文和密文对比
        返回原文，如果原文为空就返回抱歉未找到原文    
       """
        try:
            return sql(value)
        except:
            return "抱歉,解密未成功"
    else:
        return "不是标准的md5值"


def sql(value):

    conn = sqlite3.connect('/home/orange/db_File/password.db')
    c = conn.cursor()
    sql = "select text from password_name where md5='%s';" % value
    data = c.execute(sql)
    da = data.fetchall()

    conn.commit()
    conn.close()

    return da[0][0]
