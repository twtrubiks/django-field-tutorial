from django.db import models


# ForeignKey_tutorial

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(
        Reporter,
        related_name='articles',
        on_delete=models.CASCADE,
        db_index=True # 預設為 True, 會自動幫你建立 index
    )

    # reporter = models.ForeignKey(
    #     Reporter,
    #     on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        # ref
        # https://docs.djangoproject.com/en/4.2/ref/models/options/#ordering
        ordering = ["headline"]

        # unique_together = ['headline', 'reporter']
        # indexes = [
        #     models.Index(name='headline_reporter_index', fields=['headline','reporter'],)
        # ]

        # index 建議使用 Meta.indexes, db_index 未來可能會棄用
        # ref
        # https://docs.djangoproject.com/en/4.2/ref/models/fields/#db-index
