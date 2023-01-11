from django.db import models


class TechStack(models.Model):
    title = models.CharField(max_length=15, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Язык п-р"
        verbose_name_plural = "Языки п-р"


class Project(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=120)
    image = models.ImageField(upload_to='PortfolioApp/images/')
    url = models.URLField(blank=True)
    techs_tack = models.ManyToManyField(TechStack)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


