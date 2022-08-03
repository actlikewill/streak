from django.db import models

class Trackable(models.Model):
    """
    Abstract base class for all models that are trackable.
    """
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Streak(models.Model):
    """
    A single event that occurred at a specific time.
    """
    time = models.DateTimeField()
    description = models.TextField()
    trackable = models.ForeignKey(Trackable, on_delete=models.CASCADE)

    def __str__(self):
        return self.trackable.name + ": " + self.time.strftime("%Y-%m-%d %H:%M:%S")
