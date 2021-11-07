from django.db import models


class Md5str(models.Model):
    id = models.AutoField(primary_key=True)
    md5str = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.md5str
