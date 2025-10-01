from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import EmpModel
from .emp_serializer import EmpSerializer

# Create your views here.
def home(request):
    return HttpResponse("<h3>WELCOME AFREEN</h3>")

@api_view(['GET'])
def fbv_crud(request,pk=None):
    if pk is not None:
        try:
            emp_=EmpModel.objects.get(pk=pk)
        except EmpModel.DoesNotExist:
            return Response({'res':f'{emp_} does not exists'},status=status.HTTP_400_BAD_REQUEST)
        else:
            seri = EmpSerializer(emp_)
            return Response({'res':seri.data},status=status.HTTP_200_OK)
    else:
        all = EmpModel.objects.all()
        seri = EmpSerializer(all,many=True)
        return Response({'res':seri.data},status=status.HTTP_200_OK)