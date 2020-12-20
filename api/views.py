from django.shortcuts import render
from .models import Task
from .models import Tag
from .models import User
from .models import Project
from .models import Company
from .models import BillingInfo
from .serializers import TaskSerializer
from .serializers import TagSerializer
from .serializers import UserSerializer
from .serializers import ProjectSerializer
from .serializers import CompanySerializer
from .serializers import BillingInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

'''
Task
This function manage GET and POST requests over /api/tasks URL
If method is GET, all the Task objets are read and sent to the serializer to tranform them in json and sent back to the requester
If method is POST, we first check the restriction. Upon sucessfully checked, the task information in the request is deserialized
and the task is created. If the restriction is not sucess, the task is not created and a message is shown. 
'''
@api_view(['GET','POST'])
def task_list(request):
    if request.method=='GET':
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        # We check the restriction before creating the Task
        data=request.data
        usuario_task=data.get('user')
        proyecto_task=data.get('project')
        
        # We try to get the User object that corresponds to the user
        if (User.objects.filter(id=usuario_task)):
            print ("User exists")
        else:
            print ("User doesn´t exist")
            return Response(data=None)

        if (User.objects.get(id=usuario_task).projects.all().filter(id=proyecto_task)):
            # Create the Task
            print ('Create the task')
            serializer=TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Don´t create the task
            print('Task can not be created because the user has not been assigned to the project')
            return Response(data=None)
                
        '''OPTION 2. We can make the check in a single line but it can generate an exception
        try:
            User.objects.get(id=usuario_task).projects.all().get(id=proyecto_task)
        except:
            print('Task can not be created because the user has not been assigned to the project')
            return Response(data=None)
        else:
            # Create Task
            serializer=TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''

'''
Task
This function manages GET, PUT and DELETE requests over api/tasks/<int:pk>/ URL
If method is GET, we respond to the requester with the json data for the task requested.
If method is PUT, we first check the restriction. Upon sucessfully checked, the task information in the request is deserialized
and the task is created. If the restriction is not sucess, the task is not created and a message is shown.
If method is DELETE, we directly delete the task 
'''
@api_view(['GET','PUT','DELETE'])
def task_detail(request,pk):
    # Find task by primary key pk
    try:
        task=Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'message': 'Task doesn´t exist'})
        status=status.HTTP_404_NOT_FOUND

    if request.method=='GET':
        serializer=TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        data=request.data
        usuario_task=data.get('user')
        proyecto_task=data.get('project')
        
        try:
            User.objects.get(id=usuario_task).projects.all().get(id=proyecto_task)
        except:
            print('Task can not be updated because the user has not the project asigned previously')
            return Response(data=None)
        else:
            serializer=TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        task.delete()
        return Response(data=None)

'''
Tag
This function manage GET and POST requests over /api/tags URL
If method is GET, all the Tag objets are read and sent to the serializer to tranform them in json and sent back to the requester.
If method is POST, a Tag object is created.
'''
@api_view(['GET','POST'])
def tag_list(request):
    if request.method=='GET':
        tags=Tag.objects.all()
        serializer=TagSerializer(tags, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        # Create Tag
        serializer=TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Tag
This function manages GET, PUT and DELETE requests over api/tags/<int:pk>/ URL
If method is GET, we respond to the requester with the json data for the tag requested.
If method is PUT, we update the tag
If method is DELETE, we directly delete the tag 
'''
@api_view(['GET','PUT','DELETE'])
def tag_detail(request,pk):
    # Find tag by primary key pk
    try:
        tag=Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response({'message': 'Tag doesn´t exist'})
        status=status.HTTP_404_NOT_FOUND

    if request.method=='GET':
        serializer=TagSerializer(tag)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        tag.delete()
        return Response(data=None)

