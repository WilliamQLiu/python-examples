import datetime

from django.utils import timezone
from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self): # Returns Question instead of <Poll: Poll object>
        return self.question
    def was_published_recently(self): # Custom method for demonstration
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # Adds functionality to sort by field 'was_published_recently'
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    search_fields = ['question'] #Added search by 'question' field

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
