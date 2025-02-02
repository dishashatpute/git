from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SIZE_CHOICES=(
    ('s','small'),
    ('m','medium'),
    ('l','Large'),
    ('xl','Extra large'),
    ('xxl','Double extra large'),
    
)

CATEGORY_CHOICES=(
     ('mu','mens upper wear'),
     ('mb','mens bottom wear'),
     ('wu','Womens upper wear'),
     ('wb','Womens bottom wear'),  
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=3)
    size=models.CharField(choices=SIZE_CHOICES,max_length=3)
    product_image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    
# name root email root@gmail.com password 123456

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    pincode=models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES =(
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)

class Payment (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount= models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
        product=models.ForeignKey(Product, on_delete=models. CASCADE)
        quantity=models.PositiveBigIntegerField(default=1)
        ordered_date=models.DateTimeField(auto_now_add=True)
        status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
        payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
        @property
        def total_cost(self):
            return self.quantity * self.product.discounted_price