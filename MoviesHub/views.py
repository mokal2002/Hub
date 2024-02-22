from django.shortcuts import get_object_or_404, render, HttpResponse
from MoviesHub.models import *
from django.contrib import messages
import logging
from django.core.paginator import Paginator

from .forms import SearchForm
# Create your views here.
def Home(request):
    movies = MovieCard.objects.order_by('-pub_date')
    paginator = Paginator(movies, 12) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.order_by('cat_name')

    context = {
        'movies' : page_obj,
        'categories': categories,
        'page_obj': page_obj       
    }
    return render(request, "home.html" ,context)

def moviesView(request, myid):
    moviesview = MovieCard.objects.filter(id=myid)
    categories = Category.objects.order_by('cat_name')
    return render(request, "movieView.html", {'moviesview':moviesview[0], 'categories': categories})


def category(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    categories = Category.objects.order_by('cat_name')
    
    
    moviescards = category.moviecard_set.order_by('-pub_date')
    paginator = Paginator(moviescards, 12) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    
 
    context = {
		'category' : category,
		'moviescards' : page_obj,
        'categories' : categories,
        'page_obj': page_obj,
        'categories' : categories,
		}

    return render(request, 'category.html',context)


def MovieRequest(request):
    if request.method == "POST":
        request_name = request.POST.get('rname', '')
        email = request.POST.get('remail', '')
        message = request.POST.get('rmessage', '')

        if len(request_name) < 2 or len(email) < 3 or len(message) < 4:
            messages.error(request, "Please fill the form correctly.")
        else:
            request_obj = Request(request_name=request_name, email=email, message=message)
            request_obj.save()
            messages.success(request, "Your message has been submitted.")

    return render(request, "request.html")


# def search(request):
#     query = request.GET['query']
#     if len(query)>78:
#         products = []
#     else:
#         MovieName = MovieCard.objects.filter(name__icontains=query)
#         MovieDesc = MovieCard.objects.filter(desc__icontains=query)
#         # productsCat = Product.objects.filter(category__icontains=query)
#         Movies =  MovieName.union(MovieDesc)
       


#     # if products.count() == 0:
#     #     messages.error(request, "Please Search Correctly")
#     context = {
#         'Movies': Movies,
#         'query' : query
#     }    
#     return render(request, 'search.html', context)


def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = MovieCard.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'form': form, 'results': results})



def disclaimer(request):
    return render(request, 'disclaimer.html')