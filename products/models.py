from django.db import models
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='/assets/images')


class ProductDetails(models.Model):
    PRODUCT_CHOICES = [
        ('BK', 'Books'),
        ('GE', 'Gym Equipments'),
        ('SA', 'Sports Accessories'),
        ('EE', 'Electronics')
    ]
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_path = models.CharField(max_length=100, null=False, blank=False)
    product_type = models.CharField(max_length=2, null=False, blank=False, choices=PRODUCT_CHOICES)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.TextField(null=False, blank=False)
    user = models.ForeignKey('authentication.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)


class ProductForm(ModelForm):
    class Meta:
        model = ProductDetails
        fields = ['product_name', 'product_path', 'product_type', 'price', 'description', 'location', 'user']


class ProductTags(models.Model):
    TAGS = [
        ('MB', 'Motivational Books'),
        ('DB', 'Defence Books'),
        ('CB', 'College Level Books'),
        ('NO', 'Novels')
    ]
    product = models.ForeignKey(
        'ProductDetails', on_delete=models.SET_NULL, blank=True, null=True, related_name='get_product'
    )
    tag = models.CharField(max_length=2, null=False, blank=False, choices=TAGS)

    #returns a RawQuesrySet instance based on the book tag
    @classmethod
    def get_books_by_tags(cls, tag: str):
        return cls.objects.raw("""
            SELECT 
            products_productdetails.id,
            products_productdetails.product_name,
            products_productdetails.price,
            products_productdetails.description,
            products_productdetails.product_path
            FROM products_productdetails 
            RIGHT JOIN products_producttags ON products_productdetails.id=products_producttags.product_id 
            WHERE products_producttags.tag='{}'
       """.format(tag))
