from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

