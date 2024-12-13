from django.db import models
from django.contrib.auth.models import User


# Pet Profile Model for Adoption
class Pet(models.Model):
    objects = None
    owner = models.ForeignKey(User, related_name='pets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    is_available_for_adoption = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='pets/', null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.breed}"


# Care-Giver Profile Model
class CareGiver(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='caregiver_profile')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    bio = models.TextField()
    photo = models.ImageField(upload_to='caregivers/', null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.full_name

