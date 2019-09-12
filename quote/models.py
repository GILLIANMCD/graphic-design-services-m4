from django.db import models


class Quote(models.Model):
    service_list = (
        ('logo_design', 'Logo Design'),
        ('full_brand_design', 'Full Brand Design'),
        ('business_card', 'Business Card'),
        ('brochure', 'Brochure'),
        ('leaflet', 'Leaflet'),
        ('full_print_design', 'Full Print Suite'),
        )
    full_name = models.CharField(max_length=50, blank=False)
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=False)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    service_required = models.CharField(max_length=100, choices = service_list)

    
