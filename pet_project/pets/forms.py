from django.forms import ModelForm
from django import forms
from .models import Owner, Pet, Species, PetOwner




class AddOwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


# for date widget (A)
class DateInput(forms.DateInput):
    input_type = 'date'

    
class AddPetForm(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(), # (A) here
        }

    

class AddSpeciesForm(ModelForm):
    class Meta:
        model = Species
        fields = '__all__'
        
class AddPetOwnerForm(ModelForm):
    class Meta:
        model = PetOwner
        fields = '__all__'