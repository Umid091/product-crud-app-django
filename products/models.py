from django.db import models


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)       # Mahsulot nomi
    category = models.CharField(max_length=100)   # Kategoriya
    price = models.DecimalField(max_digits=10, decimal_places=2) # Narxi
    quantity = models.IntegerField(default=0)     # Soni
    created_at = models.DateTimeField(auto_now_add=True) # Qo'shilgan vaqti

    def __str__(self):
        return f"{self.name} | {self.category}"


