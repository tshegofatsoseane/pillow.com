from django.db import models

class Accommodation(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    accreditation_number = models.CharField(max_length=255)
    number_of_beds = models.IntegerField()
    email = models.EmailField(max_length=255)
    cell_number = models.CharField(max_length=20)
    street_address = models.CharField(max_length=255)
    nearest_campus = models.CharField(max_length=255)
    residence_name = models.CharField(max_length=255)

    def __str__(self):
        return self.residence_name

    class Meta:
        db_table = 'Accommodation'
