from django.shortcuts import render


def showIndex(request):
    return render(request, "index.html")


def registration(request):
    pno = request.POST.get('no')
    nm = request.POST.get('na')
    prc = request.POST.get('prc')
    qty = request.POST.get('pqty')

    from app.models import Product
    p1 = Product(number=pno, name=nm, price=prc, quantity=qty)
    p1.save()
    d1 = {'message': "data saved"}
    return render(request, "index.html", d1)
