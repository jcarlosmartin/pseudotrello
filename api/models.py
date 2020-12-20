from django.db import models

# Tag class is used to describe a specific status of the task, these are typically new, to-do, in-progress, done and urgent
class Tag(models.Model):
    #Individuals
    estado=models.CharField(max_length=50)

    class Meta:
        db_table='tag'
        ordering=['id']

# BillingInfo class is used to describe the billing information of the Company where the users work
class BillingInfo(models.Model):
    #Individuals
    cif=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=20)
    creditcard_number=models.IntegerField()

    class Meta:
        db_table='billinginfo'
        ordering=['cif']

# Project class is used to describe the project name a user is assigned to
class Project(models.Model):
    #Individuals
    nombre=models.CharField(max_length=60)

    class Meta:
        db_table='project'
        ordering=['nombre']

''' 
Company class is used to describe the name of the Company a user works in. Company class has one realtion:
A company have one billing information and a billing information can own only to a company.
'''
class Company(models.Model):
    #Individuals
    nombre=models.CharField(max_length=50)
    billinginfo=models.OneToOneField(BillingInfo, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table='company'
        ordering=['nombre']

'''
User class is used to describe the name, company and projects of a user. User class has two relations:
- A user works in a single company and a company can have multiple users working on it.
- A user can have multiple projects and a project can have multiple users.
'''
class User(models.Model):
    #Individuals
    nombre=models.CharField(max_length=50)
    # Relations
    company=models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    projects=models.ManyToManyField(Project, null=True)

    class Meta:
        db_table='user'
        ordering=['nombre']

'''
Task class is used to describe the task or activity that need to the performed in the context of a full project
Task class has several relations:
- A task can have multiple tags, and a tag can have several tasks
- A task can be assigned to a single user, and a user can be assigned to several tasks
- A task belongs to a single project, and a project can have several tasks
'''
class Task(models.Model):
    #Individuals
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    #Relations
    tags=models.ManyToManyField(Tag)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project=models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
     
    class Meta:
        db_table = 'task'
        ordering = ['nombre']

