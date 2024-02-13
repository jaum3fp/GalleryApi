from django.db.models import Model, CharField, ImageField

# Create your models here.


class Artwork(Model):
    title = CharField(max_length=50)
    author = CharField(max_length=50)
    image = ImageField(default=None, upload_to="images/")