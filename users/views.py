from email import message
from django.shortcuts import render, redirect, get_object_or_404
from recipes.forms import RecipeForm
from recipes.models import Recipe
from users.models import Cook, Skill
from .forms import CustomCreationgForm, SkillForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('cooks')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not excist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('cooks')    
    
    
    return render(request, 'users/login_register.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')



def register_user(request):
    page = 'register'
    form = CustomCreationgForm
    
    if request.method == 'POST':
        form = CustomCreationgForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'User was created')
            
            login(request, user)
            return redirect('cooks')
        else:
            messages.error(request, 'Error during registration')
            
    context = {'page': page, 'form':form}
    return render(request, 'users/login_register.html', context)





# Excisting users = cooks
def cooks(request):
    cooks = Cook.objects.all()
    context = {'cooks':cooks}
    return render(request, 'users/cooks.html', context)

def single_cook(request, pk):
    cook = Cook.objects.get(id=pk)
    recipes = Recipe.objects.filter(owner=cook)
    
    top_skills = Skill.objects.exclude(description__exact='')
    other_skills = Skill.objects.filter(description__exact='')
    
    context = {'cook':cook, 'recipes': recipes, 'top_skills': top_skills, 'other_skills': other_skills}
    return render(request, 'users/single-cook.html', context)


@login_required(login_url='login')
def account(request):
    account = request.user.cook
    skills = account.skill_set.all()
    recipes = account.recipe_set.all().order_by('-created')
    context = {'account': account, 'skills':skills, 'recipes':recipes}
    return render(request, 'users/account.html', context)



@login_required(login_url='login')
def add_skill(request):
    page = 'add'
    cook = request.user.cook
    form = SkillForm()
    
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = cook
            form.save()
            
            return redirect('account')    
        
    context = {'form': form, 'page': page}
        
    return render(request, 'users/add-skill.html', context)

@login_required(login_url="login")
def update_skill(request, pk):
    page = 'skill-edit'
    cook = request.user.cook
    recipe = cook.skill_set.get(id=pk)
    form = SkillForm(instance = recipe)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance = recipe)    
        if form.is_valid():
            recipe = form.save()
            return redirect('account')
    
    context = {'form': form, 'page': page, 'recipe':recipe}
    return render(request, 'recipes/recipe_form.html', context)



@login_required(login_url="login")
def delete_skill(request, pk):
    cook = request.user.cook
    recipe = cook.skill_set.get(id = pk)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('account')
    context = {'object': recipe}
    return render(request, 'delete.html', context) 




def inbox(request):
    return render(request, 'users/inbox.html')