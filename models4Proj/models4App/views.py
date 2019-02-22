from django.shortcuts import render

from django.http import HttpResponse
from .models import Mom
from .models import Child

# Create your views here.

# TEST
def index(request):
    return HttpResponse("test")

# LISTS MOM AND CHILD
def momChild(request):
    mothers = Mom.objects.all()
    for prnt in mothers:
        print(f'{prnt.mom_first_name} {prnt.mom_last_name}')
        for kid in Child.objects.filter(child_mom__mom_first_name=prnt.mom_first_name):
            print(kid.child_first_name)
    return HttpResponse ()



# LISTS CHILD AND MOM
def allChild(request):
    kids = Child.objects.all()
    for littles in kids:
        print(f'{littles.child_first_name} {littles.child_last_name}')
        print(littles.child_mom)

    return HttpResponse ()



# # ADDS CHILD TO EACH MOM ---couldnt figure out :(
# def addChild(request):
# #     newChild = Mom[0](child_first_name = 'jack', child_last_name= 'benimble')
#     return HttpResponse ("test")
# #

# # # DELETES FIRST MOM
def deleteMom(request):
    deleteThis = Mom.objects.all()[0]
    deleteThis.delete()
    print(Mom.objects.all())



    return HttpResponse ("delete")
