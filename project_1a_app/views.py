# from django.shortcuts import render
#
# from .models import Employee
# from project_1a_app.serialisers import Emp_serialiser
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin
# from .forms import EmpForm

# Create your views here.

# def empview(request):
#     if request.method == "POST":
#         form = EmpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = EmpForm()
#             return render(request, 'basic.html', {'form': form})
#             #return redirect('/show')
#
#
#     form = EmpForm()
#     return render(request, 'basic.html', {'form': form})

# @api_view(["GET"])
# def home(request):
#     eobj=Employee.objects.all()
#     ser=Emp_serialiser(eobj,many=True)
#     return Response(ser.data)
#
# @api_view(["POST"])
# def post(request):
#     eobj=Employee.objects.all()
#     ser=Emp_serialiser(data=request.data)
#     if ser.is_valid():
#         ser.save()
#     return Response(ser.data)
#
# @api_view(["POST"])
# def update(request,id):
#     eobj=Employee.objects.get(id=id)
#     ser=Emp_serialiser(instance=eobj,data=request.data)
#     if ser.is_valid():
#         ser.save()
#     return Response(ser.data)
#
# @api_view(["DELETE"])
# def delete(request,id):
#     eobj=Employee.objects.get(id=id)
#     ser=Emp_serialiser(eobj)
#     return Response(ser.data)

# class Emplist(GenericAPIView,ListModelMixin):
#     eobj = Employee.objects.all()
#     serializer_class = Emp_serialiser
#
#     def get(self,request):
#         return self.list(request)

#========================================================================

# from django.shortcuts import render
#
# from .models import Employee
# from project_1a_app.serialisers import Emp_serialiser
#
# # from rest_framework.response import Response
#
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
#
# class Emplist(GenericAPIView,ListModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#     def get(self,request):
#         return self.list(request)
#
# ##CreateModelMixin
# class Emppost(GenericAPIView,CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#     def post(self,request):
#         return self.create(request)
#
# ##RetrieveModelMixin
# class Empdis(GenericAPIView,RetrieveModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#     def get(self,request,**kwargs):
#         return self.retrieve(request,**kwargs)
#
# ##UpdateModelMixin
# class Empput(GenericAPIView,UpdateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#     def put(self,request,**kwargs):
#         return self.update(request,**kwargs)
#
#
# ##DestroyModelMixin
# class Empdelete(GenericAPIView,DestroyModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#     def delete(self,request,**kwargs):
#         return self.destroy(request,**kwargs)
#
#
# ##ListCreateModelMixin
# ##LisModelMixin
# class Emplc(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#
# ##RetrieveModelMixin,UpdateModelMixin.DestroyModelMixin
# class Emprud(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#     def get(self,request,**kwargs):
#         return self.retrieve(request,**kwargs)
#
#     def put(self,request,**kwargs):
#         return self.update(request,**kwargs)
#
#     def delete(self,request,**kwargs):
#         return self.destroy(request,**kwargs)


##=====================================================================

# concrete generic view class

#==========================================

# from django.shortcuts import render
# from .models import Employee
# from project_1a_app.serialisers import Emp_serialiser
# from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
#
# class Emplist(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#
# class Emppost(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#
# class Emplc(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#
#
# class Emprec(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser
#
# class Emprud(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = Emp_serialiser

#=====================================================

#viewsets

#===========================

# from django.shortcuts import render
# from .models import Employee
# from project_1a_app.serialisers import Emp_serialiser
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import viewsets
#
# class Emplist(viewsets.ViewSet):
#     def list(self,request):
#         eobj=Employee.objects.all()
#         serialiser=Emp_serialiser(eobj,many=True)
#         return Response(serialiser.data)
#
#     def create(self,request):
#         eobj=Employee.objects.all()
#         serialiser=Emp_serialiser(data=request.data)
#         if serialiser.is_valid():
#             return Response(serialiser.data)
#         return 'post error'
#
#     def retrieve(self,request,pk):
#         eobj=Employee.objects.get(pk=pk)
#         serialiser=Emp_serialiser(eobj)
#         return Response(serialiser.data)
#
#
#     def update(self,request,pk):
#         eobj=Employee.objects.get(pk=pk)
#         serialiser=Emp_serialiser(instance=eobj,data=request.data)
#         if serialiser.is_valid():
#             return Response(serialiser.data)
#         return 'error'
#
#     def delete(self,request,pk):
#         eobj=Employee.objects.get(pk=pk)
#         eobj.delete()
#         serialiser=Emp_serialiser(eobj)
#         return Response(serialiser.data)


#==============================================================

# Model View Sets

#==============================================================

from django.shortcuts import render
from .models import Employee
from project_1a_app.serialisers import Emp_serialiser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class Empviewsets(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class = Emp_serialiser


#===================================================

#Authentication & permission

#============================================================================

from django.shortcuts import render
from .models import Employee
from project_1a_app.serialisers import Emp_serialiser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Empviewsets(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class = Emp_serialiser
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