'''
USER
This function manage GET and POST requests over /api/users URL
If method is GET, all the User objets are read and sent to the serializer to tranform them in json and sent back to the requester.
If method is POST, a User objetct is created.
'''
@api_view(['GET','POST'])
def user_list(request):
    if request.method=='GET':
        users=User.objects.all()
        serializer=UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        # Create the user
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
User
This function manages GET, PUT and DELETE requests over api/users/<int:pk>/ URL
If method is GET, we respond to the requester with the json data for the user requested.
If method is PUT, we update the user
If method is DELETE, we directly delete the user 
'''
@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    # Find user by primary key pk
    try:
        user=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'message': 'El usuario no existe'})
        status=status.HTTP_404_NOT_FOUND

    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        user.delete()
        return Response(data=None)

'''
PROJECT
This function manage GET and POST requests over /api/projects URL
If method is GET, all the Project objets are read and sent to the serializer to tranform them in json and sent back to the requester.
If method is POST, a Project objetct is created.
'''
@api_view(['GET','POST'])
def project_list(request):
    if request.method=='GET':
        projects=Project.objects.all()
        serializer=ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        # Create Project
        serializer=ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Project
This function manages GET, PUT and DELETE requests over api/projects/<int:pk>/ URL
If method is GET, we respond to the requester with the json data for the project requested.
If method is PUT, we update the project
If method is DELETE, we directly delete the project 
'''
@api_view(['GET','PUT','DELETE'])
def project_detail(request,pk):
    # Find project by primary key pk
    try:
        project=Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'message': 'Project doesn´t exist'})
        status=status.HTTP_404_NOT_FOUND

    if request.method=='GET':
        serializer=ProjectSerializer(project)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        project.delete()
        return Response(data=None)

'''
COMPANY
This function manage GET and POST requests over /api/companies URL
If method is GET, all the Company objets are read and sent to the serializer to tranform them in json and sent back to the requester.
If method is POST, a Company objetct is created.
'''
@api_view(['GET','POST'])
def company_list(request):
    if request.method=='GET':
        companies=Company.objects.all()
        serializer=CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        # Create Company
        serializer=CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Company
This function manages GET, PUT and DELETE requests over api/companies/<int:pk>/ URL
If method is GET, we respond to the requester with the json data for the company requested.
If method is PUT, we update the company
If method is DELETE, we directly delete the company 
'''
@api_view(['GET','PUT','DELETE'])
def company_detail(request,pk):
    # Find company by primary key pk
    try:
        company=Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({'message': 'Company doesn´t exist'})
        status=status.HTTP_404_NOT_FOUND

    if request.method=='GET':
        serializer=CompanySerializer(company)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        company.delete()
        return Response(data=None)

'''
BillingInfo
This function manage GET and POST requests over /api/billinginfos URL
If method is GET, all the BillingInfo objets are read and sent to the serializer to tranform them in json and sent back to the requester.
If method is POST, a BillingInfo objetct is created.
'''
@api_view(['GET','POST'])
def billinginfo_list(request):
    if request.method=='GET':
        billinginfos=BillingInfo.objects.all()
        serializer=BillingInfoSerializer(billinginfos, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        # Create Billing Info
        serializer=BillingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
BillingInfo
This function manages GET, PUT and DELETE requests over api/billinginfos/<int:pk>/ URL
If method is GET, we respond to the requester with the json data for the billing info requested.
If method is PUT, we update the billing info
If method is DELETE, we directly delete the billing info 
'''
@api_view(['GET','PUT','DELETE'])
def billinginfo_detail(request,pk):
    # Find billing info by primary key pk
    try:
        billinginfo=BillingInfo.objects.get(pk=pk)
    except BillingInfo.DoesNotExist:
        return Response({'message': 'Billing Info doesn´t exist'})
        status=status.HTTP_404_NOT_FOUND

    if request.method=='GET':
        serializer=BillingInfoSerializer(billinginfo)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=BillingInfoSerializer(billinginfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        billinginfo.delete()
        return Response(data=None)
