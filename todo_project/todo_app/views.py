from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializer import TodoSerializer
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    

class MyTokenObtainPairView(TokenObtainPairView): 
    serializer = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTodos(request):
    user = request.user 
    todos = user.todo_set.all()
    serializer = TodoSerializer(todos , many = True)
    return Response(serializer.data , status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTodos(request) : 
    serializer  = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user = request.user )
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTodo(request , pk):
    try:  
        todo = Todo.objects.get(id = pk)
        if todo.user != request.user : 
            return Response(status=status.HTTP_403_FORBIDDEN)
    except Todo.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TodoSerializer(instance = todo , data = request.data)
    if serializer.is_valid() : 
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)            


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTodo(request , pk):
    try:  
        todo = Todo.objects.get(id = pk)
        if todo.user != request.user : 
            return  Response(status=status.HTTP_403_FORBIDDEN)
    except Todo.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    todo.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)