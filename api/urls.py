
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='tasks'), #GET y POST
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'), #GET, PUT, DELETE

    path('tags/', views.tag_list, name='tags'), #GET y POST
    path('tags/<int:pk>/', views.tag_detail, name='tag_detail'), #GET, PUT, DELETE

    path('users/', views.user_list, name='users'), #GET y POST
    path('users/<int:pk>/', views.user_detail, name='user_detail'), #GET, PUT, DELETE

    path('projects/', views.project_list, name='projects'), #GET y POST
    path('projects/<int:pk>/', views.project_detail, name='project_detail'), #GET, PUT, DELETE

    path('companies/', views.company_list, name='companies'), #GET y POST
    path('companies/<int:pk>/', views.company_detail, name='company_detail'), #GET, PUT, DELETE

    path('billinginfos/', views.billinginfo_list, name='billinginfos'), #GET y POST
    path('billinginfos/<int:pk>/', views.billinginfo_detail, name='billinginfo_detail') #GET, PUT, DELETE

]
