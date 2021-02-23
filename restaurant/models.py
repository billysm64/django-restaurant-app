from django.db import models

class Menu(models.Model):
    CHIN_HUM = "Chin hum"
    KAENG_OM = "Kaeng om"
    TOM_SAEP = "Tom saep"
    YAM_THALE = "Yam thale"
    MU_PHAT_SATO = "Mu phat sato"

    TYPES = [
        (CHIN_HUM, "Chin hum"),
        (KAENG_OM, "Kaeng om"),
        (TOM_SAEP, "Tom saep"),
        (YAM_THALE, "Tom saep"),
        (MU_PHAT_SATO, "Mu phat sato")
    ]

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text[:50]
