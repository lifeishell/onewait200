from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)

class Relation(models.Model):
    from_person = models.ForeignKey(Person, related_name="from")
    to_person = models.ForeignKey(Person, related_name="to")
    description = models.CharField(max_length=256)