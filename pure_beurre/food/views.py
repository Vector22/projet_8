from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import render, redirect
import json

from .forms import SignUpForm, ResearchForm
from .models import Category, Food, MyFood

# Create your views here.


def home(request):
    """ show the home page """

    if request.method == 'POST':
        form = ResearchForm(request.POST or None)
        if form.is_valid():
            searchedFood = form.cleaned_data['search']
            return redirect('result', searchedFood=searchedFood)
    else:
        form = ResearchForm()
    return render(request, 'food/index.html', {'form': form})


def result(request, searchedFood):
    """ The search result page """

    if request.method == 'POST':
        form = ResearchForm(request.POST or None)
        if form.is_valid():
            searchedFood = form.cleaned_data['search']
            return redirect('result', searchedFood=searchedFood)
    else:
        form = ResearchForm()

    food = Food.objects.filter(nameFr__contains=str(searchedFood))[0]
    temp = food.category.food_set.all()
    foodSubtituts = temp.exclude(id=food.id).order_by('nutritionGrade')

    return render(request, 'food/result.html', locals())


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'food/registration/signup.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse(home))


def all_foods(request):
    foods = Food.objects.all()
    total = Food.objects.count()
    return render(request, 'food/all_foods.html', locals())


def test(request):
    return render(request, 'food/test.html')
