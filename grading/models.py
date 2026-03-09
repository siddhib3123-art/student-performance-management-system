from django.db import models


class Student(models.Model):
    roll=models.CharField(max_length=10 ,unique=True)#unique is a key which is unique key through which we can access update or delete related data
    name=models.CharField(max_length=100)
    english=models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    socialscience = models.IntegerField()
    marathi = models.IntegerField()
    total = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.0)
    grade=models.CharField(max_length=10,default="NA")
    def save(self, *args, **kwargs):
        #calculate total
        self.total=(
            self.english + self.maths +self.science + self.socialscience + self.marathi
        )
        #calculate percentage
        self.percentage = self.total/5
    #assigning grade
        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "FAIL"
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.roll} - {self.name}"


