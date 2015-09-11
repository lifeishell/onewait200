from django.contrib import admin
from onewait200.app.models import Person, Relation

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)

class RelationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Relation, RelationAdmin)