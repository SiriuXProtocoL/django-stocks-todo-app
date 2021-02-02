from django.db import models

# Create your models here.

#Step 1: Creating the database, defining the model
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    #to see items in a better way
    def __str__(self):
        return self.item

#step 2: Create a migration
#/usr/bin/python3 /home/siriux/Documents/Project/Django/todo/manage.py makemigrations

#step 3: Push the migration
#/usr/bin/python3 /home/siriux/Documents/Project/Django/todo/manage.py migrate

