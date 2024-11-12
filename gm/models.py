from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
    photo = models.ImageField(upload_to="r")
    Exe_name = models.CharField(max_length=50)
    Exe_time=models.CharField(max_length=50,default=0)

    def __str__(self)->str:
        return self.Exe_name
    

class Pro(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="r")   
    # name=models.CharField(max_length=50) 
    



class Workout(models.Model):
    name = models.CharField(max_length=100)  # e.g., 'Chest Beginner', 'Leg Beginner'
    duration = models.CharField(max_length=10)  # e.g., '11 MINS'
    exercises = models.IntegerField()  # e.g., 11 exercises
    image = models.ImageField(upload_to='workouts/')  # e.g., image for the workout
    description = models.TextField()  # Optional description if needed

    def __str__(self):
        return self.name

class Exerc(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises_set')  # Link to Workout
    name = models.CharField(max_length=100)  # Exercise name (e.g., 'Push-ups')
    sets = models.IntegerField()  # Number of sets for the exercise
    reps = models.CharField(max_length=50)  # Repetitions or duration (e.g., '12 reps' or '30 seconds')
    image = models.ImageField(upload_to='exercises/')  # Optional image for the exercise (e.g., GIF or JPG)

    def __str__(self):
        return f"{self.name} ({self.workout.name})"
