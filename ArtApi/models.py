from django.db.models import Model, CharField, ImageField, TextField

# Create your models here.


class Artwork(Model):
    title = CharField(max_length=50)
    author = CharField(max_length=50)
    image = TextField(max_length=1000)