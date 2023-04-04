from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(
        max_length=250, verbose_name="دسته بندی", blank=True, null=True)

    def __str__(self):
        return self.title


class Article(models.Model):

    head = models.CharField(
        max_length=250, verbose_name="عنوان", blank=True, null=True)

    description = models.CharField(
        max_length=250, verbose_name="توضیحات ", blank=True, null=True)

    image = models.FileField(verbose_name="Image",
                             upload_to="Media/article", blank=True, null=True)

    date_release = models.DateField(
        verbose_name="تاریخ انتشار", null=False, blank=False, auto_now_add=True)

    tag = models.TextField(max_length=250, null=True,
                           blank=True, verbose_name="تگ")

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __img__(self):
        return self.head


class Comment(models.Model):
    message_body = models.CharField(
        verbose_name="نظرات", blank=True, null=True, max_length=250)

    isActive = models.BooleanField(default=False)

    title = models.CharField(
        max_length=250, verbose_name="عنوان", blank=False, null=False)

    send_date = models.DateField(
        verbose_name="تاریخ انتشار", blank=False, null=False, auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.message_body
