from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_employee(request):
    serializer = employeeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def read_employee(request):
    employees = employee.objects.all()
    serializer = employeeSerializers(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def read_employee_pk(request, pk):
    employee_instance = get_object_or_404(employee, pk=pk)
    serializer = employeeSerializers(employee_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['PUT'])
def update_employee(request, pk):
    employee_instance = get_object_or_404(employee, pk=pk)
    serializer = employeeSerializers(employee_instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee(request, pk):
    employee_instance = get_object_or_404(employee, pk=pk)
    employee_instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
