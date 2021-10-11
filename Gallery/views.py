import datetime as dt
from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import Author, Images, Category, Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def pics(request):
    category = Category.get_categories()
    pictures = Images.all_pics()
    location_pics = Location.get_location()

    return render(request,'allpics.html',{'pictures': pictures, 'category': category, 'location_pics':location_pics })




def single_pic(request,id):
    try:
        pic = Images.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"single_pic.html", {"pic":pic})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_pics = Images.search_by_name(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{"message":message,"image":searched_pics})

    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})


def viewPics_by_location(request,location):
    locationpic = Images.view_pictures_by_location(location)
    return render(request,"location_pics.html",{"locationpic":locationpic})

def viewPics_by_category(request,category):
    photos =Images.view_pictures_by_category(category)
    return render (request,'category.html',{"photos":photos})
