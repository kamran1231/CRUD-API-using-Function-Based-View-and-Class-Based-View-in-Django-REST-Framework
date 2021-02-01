from django.shortcuts import render,HttpResponse
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework import serializers
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View


@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')


    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)

        # partial update
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')




    def delete(self, request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        # object ko get karege:
        stu = Student.objects.get(id=id)
        # no need to call serializer
        stu.delete()
        # now we need to send a respose to a user that his data has been deleted:
        res = {'msg': 'Data deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        # if u dont want to write this 2 line so u need to do this:
        return JsonResponse(res, safe=False)







# Create your views here.
# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return  HttpResponse(json_data,content_type='application/json')
#
#         else:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu, many=True)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#
#
#     elif request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data,content_type='application/json')
#
#
#     elif request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#
#         #partial update
#         serializer = StudentSerializer(stu, data=python_data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
#
#
#     elif request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         #object ko get karege:
#         stu = Student.objects.get(id=id)
#         #no need to call serializer
#         stu.delete()
#         #now we need to send a respose to a user that his data has been deleted:
#         res = {'msg': 'Data deleted'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data,content_type='application/json')
#         #if u dont want to write this 2 line so u need to do this:
#         return JsonResponse(res,safe=False)



