from django.db import models
# Create your models here.

class property(models.Model):
 # BUNGLOW = 'BUNGLOW'
 # ROW_HOUSE = 'ROW_HOUSE'
 # APPARTMENT = 'APPARTMENT'
 prop_option = (('BUNGLOW','BUNGLOW'),('ROW_HOUSE','ROW_HOUSE'),('APPARTMENT','APPARTMENT'))

 # FULLY = 'fully'
 # SEMI = 'semi'
 # NOT = 'not'
 furn_option = (('FULLY','FULLY'),('SEMI','SEMI'),('NOT','NOT'))

 MONTH = 'month'
 YEAR = 'year'
 age_option = ((MONTH,MONTH),(YEAR,YEAR))

 NORTH = 'north'
 SOUTH = 'south'
 EAST = 'east'
 WEST = 'west'
 dir_option = ((NORTH,NORTH),(SOUTH,SOUTH),(EAST,EAST),(WEST,WEST))

 p_name = models.CharField(max_length=20)
 p_address = models.TextField(max_length=20)
 p_area = models.CharField(max_length=20)
 p_type = models.CharField(max_length=15,choices=prop_option,default='APPARTMENT')
 p_furnishingtype = models.CharField(max_length=20,choices=furn_option,default='NOT')
 p_age_type = models.CharField(max_length=20,choices=age_option,default=MONTH)
 p_age = models.PositiveIntegerField()
 p_direction = models.CharField(max_length=20,choices=dir_option)
 p_rentprize = models.PositiveIntegerField()
 a_name = models.CharField(max_length=200)


class Image(models.Model):
 p_image = models.ImageField(upload_to='uploads/')
 proty = models.ForeignKey(property,on_delete=models.CASCADE)


class registration(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=10)
    about = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.PositiveIntegerField()
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)


class MyImage(models.Model):
   image = models.ImageField(upload_to='uploads/')
