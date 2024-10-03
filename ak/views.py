from django.shortcuts import render
import time,threading
from django.http import HttpResponse,JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


"""
Note:- sqlite db is used username-admin password-admin.
1. signals are executed synchronously, below is the given example. It trigger signal as employee gets created.
        Delay is used in signal to see how it affects the request/response time in a django view.
2. Django signals run in same thread as the caller so the answer is yes,and it excuted synchronously. Given in below example
3. Yes, django signals run within same database transaction as the caller
"""

def trigger_signal(request):
    caller_thread = threading.current_thread().name
    print(f"Caller thread: {caller_thread}")

    start_time = time.time()
    
   # Creates new employee to trigers post signal in signals file.
    emp=Employee.objects.create(name="test")

    end_time = time.time()
    execution_time = end_time - start_time
    return HttpResponse(f"View execution time: {execution_time} seconds")

class Rectangle(APIView):
    def get(self,request):
        data=request.data
        try:
            if data.get('length')<=0 or data.get('width')<=0:
                return Response({'error': 'Length and width must be positive numbers', "status":400})

            area=data.get('length')*data.get('width')
            response={
                'length':data.get('length'),
                'width':data.get('length'),
                'area':area
            }
            return Response(response)
        except:
            return Response({'error': 'Invalid input. Please provide valid numbers for length and width.', "status":400})
