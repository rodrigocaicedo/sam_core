from django.shortcuts import render, redirect
from capellania_sam.forms import InformeGeneralForm


def CreateInformeGeneral(request):
#    context = RequestContext(request)
    if request.method == "POST":
        form = InformeGeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://www.google.com")
        else:
            print form.errors
            return render(request, "capellania_sam/prueba.txt", {"form":form})
    else:
        form = InformeGeneralForm()
        return render(request, "capellania_sam/prueba.txt", {"form":form})
# Create your views here.




# Create your views here.
