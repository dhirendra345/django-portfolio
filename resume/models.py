from django.db import models

class Skill(models.Model):
    category = models.CharField(max_length=100)
    items = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    score = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
