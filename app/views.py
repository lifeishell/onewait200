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
        return HttpResponse(json.dumps('missing name'), content_type="application/json")
    if Person.objects.filter(name=name).count() > 0:
        return HttpResponse(json.dumps('existing'), content_type="application/json")
    p = Person.objects.create()
    p.name = name
    try:
        p.save()
    except:
        return HttpResponse(json.dumps('save error'), content_type="application/json")

    return HttpResponse(json.dumps('success'), content_type="application/json")

def add_relation(request):
    if request.POST and request.POST['from'] and request.POST['to'] and request.POST['description']:
        to_person = request.POST['to']
        description = request.POST['description']
        from_person = request.POST['from']
    else:
        return HttpResponse(json.dumps('missing name'), content_type="application/json")

    try:
        r = Relation.objects.create(
            from_person=Person.objects.get(name=from_person),
            to_person=Person.objects.get(name=to_person)
            )
    except:
        return HttpResponse(json.dumps('existing'), content_type="application/json")

    try:
        r.description = description
        r.save()
    except:
        return HttpResponse(json.dumps('save error'), content_type="application/json")
    return HttpResponse(json.dumps('success'), content_type="application/json")
