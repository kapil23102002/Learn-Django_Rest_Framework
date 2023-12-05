from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializier
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,  'home.html')

# Model Object - Single Student data
def student_details(request, pk):
    stu = Student.objects.get(id = pk) # get data from model object by dynamically
    serializer = StudentSerializier(stu) #convert into python data
    json_data = JSONRenderer().render(serializer.data) # convert into JSON data
    return HttpResponse(json_data, content_type='application/json')