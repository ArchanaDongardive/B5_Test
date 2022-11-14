from django.db import models

# Create your models here.




class Booklet(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.name


    class Meta:
        db_table = "booklets"    
