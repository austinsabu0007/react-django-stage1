from django.shortcuts import render
from rest_framework import generics
from .serializers import PersonSerializer
from .models import Person

class PersonView(generics.CreateAPIView):
    queryset= Person.objects.all()
    serializer_class = PersonSerializer
def front(request):
    context = { }
    return render(request, "index.html", context)