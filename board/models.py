from django.db import models

# Create your models here.
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now=timezone.now)
    readcount = models.IntegerField(default=0)

    def _str_(self):
        return '%s. %s(%d)' % (self.title, self.writer, self.readcount)
    def UpReadCount(self):
        self.readcount += 1
        self.save()