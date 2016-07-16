from django.contrib.gis.db import models

# Create your models here.
class PokemonSighting(models.Model):
    V_UNVERIFIED = "V_UNVERIFIED"
    VERIFICATION_CATEGORIES = (
                               (V_UNVERIFIED, "Unverified"),
                               )
    name = models.CharField(max_length=250)
    reported = models.DateTimeField(auto_now_add=True)
    verification = models.CharField(max_length=15, choices=VERIFICATION_CATEGORIES, default=V_UNVERIFIED)
    location = models.PointField()
    
    objects = models.GeoManager()