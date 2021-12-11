from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Quote, Category
from django.views.generic import ListView, CreateView, DeleteView
from .forms import FanForm

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def quotes_index(request):
    quotes = Quote.objects.all()
    return render(request, "quotes/index.html", {"quotes": quotes})


def quotes_detail(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    remaining_cats = Category.objects.exclude(id__in =quote.categories.all().values_list('id'))
    fan_form = FanForm()
    return render(request, "quotes/detail.html", {"quote": quote, "fan_form": fan_form, 'cats' : remaining_cats})


class QuoteCreate(CreateView):
    model = Quote
    fields = "__all__"


class QuoteUpdate(UpdateView):
    model = Quote
    fields = "__all__"


class QuoteDelete(DeleteView):
    model = Quote
    success_url = "/quotes/"

class CatList(ListView):
    model = Category

class CatDetail(DetailView):
    model = Category
    fields = '__all__'

class CatCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/categories/'

def add_fan(request, quote_id):
    form = FanForm(request.POST)
    if form.is_valid():
        new_fan = form.save(commit=False)
        new_fan.quote_id = quote_id
        new_fan.save()
    return redirect("detail", quote_id=quote_id)

def assoc_cat(request,quote_id,cat_id):
    Quote.objects.get(id=quote_id).categories.add(cat_id)
    return redirect('detail', quote_id=quote_id)

