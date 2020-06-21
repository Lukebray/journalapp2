from django.db import models

class User(models.Model):
    username = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Journal(models.Model):
    journal_name = models.CharField(max_length=254)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.journal_name

class Entry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField(max_length=10000)
    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

