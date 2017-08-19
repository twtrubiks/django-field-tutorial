from django.db import models


# ForeignKey_tutorial

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(
        Reporter,
        related_name='articles',
        on_delete=models.CASCADE
    )

    # reporter = models.ForeignKey(
    #     Reporter,
    #     on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
