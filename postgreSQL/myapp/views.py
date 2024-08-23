from django.shortcuts import render
from .models import Person
from django.http import HttpResponse

def person_list(request):
    # 직접 SQL 쿼리를 사용해 Person 데이터를 가져옵니다.
    people = Person.objects.raw('SELECT * FROM myapp_person;')

    # HTML 내용을 생성합니다.
    html = "<h1>Person List</h1><ul>"

    # 각 Person 객체를 순회하면서 리스트 아이템을 추가합니다.
    for person in people:
        html += f"<li>{person.first_name} {person.last_name}</li>"

    html += "</ul>"

    # 데이터를 템플릿에 넘겨줍니다.
    return HttpResponse(html)