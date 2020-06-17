from django.shortcuts import render
from .models import Schedule
import requests
from rest_framework import generics, status 
from rest_framework.response import Response
from .serializers import ScheduleSerializer
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def task():
    url = Schedule.objects.latest('time').url
    result = requests.get(url).json()
    print(result)

class ScheduleAPI(generics.CreateAPIView):
    queryset= Schedule.objects.all()
    serializer_class = ScheduleSerializer  
    def create(self, request):
        queryset = self.get_queryset()
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            time = request.data['time']
            time = time.replace("T", " ")+":00"
            url = request.data['url']
            scheduler = BackgroundScheduler()
            scheduler.add_job(task, 'date', run_date=time)
            scheduler.start()
            serializer.save()

            return Response({
                'error': False,
                'data': serializer.data,
                'message': 'success',
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': True,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)


        

class ServerStateAPI(generics.ListAPIView):
    def list(self, request):
        return Response({
            'status': 'OK',   
        }, status = status.HTTP_200_OK)
    


        


