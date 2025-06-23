from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
            return self.name

    def __repr__(self):
            return f"Country(name={self.name})"


class City(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")
    zip_code = models.CharField(max_length=50, unique=True, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"City(name={self.name}, country={self.country}, zip_code={self.zip_code})"


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="locations")
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)

    class Meta:
        ordering = ['city__name', 'name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Location(name={self.name}, city={self.city}, latitude={self.latitude}, longitude={self.longitude})"


class Event(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="events")
    owner_of_event = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")

    class Meta:
        ordering = [ 'start_date', 'name',]

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f"Event(name={self.name}, description={self.description},"
                f" start_date={self.start_date}, end_date={self.end_date},"
                f" location={self.location}, owner_of_event={self.owner_of_event})")


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.content

    def __repr__(self):
        return (f"Comment(event={self.event}, user={self.user}, content={self.content},"
                f" date_posted={self.date_posted})")