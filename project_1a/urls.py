"""
URL configuration for project_1a project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from project_1a_app import views

# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# # router.register('emplist',views.Emplist,basename='empdata')
# router.register('empviewsets',views.Empviewsets,basename='emp')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('project_1a_app.urls')),
    # path('list/',views.Emplist.as_view()),
    # path('post/',views.Emppost.as_view()),
    # path('dis/<int:pk>/',views.Empdis.as_view()), #note: <int:id> not support
    # path('put/<int:pk>/',views.Empput.as_view()),
    # path('delete/<int:pk>/',views.Empdelete.as_view()),
    # path('lc/',views.Emplc.as_view()),
    # path('rud/<int:pk>/',views.Emprud.as_view()),
## concrete generic view class urls
    # path('emplist/',views.Emplist.as_view()),
    # path('emppost/',views.Emppost.as_view()),
    # path('emplc/',views.Emplc.as_view()),
    # path('empdis/<int:pk>/',views.Emprec.as_view()),
    # path('emprud/<int:pk>/',views.Emprud.as_view()),

    #path('',include(router.urls)),
    path('apilist/',views.apiviewlist.as_view()),
    path('apiurd/<int:id>/',views.apiviewurd.as_view()),
]
