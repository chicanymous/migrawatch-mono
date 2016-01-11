from __future__ import unicode_literals
from django.db import models
from common.models import BaseModel
from accounts.models import Member, Organization
from common.miscellany import STATES


class Raid(BaseModel):
    detainee_count = models.PositiveSmallIntegerField(null=True)

    state = models.CharField(choices=STATES, max_length=2)
    city = models.CharField(null=True, max_length=64)
    zip_code = models.CharField(null=True, max_length=11)

    reportee = models.ForeignKey(Member, related_name='reported_raids')
    reported_by = models.ForeignKey(Organization, related_name='reported_raids')

    verified = models.NullBooleanField()
    verified_by = models.ForeignKey(Member, related_name='verified_raids', null=True)

    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    notes = models.CharField(max_length=5000)

    def __unicode__(self):
        return 'Raid in {} reported by {}'.format(self.state, self.reportee)

    def verify(self, member):
        self.verified = True
        self.verified_by = member
        self.save()
        return self.verified

    def negate(self, member):
        ''' because you never know '''
        self.verified = False
        self.verified_by = member
        self.save()
        return self.verified
