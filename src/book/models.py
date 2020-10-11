from book.validators import date_should_be_in_past_validator, year_validator

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    date_of_birth = models.DateField(validators=[date_should_be_in_past_validator])
    date_of_death = models.DateField(null=True, blank=True,
                                     validators=[date_should_be_in_past_validator])
    email = models.EmailField(blank=True, null=True)
    country = models.CharField(max_length=64)
    gender = models.BooleanField(null=True, blank=True,
                                 help_text="True if male, False if female, Null is unknown")
    language = models.CharField(max_length=64)
    created_by_student = models.DateTimeField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=127)
    publish_year = models.PositiveSmallIntegerField(validators=[year_validator])
    created_by_student = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
