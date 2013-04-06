from django.db import models

class Competitor(models.Model):
    name = models.TextField(max_length=100)
    nick_name = models.TextField(max_length=100)
    no = models.IntegerField(max_length=1, unique=True)

    def __unicode__(self):
        return '%s' % self.name

class Vote(models.Model):
    competitor = models.ForeignKey(Competitor, related_name='votes')

    def __unicode__(self):
        return 'Vote for %s' % self.competitor.nick_name