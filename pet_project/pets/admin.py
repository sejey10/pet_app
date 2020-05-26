from django.contrib import admin
from .models import Owner, Pet, PetOwner, Species



admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(PetOwner)
admin.site.register(Species)