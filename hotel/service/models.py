from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    file = models.FileField(upload_to='uploads/',default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
 
class Addroom(models.Model):
    file = models.FileField(upload_to='uploads/', default='default.jpg',blank=True, null=True)  # use ImageField
    rent = models.DecimalField(max_digits=10, decimal_places=2)             # price as decimal
    roomname = models.CharField(max_length=50)
    roomratting = models.DecimalField(max_digits=5, decimal_places=1)        # e.g. 4.5
    bed = models.PositiveIntegerField()
    bath = models.PositiveIntegerField()
    wifi = models.BooleanField(default=False)
    desc = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def star_range(self):
        return range(int(self.roomratting))