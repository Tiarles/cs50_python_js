from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # CASCADE: When the referenced object is deleted, also delete the
    # objects that have references to it (when you remove a blog post
    # for instance, you might want to delete comments as well).
    # SQL equivalent: CASCADE.
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    # origin = models.CharField(max_length=64)

    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    # destination = models.CharField(max_length=64)

    duration = models.IntegerField()

    def __str__(self):
        return f"({self.id}) From {self.origin} to {self.destination}: {self.duration} min."
