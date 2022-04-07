from django.db import models

# Create your models here.
from django.db import models
from django.db import connections

# Create your models here.
#USER DETAILS DATABASE
class User(models.Model):
    username = models.CharField(max_length=100,unique =True,blank = False)
    password = models.CharField(max_length=100,blank = False)
    emailadd = models.CharField(max_length=100, unique = True,blank = False)
    fname = models.CharField(max_length=50,blank = False)
    lname = models.CharField(max_length=50,blank = False)
    address = models.CharField(max_length=50,blank = False)
    contactNum = models.CharField(max_length=50, default = False,blank = False)
#USER ROOM DETAILS DATABASE
class Room(models.Model):
    slot = models.CharField(max_length=50,blank = False, unique=False)
    roomtype = models.CharField(max_length=50)
    dateofuse = models.DateField(max_length=50,blank=True, null=True,default='')
    username = models.ForeignKey(User,to_field='username', related_name='username+', on_delete=models.CASCADE)
    class meta:
        db_table = 'nameless_room'
class RoomReservation(models.Model):
    roomnumber = models.CharField(max_length=50, unique = True)
    roomtype = models.CharField(max_length=50)
    dateofuse = models.CharField(max_length=50)
    timeuse = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    emailadd = models.CharField(max_length=50)
    contactNum = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    class meta:
        db_table = 'nameless_roomreservation'
#ADMIN ADD ROOM DETAILS DATABASE
class AddRoom(models.Model):
    roomnumber = models.CharField(max_length=50, unique = True)
    roomtype = models.CharField(max_length=50)
    class meta:
        db_table = 'nameless_addroom'
class Admin(models.Model):
    username = models.CharField(max_length=100,unique =True,blank = False)
    password = models.CharField(max_length=100,blank = False)
    emailadd = models.CharField(max_length=100, unique = True,blank = False)
    fname = models.CharField(max_length=50,blank = False)
    lname = models.CharField(max_length=50,blank = False)
    address = models.CharField(max_length=50,blank = False)
    contactNum = models.CharField(max_length=50, default = False,blank = False)

