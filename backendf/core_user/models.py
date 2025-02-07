from django.db import models

# user/models.py
class Geo(models.Model):
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    def __str__(self):
        return f"Lat: {self.lat}, Lng: {self.lng}"


class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return f"{self.street}, {self.city}"


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='user')
    phone = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.name
