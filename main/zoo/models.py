from django.db import models
from django.utils import timezone

from .name_generator import generate_name



class Zoo(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50, default=generate_name())

    def __str__(self):
        return self.name

    def number_of_cages(self):
        """Return the number of cages in the zoo."""
        return len(Cage.objects.filter(zoo_id=self.id))

    def add_cage(self, name=None):
        """Cage objects are added to a Zoo's cages list."""
        cage = Cage(name)
        Cage.objects.create()
        return cage


class Cage(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50, default=generate_name())
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE, related_name='cages')

    def __str__(self):
        return self.name


class BaseAnimal(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50, default=generate_name())
    cage = models.ForeignKey(Cage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name