from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

#from equityapp.models import equity1
#from equityapp.serializers import equityserializers
from django.shortcuts import render,redirect
 
from django.http import HttpResponse
import mysql.connector
from mysql.connector import Error

import csv
conn=mysql.connector.connect(host='127.0.0.1',
                                         port='3306',
                                         database='EQUITY_L',
                                         user='root',
                                         password='Sandstone@34',
                                        auth_plugin='mysql_native_password'
                                         )
cursor=conn.cursor()
#def categorydisplay(request,id):
#    print(id)
#    cursor.execute("SELECT * FROM 'equity' WHERE `SYMBOL`={}".format(id))
#    data=cursor.fetchone()
#    print(list(data))
#    return render(request,'edit.html',{'categories':data})
def home(request):
    return  render(request,'home.html')
def categorycreate(request):
    return render(request,'add.html')


def categorydelete(request):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
      if request.method == 'POST':
        print(request.POST)
        name = request.POST['symbol']
       
        val='"'+name+'"'
        print(val)
        cursor.execute("SELECT * from `equity` where SYMBOL={}".format(val) )
        data=cursor.fetchall()
        print("value si is is is",data)
        return render(request,'view.html',{'categories':data})
    #return redirect(categorylisting) 
def categorylisting(request):
    cursor.execute("SELECT * FROM `equity`")
    data = cursor.fetchall()
    #return list(data)
    print(data)
    for i in data:
        print(i[0])
        break
    return render(request, 'view.html', {'categories': data})   
#@csrf_exempt
#def equityapi(request,id=0):
#    if request.method=='GET':
#        eqt=equity1.objects.all()
#        equity_serializers=equity_serializers(eqt,many=True)
#        return JsonResponse(equity_serializers.data,safe=False)
