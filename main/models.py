from django.db import models

class Table(models.Model):
	number = models.IntegerField()
	n_places = models.IntegerField()
	form = models.CharField(max_length=50)
	coordinates_x = models.IntegerField(blank=True, null= True)
	coordinates_y = models.IntegerField(blank=True, null= True)
	size_w = models.IntegerField(blank=True, null= True)
	size_h = models.IntegerField(blank=True, null= True)
	date_reserved = models.DateField(blank=True, null= True)
	reserved = models.BooleanField(default = False)

	def __str__(self):
		return "Table "+str(self.number)