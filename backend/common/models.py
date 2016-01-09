from __future__ import unicode_literals
from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
	'''abstract base model'''
	uuid = models.UUIDField(default=uuid4, editable=False, db_index=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True


class Address(BaseModel):
	line_1 = models.CharField(max_length=128)
	line_2 = models.CharField(max_length=128, null=True)
	city = models.CharField(max_length=64)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=11)

	def __unicode__(self):
		address = self.line_1
		if self.line_2 is not None:
			address += '\n{}'.format(self.line_2)
		address += '\n{}, {} {}'.format(self.city, self.state, self.zip_code)
		return address