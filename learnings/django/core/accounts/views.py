from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *
from rest_framework.views import APIView,Response, status
# Create your views here.

def Hello(request):
    return HttpResponse(render(request,"index.html",context={'items':[1,2,3,4,5,6]}))


class CrudView(APIView):
    def get(self,request):
        name = request.query_params.get('name',None)
        students = Student.objects.filter(name=name)
        
        return Response(students)
    
    def post(self,request):
        name = request.data.get('name')
        age = request.data.get('age')
        email = request.data.get('email')
        address = request.data.get('address')

        if name == '' or age == '' or email == '' or address == '':
            return Response('Please provide all details!',status=400)
        
        student,created = Student.objects.get_or_create(name=name,age=age,email=email,address=address)
        if not created:
            return Response(f'Warning:Object already created:{student}',status=200)
        return Response(student,status=200)