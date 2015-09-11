from django.contrib import admin
from onewait200.app.models import Person, Relation

class RelationAdmin(admin.ModelAdmin):
    list_display = ('from_person', 'to_person', 'description')

admin.site.register(Relation, RelationAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Person, PersonAdmin)
