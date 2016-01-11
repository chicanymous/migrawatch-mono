from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel
from common.models import Address

class Organization(BaseModel):
	name = models.CharField(max_length=128)
	phone_number = models.CharField(max_length=11)
	address = models.ForeignKey(Address, null=True)

	def __unicode__(self):
		return self.name


class Member(BaseModel):
	POSITIONS = [('Member', 'MEMBER'), ('Admin', 'ADMIN')]
	user = models.OneToOneField(User)
	phone_number = models.CharField(max_length=11, null=True)
	logins = models.PositiveSmallIntegerField(default=0)
	position = models.CharField(choices=POSITIONS, default='MEMBER', max_length=16)

	def __unicode__(self):
		return self.affiliations.first().organization.name + ' member'

	def is_admin(self):
		return self.position == 'ADMIN'

	def is_member(self):
		return self.position == 'MEMBER'


class Affiliation(BaseModel):
	organization = models.ForeignKey(Organization)
	member = models.ForeignKey(Member, related_name='affiliations')
