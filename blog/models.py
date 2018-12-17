from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    summary = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails')
    body = RichTextUploadingField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    last_modified_date = models.DateTimeField(null=True, auto_now=True)
    tag = models.ManyToManyField('Tag')
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def display_tag(self):
        return ', '.join(tag.name for tag in self.tag.all())

    display_tag.short_description = 'Tag'

    class Meta:
        ordering = ['-created_date']


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField(help_text='Brief introduction about the author')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
