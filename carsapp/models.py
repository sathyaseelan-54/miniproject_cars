from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100 )
    phone = models.CharField( max_length = 10,null = False,blank = False,unique = True)
    model = models.CharField(max_length = 100)
    departuredate = models.DateTimeField()
    returndate = models.DateTimeField()

    def __str__(self):
        return self.name

class Contact(models.Model):

    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    message = models.TextField()

    def __str__(self):
        return self.first_name


