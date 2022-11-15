from django.shortcuts import render

# Create your views here.

b_obj = Books.objects.filter(name_endswtih="a")
print(b_obj)