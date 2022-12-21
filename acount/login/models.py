from django.db.models import *


class Task(Model):
	title = CharField(max_length=200)
	complete = BooleanField(default=False)
	created = DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title