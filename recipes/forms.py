import imp
from django import forms


from users.models import Cook
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'description', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }        
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            
