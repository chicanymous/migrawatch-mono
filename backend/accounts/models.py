from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel
from common.models import Address


class BaseUser(BaseModel, User):
	''' the base user ''' 
	phone_number = models.CharField(max_length=11)
	logins = models.PositiveSmallIntegerField(default=0)

	def __unicode__(self):
		return this.user.email


class Organization(BaseModel):
	name = models.CharField(max_length=128)
	phone_number = models.CharField(max_length=11)
	address = models.ForeignKey(Address, null=True)

	def __unicode__(self):
		return self.name


class Member(BaseModel):
	POSITIONS = [('Member', 'MEMBER'), ('Admin', 'ADMIN')]
	user = models.ForeignKey(BaseUser)
	position = models.CharField(choices=POSITIONS, default='MEMBER', max_length=16)

	def is_admin(self):
		return self.position == 'ADMIN'

	def is_member(self):
		return self.position == 'MEMBER'


class Affiliation(BaseModel):
	organization = models.ForeignKey(Organization)
	member = models.ForeignKey(Member)