from django.contrib import admin
from accounts.models import Organization, Member, Affiliation

admin.site.register(Organization)
admin.site.register(Member)
admin.site.register(Affiliation)