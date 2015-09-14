from django.http import HttpResponse
from onewait200.app.models import Person, Relation

def get_relations(request):
    response = []
    rela = Relation.objects.all()
    obj = None
    for r in rela:
        if obj and r.from_person.id in obj.values():
            break
        else:
            obj = {
                'id': r.from_person.id,
                'name': r.from_person.name
            }
            relations = Relation.objects.filter(from_person=Relation.objects.all()[0].from_person)
            obj['relations'] = []
            for re in relations:
                relation = {
                    'withWho': re.to_person.pk,
                    'text': re.description
                }
                obj['relations'].append(relation)
            response.append(obj)

    return HttpResponse(response)
