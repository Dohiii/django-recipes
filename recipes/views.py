
from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe, Tag
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def recipes(request):
    recipes = Recipe.objects.all().order_by('-created')
    tags = Tag.objects.all()
    context = {'recipes':recipes, 'tags': tags}
    return render(request, 'recipes/recipes.html', context)

def single_recipe(request, pk):
    recipe_object = Recipe.objects.get(id=pk)
    tags = Tag.objects.all()
    context = {'recipe': recipe_object, 'tags': tags}
    return render(request, 'recipes/single-recipe.html', context)

@login_required(login_url="login")
def add_recipe(request):
    page = 'add'
    owner = request.user.cook
    form = RecipeForm()
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = owner
            form.save()
            
            return redirect('account')    
        
    context = {'form': form, 'page': page}
        
    return render(request, 'recipes/recipe_form.html', context)


@login_required(login_url="login")
def update_recipe(request, pk):
    page = 'update'
    cook = request.user.cook
    recipe = cook.recipe_set.get(id = pk)
    form = RecipeForm(instance=recipe)
    
    if request.method == 'POST':       
        form = RecipeForm(request.POST, request.FILES, instance = recipe)
        if form.is_valid():           
            recipe = form.save()
            return redirect('account')
    
    context = {'form':form, 'recipe':recipe}
    return render(request, 'recipes/recipe_form.html', context)

@login_required(login_url="login")
def delete_recipe(request, pk):
    cook = request.user.cook
    recipe = cook.recipe_set.get(id = pk)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('account')
    
    context = {'object': recipe}    
    return render(request, 'delete.html', context) 

    
    