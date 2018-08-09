from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def saveFood(request):
    """ This function perform the task what permit
    to save a food in favorite by the user
    """

    # the variables to return to the client side
    alreadySaved = False
    saved = False

    # recover the data transmitted by the client
    foodId = int(request.POST['foodId'])

    userId = request.user.id  # the user's id
    # verfy if the food has been already saved by the user
    foodSaved = MyFood.objects.filter(userId=userId).exists()
    # if never saved, save it
    if not foodSaved:
        alreadySaved = True
        saved = True
        food = Food.objects.get(id=foodId)  # the concerned food
        # save the food in the db
        favoriteFood = MyFood.objects.create()
        favoriteFood.userId = userId
        favoriteFood.food = food
        favoriteFood.save()

    return json.dumps({'alreadySaved': alreadySaved,
                       'saved': saved})


def test(request):
    return render(request, 'food/test.html')


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


def all_foods(request):
    foods = Food.objects.all()
    total = Food.objects.count()
    return render(request, 'food/all_foods.html', locals())
