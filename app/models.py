from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)

class Relation(models.Model):
    from = models.ForeignKey(Persons)
    to = models.ForeignKey(Persons)
    description = models.CharField(max_length=256)