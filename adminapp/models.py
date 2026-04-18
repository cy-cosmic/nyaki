from django.db import models


# Create your models here.
class BaseUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ForestRidgeHome(BaseUpload):
    description = models.CharField(max_length=100, default="Forest Ridge Dr SE")


class RStreetHome(BaseUpload):
    description = models.CharField(max_length=100, default="R Street NE")


class FoodAndActivities(BaseUpload):
    description = models.CharField(max_length=100, default="Food & Activities")
