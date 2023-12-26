from django.db import models


# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=300, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Home'


class Shop(models.Model):
    chair_name = models.CharField(max_length=55, blank=True)
    chair_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    chair_photo = models.ImageField(upload_to='images/', blank=True)
    is_visible = models.BooleanField(default=True)


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'AboutUs'


class OurTeam(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Testimonials(models.Model):
    text = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=400, blank=True)
    body = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='blog_images/', blank=True)
    is_visible = models.BooleanField(default=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    message = models.TextField(max_length=300, blank=True)
    is_precessed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.email}'

    class Meta:
        verbose_name_plural = 'ContactForm'
        ordering = ('-created_at',)
