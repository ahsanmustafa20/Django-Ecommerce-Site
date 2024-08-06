from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Products, Order
from django.views import generic
from .forms import OrderForm

from django.core.paginator import Paginator
# Create your views here.

# def index(request):
#     product_objects = Products.objects.all
#     return render(request, 'shop/index.html', {'product_objects': product_objects})

class ProductList(generic.ListView):
    model = Products
    template_name = 'shop/index.html'
    context_object_name = 'product_objects'

    #search code
    def get_queryset(self):
        QuerySet = super().get_queryset()
        item_name = self.request.GET.get('item_name')

        if item_name:
            QuerySet = QuerySet.filter(title__icontains=item_name)
        
        # paginator
        paginator = Paginator(QuerySet, 4)
        page = self.request.GET.get('page')
        QuerySet = paginator.get_page(page)

        return QuerySet
    


# def detail(request,id):
#     product_object = Products.objects.get(id=id)
#     return render(request, 'shop/detail.html', {'product_object': product_object})

class DetailView(generic.DetailView):
    model = Products
    template_name = 'shop/detail.html'
    context_object_name = 'product_object'


# def checkout(request):
#     return render(request, 'shop/checkout.html')

# class CheckoutView(generic.TemplateView):
#     template_name = 'shop/checkout.html'

#     def get_queryset(self):

#         if self.request.method == "post":
#             name = self.request.POST.get('name','')
#             email = self.request.POST.get('email','')
#             address = self.request.POST.get('address','')
#             city = self.request.POST.get('city','')
#             state = self.request.POST.get('state','')
#             zip = self.request.POST.get('zip','')
#             order = Order(name=name, email=email, address=address, city=city,
#                       state=state, zip=zip)
#             order.save()

class CheckoutView(generic.TemplateView):
    template_name = 'shop/checkout.html'

    def get(self, request, *args, **kwargs):
        form = OrderForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print(form.errors)  # Print form errors for debugging
        return render(request, self.template_name, {'form': form})
    
class Success(generic.TemplateView):
    template_name = 'shop/success.html'