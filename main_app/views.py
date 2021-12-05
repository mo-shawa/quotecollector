from django.shortcuts import render

class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
    

quotes = [
    Quote('David Goggins', "WHO'S GONNA CARRY THE BOATS AND THE LOGS??"),
    Quote('Kendrick Lamar', "I always thought it was me against the world, and then one day I realized it's just me against me."),
    Quote('Unknown', 'Hard times create strong men. Strong men create easy times. Easy times create weak men. Weak men create hard times.'),
    Quote('Jordan Peterson', 'When you have something to say, silence is a lie.')
]

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html' )

def quotes_index(request):
    return render(request, 'quotes/index.html', {'quotes': quotes})