from django.db import models

class Task(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	text = models.CharField(blank=True, max_length=100)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	duration = models.IntegerField()
	progress = models.FloatField()
	parent = models.CharField(max_length=100)
	sort_order = models.IntegerField(default=0)

class Link(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	source = models.CharField(max_length=100)
	target = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	lag = models.IntegerField(blank=True, default=0)
