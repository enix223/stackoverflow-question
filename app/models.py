from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import DateRangeField

# http://stackoverflow.com/questions/41324537/why-model-object-is-not-iterable


class Background(models.Model):
    bk_color = models.CharField(max_length=20)
    createAt = models.DateTimeField('create', auto_now=True)

    def __unicode__(self):
        return self.bk_color


class FormOne(models.Model):
    name = models.CharField(max_length=40)
    # background = models.ManyToManyField(Background, blank=True)
    background = models.ForeignKey(Background, blank=True)  # use ForeignKey instead of ManyToManyField

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    datefromto = DateRangeField()


class Scheduler(models.Model):
    weekhours = models.ManyToManyField('WeekHour', related_name='schedulers')


class WeekHour(models.Model):
    hour = models.PositiveSmallIntegerField(verbose_name='Hour in week (0 - 7*24')


class Book(models.Model):
    name = models.CharField('name of the book', max_length=100)
    author_name = models.CharField('the name of the author', max_length=50)


class MovieDetails(models.Model):
    pass


class TheaterBase(models.Model):
    pass


class TheaterShowTimings(models.Model):
    showname = models.CharField(max_length=100)
    showtime = models.TimeField()  # stores only time
    theatershowtimingsid = models.CharField(primary_key=True, max_length=100)
    movieActiveDays = models.ManyToManyField('MovieActiveDays', through='ActiveShowTimings')

    def __str__(self):
        return self.theatershowtimingsid


class MovieActiveDays(models.Model):
    date = models.DateField()  # stores single only date
    moviedetails = models.ForeignKey(MovieDetails, on_delete=models.CASCADE)
    theaterbase = models.ForeignKey(TheaterBase, on_delete=models.CASCADE)
    activedayid = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.activedayid


class ActiveShowTimings(models.Model):
    TheaterShowTimings = models.ForeignKey('TheaterShowTimings', on_delete=models.CASCADE)
    MovieActiveDays = models.ForeignKey(MovieActiveDays, on_delete=models.CASCADE)
    activeshowid = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.activeshowid
