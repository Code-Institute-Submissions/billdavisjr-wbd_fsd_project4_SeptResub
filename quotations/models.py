from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254)
    # note: did not add null=True and blank=True params to these
    # as these both are required and must be non-blank

    # get rid of warning from pylint
    objects = models.Manager()

    def __str__(self):
        return self.display_name

    def get_display_name(self):
        return self.display_name


class Quotation(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    text = models.TextField()
    person = models.CharField(max_length=254)

    source = models.CharField(max_length=254, blank=True, default='')
    dateSaid = models.DateField(null=True, blank=True)
    yearsLived = models.CharField(max_length=254, blank=True, default='')
    stars = models.DecimalField(max_digits=2, decimal_places=1,
                                null=True, blank=True)
    occupation = models.TextField(blank=True)
    realName = models.CharField(max_length=254, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    favorite = models.BooleanField(default=False)

    # get rid of warning from pylint
    objects = models.Manager()

    def __str__(self):
        return self.text + '  -- ' + self.person
