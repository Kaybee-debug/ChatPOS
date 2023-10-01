from django.shortcuts import render
from .models import Business,Product
from .forms import BusinessForm,ProductForm

# Create your views here.
# def bank_list(request):
#     banks = Bank.objects.all()
    
#     context = {
#         "banks": banks
#     }
   
#     return render(request,"view.html",context)

def business_create(request):
    form = BusinessForm()
    if request.method == "POST":
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        "form":form
    }
   
    return render(request,"Business.html",context)

def product_create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        "form":form
    }
   
    return render(request,"product.html",context)

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "view.html", context)
# def product_list(request, business_name_id):
#     business = Business.objects.get(pk=business_name_id)
#     product = Product.objects.filter(business_name=business)
#     return render(request, 'view.html', {'business': business, 'product': product})

# def bank_list(request):
#     banks = Bank.objects.all()
    
#     context = {
#         "banks": banks
#     }
   
#     return render(request,"view.html",context)

# def feature_detail(request, bank_name_id):
#     bank = Bank.objects.get(pk=bank_name_id)
#     features = Features.objects.filter(bank_name=bank)
#     return render(request, 'loanFeatures.html', {'bank': bank, 'features': features})
