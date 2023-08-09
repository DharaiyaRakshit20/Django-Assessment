from django.shortcuts import render
from .models import form
import datetime
from rest_framework.decorators import api_view
from .serializers import formSerializer
from rest_framework.response import Response
# Create your views here.


def home(request):
    if request.method == "POST":
        form.objects.create(
            Blog=request.POST["blog"],
            Contant=request.POST["contant"],
            Create=datetime.datetime.now(),
            Update=datetime.datetime.now()
        )
        return render(request, "from.html", {"msg": "Data Added."})
    else:
        return render(request, 'from.html')


@api_view(['GET'])
def all_data(request):
    data=form.objects.all()
    serial=formSerializer(data,many=True)
    return Response(serial.data)

@api_view(['GET'])
def one_data(request,pk):
    ony_data=form.objects.get(id=pk)
    serial=formSerializer(ony_data)
    return Response(serial.data)

@api_view(['GET'])
def update(request,pk,B,C):
    try:
        one_data=form.objects.get(id=pk)
        one_data.Blog=B
        one_data.Contant=C
        one_data.save()

    except:
        form.objects.create(
            Blog=B,
            Contant=C
        )
    data=form.objects.all()
    serial=formSerializer(data,many=True)
    return Response(serial.data)

@api_view(['GET'])
def delete(request,pk):
    one_delete=form.objects.get(id=pk)
    one_delete.delete()
    one_delete.save()
    serial=formSerializer(one_delete,many=True)
    return Response(serial.data)