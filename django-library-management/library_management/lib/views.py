from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from lib.models import library
from lib.serializers import libraryserializers
# Create your views here.

@csrf_exempt
def libraryview(request,id=0):
    if request.method=="GET":
        libval=library.objects.all()
        lib_serialize=libraryserializers(libval,many=True)
        return JsonResponse(lib_serialize.data,safe=False)
    elif request.method=="POST":
        libdata=JSONParser().parse(request)
        lib_serialize=libraryserializers(data=libdata)
        if lib_serialize.is_valid():
            lib_serialize.save()
            return JsonResponse("successfully added",safe=False)
        return JsonResponse("failed")
    elif request.method=='PUT':
        libchg=JSONParser().parse(request)
        lib_put=library.objects.get(userid=libchg['userid'])
        lib_serialize=libraryserializers(lib_put,data=libchg)
        if lib_serialize.is_valid():
            lib_serialize.save()
            return JsonResponse("successfully updated",safe=False)
        return JsonResponse("failed")
    elif request.method=="DELETE":
        lib_del=library.objects.get(userid=id)
        lib_del.delete()
        return JsonResponse("successfully deleted",safe=False)
