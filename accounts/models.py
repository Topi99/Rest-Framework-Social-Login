from django.db import models

class Account(models.Model):
	token = models.TextField()
