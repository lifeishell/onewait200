from django.contrib import admin
from onewait200.app.models import Person, Relation

class RelationInline(admin.TabularInline):
    model = Relation

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        RelationInline,
    ]
admin.site.register(Person, PersonAdmin)