from django.urls import reverse
from django.db import models

class PoliticalParty(models.Model):
    name = models.CharField(verbose_name="Naziv stranke", max_length=200)
    short_name = models.CharField(verbose_name="Kratki naziv", max_length=50)
    slug = models.SlugField(verbose_name="slug", max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Politička stranka"
        verbose_name_plural = "Političke stranke"

    def get_absolute_url(self):
        return reverse('url_glavni:fps_party', kwargs={'slug': self.slug})

# INCOME_TYPES = (
#     (1, u'Prihodi iz državnog proračuna'),
#     (2, u'Prihodi iz proračuna jedinica lokalne i područne (regionalne) samouprave'),
#     (3, u'Prihodi od imovine'),
#     (4, u'Prihodi od donacija'),
#     (5, u'Drugi prihodi'),
# )

class Income(models.Model):
    # code = models.SmallIntegerField(verbose_name=u"Šifra", choices=INCOME_TYPES)
    name = models.CharField(verbose_name="Naziv prihoda", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Prihod"
        verbose_name_plural = "Prihodi"

class Amount(models.Model):
    party = models.ForeignKey(
        PoliticalParty,
        verbose_name="Politička stranka",
        related_name='amounts',
        on_delete=models.PROTECT
    )
    income = models.ForeignKey(
        Income,
        verbose_name="Prihod",
        on_delete=models.PROTECT
    )
    amount = models.DecimalField(
        verbose_name="Iznos",
        decimal_places=2,
        max_digits=20,
        default=0
    )
    year = models.SmallIntegerField(verbose_name="Godina")

    def __str__(self):
        return self.party.short_name + ", " + self.income.name + ": " + str(self.amount)

    class Meta:
        verbose_name = "Iznos"
        verbose_name_plural = "Iznosi"
