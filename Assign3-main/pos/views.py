from django.shortcuts import render

from .forms import ScanForm
from .models import Product

def scan_view(request):
    product = None
    msg = " "
    form = ScanForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        code = form.cleaned_data["upc"].strip()
        product = Product.objects.filter(upc=code).first()
        if not product:
            msg = f"No product found for UPC: {code}"
            
    return render(request, "scan.html", {"form": form, "product": product, "msg": msg})       
