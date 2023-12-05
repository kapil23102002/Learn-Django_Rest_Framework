from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializier
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,  'home.html')

# Model Object - Single Student data
def student_details(request, pk):
    stu = Student.objects.get(id = pk) # get data from model object by dynamically
    serializer = StudentSerializier(stu) #convert into python data
    
    # json_data = JSONRenderer().render(serializer.data) # convert into JSON data
    # return HttpResponse(json_data, content_type='application/json')
# replace lower line from upper 2 lines----------
    return JsonResponse(serializer.data)

# Quesry Set - All Student Data
def student_info(request):
    stu = Student.objects.all()# get all data from model object
    serializer = StudentSerializier(stu, many = True) #convert into python data
    return JsonResponse(serializer.data, safe = False) # safe = False becoz all data is not dict format
    
# Post Method by using Desirializer  with third party App ------------

@csrf_exempt
def student_deserializer(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializier(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created...'}
            return JsonResponse(res)
        else:
            return JsonResponse(serializer.errors)
