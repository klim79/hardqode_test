from django.contrib.auth.models import User
from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/")
    length = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)


class UserAvailableProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)


class UserProgress(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    watch_time = models.IntegerField()
    watched = models.BooleanField(default=False)



# class UserOption(models.Model):
#     user = models.ForeignKey(UserData, on_delete=models.CASCADE)
#     product = models.ForeignKey(UserData, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Product, on_delete=models.CASCADE)
#     watch_time = models.IntegerField()
#     watched = models.BooleanField(default=False)

# class UserData(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     user = models.ManyToManyField(User)
#     watch_time = models.IntegerField()
#     watched = models.BooleanField(default=False)


# class AddUserInfo(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # user = models.ManyToManyField(Product)
    # lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # watch_time = models.IntegerField()
    # watched = models.BooleanField(default=False)


# class ProductContent(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
