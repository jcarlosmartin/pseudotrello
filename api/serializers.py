from rest_framework import serializers
from .models import Task
from .models import Tag
from .models import User
from .models import Project
from .models import Company
from .models import BillingInfo

# TaskSerializer class is used to send the data corresponding to the Task class in models.py in a json format
class TaskSerializer (serializers.ModelSerializer):
    class Meta:
        model=Task
        # These are the fields in the Task class that will be sent via json
        fields=['id', 'nombre', 'descripcion', 'tags', 'user', 'project']

# TagSerializer class is used to send the data corresponding to the Tag class in models.py in a json format
class TagSerializer (serializers.ModelSerializer):
    class Meta:
        model=Tag
        # These are the fields in the Task class that will be sent via json
        fields=['id','estado']

# UserSerializer class is used to send the data corresponding to the User class in models.py in a json format
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model=User
        # These are the fields in the Task class that will be sent via json
        fields=['id', 'nombre','company','projects']

# ProjectSerializer class is used to send the data corresponding to the Project class in models.py in a json format
class ProjectSerializer (serializers.ModelSerializer):
    class Meta:
        model=Project
        # These are the fields in the Task class that will be sent via json
        fields=['id','nombre']

# CompanySerializer class is used to send the data corresponding to the Company class in models.py in a json format
class CompanySerializer (serializers.ModelSerializer):
    class Meta:
        model=Company
        # These are the fields in the Task class that will be sent via json
        fields=['id','nombre','billinginfo']

# BillingInfoSerializer class is used to send the data corresponding to the BillingInfo class in models.py in a json format
class BillingInfoSerializer (serializers.ModelSerializer):
    class Meta:
        model=BillingInfo
        # These are the fields in the Task class that will be sent via json
        fields=['id','cif','street','postal_code','country','creditcard_number']