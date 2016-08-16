from django.db import models


class Surfer(models.Model):
    name = models.CharField(max_length=200)
    skill = models.PositiveIntegerField()

    bio = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

class Shaper(models.Model):
    name = models.CharField(max_length=200)
    shaping_since = models.DateField()
    label = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    website_url = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s (since %s)' % (self.name, self.shaping_since.year)

class SurfboardModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Surfboard(models.Model):
    name = models.CharField(max_length=200)
    length = models.FloatField()
    width = models.FloatField()

    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    created_at = models.DateField(auto_now_add=True)

    shapers = models.ManyToManyField(Shaper) #changed from shaper, ForeignKey
    surfer = models.ForeignKey(Surfer)
    surfboard_model = models.ForeignKey(SurfboardModel, null=True, blank=True)

    @property
    def display_length(self):
        return '''%s' - %s"''' % (int(self.length / 12), self.length % 12)

    @property
    def display_dimensions(self):
        return u'%s x %s"' % (
            self.display_length,
            self.width,
        )

    def __unicode__(self):
        return u'%s by %s (%s) model: %s' % (
            self.name,
            self.shapers.all(), #Changed from .name
            self.display_dimensions,
            self.surfboard_model
        )

