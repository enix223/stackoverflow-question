from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import DateRangeField
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.conf import settings


class Image(models.Model):
    # http://stackoverflow.com/questions/42874638/django-rest-framework-how-to-download-image-with-this-image-send-directly-in-t
    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    creation_date = models.DateTimeField(
        help_text=_('Creation date'),
        auto_now_add=True,
        editable=False
    )

    modified_date = models.DateTimeField(
        help_text=_('Last modification date'),
        auto_now=True
    )

    image_file = models.ImageField(upload_to='images/', null=True)


# http://stackoverflow.com/questions/42428059/django-tests-with-schema-schema-not-found


class MyModel(models.Model):
    """Base AdWords account model."""
    account_nm = models.CharField(max_length=255, blank=True, null=True,
                                  db_column='customer_nm')

    class Meta:
        #app_label = 'mylabel'
        db_table = '"stage"."mytable"'
        managed = True #False if not settings.TESTING else True

# http://stackoverflow.com/questions/42340190/django-query-with-conditional-function-when


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return '%s %s' % (self.name, self.price)

    def __repr__(self):
        return unicode(self).encode('utf-8')


class Menu(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product)

    def __unicode__(self):
        return '%s %s' % (self.date, self.product)

    def __repr__(self):
        return unicode(self).encode('utf-8')


class Order(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return '%s %s' % (self.date, self.user)

    def __repr__(self):
        return unicode(self).encode('utf-8')


class OrderItems(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Menu, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    take_away = models.BooleanField(default=False)

    def take_away_cost(self):
        return self.product__product__price * self.quantity + 1

    def __unicode__(self):
        return '%s %s %s %s' % (self.order, self.product, self.quantity, self.take_away)

    def __repr__(self):
        return unicode(self).encode('utf-8')

# http://stackoverflow.com/questions/41324537/why-model-object-is-not-iterable


class Services(models.Model):
    description = models.TextField()  # Already existing field


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
