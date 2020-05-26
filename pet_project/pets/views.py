from django.shortcuts import render, redirect
from .forms import AddOwnerForm, AddPetForm, AddPetOwnerForm, AddSpeciesForm
from .models import Owner, Pet, PetOwner, Species


def home(request):
    template_name = 'home.html'
    return render(request, template_name, context=None)

############################### OWNERS ##########################################

# ADD OWNER

def add_owner(request):
    template_name = 'owners/add_owner.html'
    form = AddOwnerForm()
    if request.method == 'POST':
        form = AddOwnerForm(request.POST)
        form.save()
        return redirect(home)
        print(form)
    print('Failed to submit')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)



# SHOW ALL OWNERS
def show_owners(request):
    template_name = 'owners/all_owners.html'
    owners = Owner.objects.all()
    context = {
        'owners': owners
    }
    return render(request, template_name, context)

# SHOW OWNER DETAIL/UPDATE NA DIN
def owner_detail(request, id):
    template_name = 'owners/owner_detail.html'
    specific_owner = Owner.objects.get(id=id)
    form = AddOwnerForm(request.POST or None, instance=specific_owner)
    if  form.is_valid():
        form.save()
        return redirect(show_owners)
    print('Failed to submit')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)

# DELETE OWNER
def owner_delete(request, id):
    template_name = 'owners/owner_deleted.html'
    specific_owner = Owner.objects.get(id=id)
    specific_owner.delete()
    return redirect(home)

######################################### PETS ################################################
def add_pet(request):
    template_name = 'pets/add_pet.html'
    form = AddPetForm()
    if request.method == 'POST':
        form = AddPetForm(request.POST)
        form.save()
        return redirect(home)
        print(form)
    print('Failed to submit')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)

# SHOW ALL PETS
def show_pets(request):
    template_name = 'pets/all_pets.html'
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }
    return render(request, template_name, context)


# SHOW PET DETAIL
def pet_detail(request, id):
    template_name = 'pets/pet_detail.html'
    specific_pet = Pet.objects.get(id=id)
    context = {
        'specific_pet': specific_pet
    }
    return render(request, template_name, context=context)

# EDIT PET DETAIL
def edit_pet(request, id):
    template_name = 'pets/edit_pet.html'
    specific_pet = Pet.objects.get(id=id)
    form = AddPetForm(request.POST or None, instance=specific_pet)
    if  form.is_valid():
        form.save()
        return redirect(show_pets)
    print('Failed to submit')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)


# DELETE PET
def delete_pet(request, id):
    template_name = 'pets/delete_pet.html'
    specific_pet = Pet.objects.get(id=id)
    specific_pet.delete()
    return render(request, template_name, context=None)

######################################### SPECIES ################################################
# ADD SPECIES
def add_species(request):
    template_name = 'species/add_species.html'
    form = AddSpeciesForm()
    if request.method == 'POST':
        form = AddSpeciesForm(request.POST)
        form.save()
        return redirect(home)
        print(form)
    print('Failed to submit')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)

# SHOW SPECIES
def show_species(request):
    template_name = 'species/all_species.html'
    species = Species.objects.all()
    context = {
        'species': species
    }
    return render(request, template_name, context)

# DITO NYO NLANG LAGAY YUNG EDIT SPECIES AND DELETE IF YOU WANT
# def delete_species tsaka def_update_species


######################################### ASSIGNING OWNERS ################################################

# ASSIGN OWNER
def assign_owner(request):
    template_name = 'assign_owner.html'
    form = AddPetOwnerForm()
    if request.method == 'POST':
        form = AddPetOwnerForm(request.POST)
        form.save()
        return redirect(home)
        print(form)
    print('Failed to submit')
    context = {
        'form': form
    }
    return render(request, template_name, context)


# SHOW ALL PETS OWNED BY OWNERS
def owners_with_pets(request):
    template_name = 'owners_with_pets.html'
    pets_owned = PetOwner.objects.all()
    context = {
        'pets_owned': pets_owned
    }
    return render(request, template_name, context)