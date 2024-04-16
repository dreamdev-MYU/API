from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    photo = models.ImageField(upload_to='product_image/', blank=False,null=False)
    company_made = models.CharField(max_length=300, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
