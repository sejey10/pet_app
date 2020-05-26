from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    ############################## OWNERS URLS ##############################
    path('add_owner/', views.add_owner, name='add_owner'),
    path('show_owners/', views.show_owners, name='show_owners'),
    path('owner_detail/<int:id>', views.owner_detail, name='owner_detail'),
    path('owner_delete/<int:id>', views.owner_delete, name='owner_delete'),

    ############################## PETS URLS ##############################
    path('add_pet/', views.add_pet, name='add_pet'),
    path('show_pets/', views.show_pets, name='show_pets'),
    path('pet_detail/<int:id>', views.pet_detail, name='pet_detail'),
    path('edit_pet/<int:id>', views.edit_pet, name='edit_pet'),
    path('delete_pet/<int:id>', views.delete_pet, name='delete_pet'),
    path('add_species/', views.add_species, name='add_species'),

    ############################## SPECIES URLS ##############################
    path('show_species/', views.show_species, name='show_species'),
    

    ############################## ASSIGN OWNERS URLS ##############################
    path('assign_owner/', views.assign_owner, name='assign_owner'),
    path('owners_with_pets/', views.owners_with_pets, name='owners_with_pets')
]
