from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    mobile = models.CharField(max_length=64)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=64, null=True)
    notes = models.TextField()

    def __str__(self):
        return self.first_name


class Species(models.Model):
    species_name = models.CharField(max_length=255)

    def __str__(self):
        return self.species_name


class Pet(models.Model):
    name = models.CharField(max_length=128)
    species_id = models.ForeignKey(Species, on_delete=models.CASCADE)
    birth_date = models.DateField(auto_now=False,null=True)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.name


class PetOwner(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)


