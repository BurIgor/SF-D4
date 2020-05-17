from django.db import models

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    publishing = models.ForeignKey('Publishing', on_delete=models.CASCADE, related_name='books', null=True)

    def __str__(self):
        return self.title


class Publishing(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
