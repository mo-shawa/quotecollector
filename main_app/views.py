from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Quote, Category
from django.views.generic import ListView, CreateView, DeleteView
from .forms import FanForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user = form.save()
        login(request,user)
        return redirect('home')
    else:
        error_message = 'invalid signup'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message':error_message}
    return render(request,'registration/signup.html', context)


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

@login_required
def quotes_index(request):
    quotes = Quote.objects.filter(user=request.user)
    return render(request, "quotes/index.html", {"quotes": quotes})

@login_required
def quotes_detail(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    remaining_cats = Category.objects.exclude(id__in =quote.categories.all().values_list('id'))
    fan_form = FanForm()
    return render(request, "quotes/detail.html", {"quote": quote, "fan_form": fan_form, 'cats' : remaining_cats})

class QuoteCreate(LoginRequiredMixin, CreateView):
    model = Quote
    fields = ['quote','author','categories']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuoteUpdate(LoginRequiredMixin, UpdateView):
    model = Quote
    fields = "__all__"

class QuoteDelete(LoginRequiredMixin, DeleteView):
    model = Quote
    success_url = "/quotes/"

class CatList(LoginRequiredMixin, ListView):
    model = Category

class CatDetail(LoginRequiredMixin, DetailView):
    model = Category
    fields = '__all__'

class CatCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    success_url = '/categories/'

@login_required
def add_fan(request, quote_id):
    form = FanForm(request.POST)
    if form.is_valid():
        new_fan = form.save(commit=False)
        new_fan.quote_id = quote_id
        new_fan.save()
    return redirect("detail", quote_id=quote_id)

@login_required
def assoc_cat(request,quote_id,cat_id):
    Quote.objects.get(id=quote_id).categories.add(cat_id)
    return redirect('detail', quote_id=quote_id)

