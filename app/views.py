from django.http import HttpResponse
from onewait200.app.models import Person, Relation

def get_relations(request):
    response = []
    person = Person.objects.all()

    obj = None

    for p in person:
        relations = Relation.objects.filter(from_person=p)
        obj = {
                'id': p.id,
                'name': p.name,
                'relations': []
            }
        for r in relations:
            relation = {
                'withWho': r.to_person.pk,
                'text': r.to_person.description,
                'oneWay': Relations.objects.filter(to_person=p, from_person=r.to_person).count()
            }
            obj['relations'].append(relation)

        response.append(obj)

    return HttpResponse(response)
