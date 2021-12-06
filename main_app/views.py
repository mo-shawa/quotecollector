from django.shortcuts import render
from .models import Quote

# class Quote:
#     def __init__(self,author,quote):
#         self.author = author
#         self.quote = quote
    

# quotes = [
#     Quote('Kendrick Lamar', "I always thought it was me against the world, and then one day I realized it's just me against me."),
#     Quote('Unknown', 'Hard times create strong men. Strong men create easy times. Easy times create weak men. Weak men create hard times.'),
#     Quote('Unknown', 'When you have something to say, silence is a lie.'),
#     Quote('David Goggins', "WHO'S GONNA CARRY THE BOATS"),
# ]

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html' )

def quotes_index(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', {'quotes': quotes})

def quotes_detail(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    return render(request,'quotes/detail.html',{'quote': quote
    })
