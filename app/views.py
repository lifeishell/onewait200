import json
from django.http import HttpResponse
from onewait200.app.models import Person, Relation

def get_relations(request):
    response = []
    person = Person.objects.all()

    obj = None

    for p in person:
        relations = Relation.objects.filter(from_person=p)
        obj = {
                'id': p.name,
                'name': p.name,
                'relations': []
            }
        for r in relations:
            relation = {
                'withWho': r.to_person.name,
                'text': r.description,
                'oneWay': Relation.objects.filter(to_person=p, from_person=r.to_person).count()
            }
            obj['relations'].append(relation)

        response.append(obj)

    return HttpResponse(json.dumps(response), content_type="application/json")

def add_person(request):
    if request.POST and request.POST['name']:
        name = request.POST['name']
    else:
        return HttpResponse('no param')
    if Person.objects.filter(name=name).count() > 0:
        return HttpResponse('existing')
    p = Person.objects.create()
    p.name = name
    try:
        p.save()
    except:
        return HttpResponse('save error')

    return HttpResponse('succ')

def add_relation(request):
    if request.POST and request.POST['from'] and request.POST['to'] and request.POST['description']:
        to_person = request.POST['to']
        description = request.POST['description']
        from_person = request.POST['from']
    else:
        return HttpResponse('no param')

    try:
        r = Relation.objects.create(
            from_person=Person.objects.get(name=from_person),
            to_person=Person.objects.get(name=to_person)
            )
    except:
        return HttpResponse('existing')

    try:
        r.description = description
        r.save()
    except:
        return HttpResponse('save error')
    return HttpResponse('succ')
