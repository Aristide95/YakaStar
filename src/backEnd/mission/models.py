from django.db import models
from django.utils import timezone

class Mission(models.Model):
        title = models.CharField(max_length = 64)
        desc = models.TextField()
        type_mission = models.CharField(max_length = 64)
        state = models.IntegerField(default = 0)
        creation_date = models.DateTimeField(default = timezone.now)
        publication_date = models.DateTimeField(null=True)
        commercial_id = models.ForeignKey('Etudiant', on_delete=models.CASCADE)
        client_name = models.CharField(max_length = 64)
        logo_url = models.URLField(null=True)
        devis_url = models.URLField(null=True)
        techno = models.ManyToManyField('Techno')
        num_presta = models.IntegerField(default = 1)

        def __str__(self):
                return self.title

class Techno(models.Model):
        name = models.CharField(max_length = 64)

        def __str__(self):
                return self.name

class Etudiant(models.Model):
        firstname = models.CharField(max_length = 64)
        lastname = models.CharField(max_length = 64)
        email = models.EmailField(max_length = 64)
        status = models.CharField(max_length = 64)
        cv_url = models.URLField(null=True)
        creation_date = models.DateTimeField(default = timezone.now)

        def __str__(self):
                return self.firstname

class Calendrier(models.Model):
        title = models.CharField(max_length = 64)
        start = models.DateTimeField(default = timezone.now)
        end = models.DateTimeField(default = timezone.now)

        def __str__(self):
                return str(self.date)

class UserLogin(models.Model):
        login = models.CharField(max_length = 64)
        password = models.CharField(max_length = 64)
