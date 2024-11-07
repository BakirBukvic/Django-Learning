from django.http import HttpResponse
from django.shortcuts import render
from .models import item
from django.template import loader
from .forms import ItemForm
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    
    
    items = item.objects.all()
    context = {
        'items':items,

    }
    return render(request,'food/index.html',context)


class IndexClassView(ListView):
    model = item
    template_name='food/index.html'
    context_object_name='items'





def detail(request,item_id):
    item_id = item.objects.get(pk=item_id)

   
    context = {
        'item': item_id
    }
    return render (request,'food/details.html',context)

class FoodDetail(DetailView):
    model = item
    template_name = 'food/details.html'
    


def add_item(request):

    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/add-item.html', {'form':form})


class CreateItem (CreateView):
    model  = item
    fields = ['item_name','item_desc',"item_price","image_url"]
    template_name = 'food/add-item.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
    


def update(request,id):

    some_item = item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance = some_item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render (request, 'food/add-item.html', {'item':some_item, 'form':form})


def delete(request, id):
    some_item = item.objects.get(id=id)
    if request.method == 'POST':
        some_item.delete()
        return redirect ('food:index')
    return render(request,'food/item-delete.html', {'item':some_item})


    