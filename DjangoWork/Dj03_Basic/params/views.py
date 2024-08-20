from django.http import HttpResponse
from django.shortcuts import render

# view 함수의 첫번째 매개변수는  HttpRequest 객체다
# client 로부터 넘어오는 parameter 들이 담겨져 있다
# https://docs.djangoproject.com/en/4.0/ref/request-response/#httprequest-objects


# 브라우저에서 직접 get 방식으로 받아올수 있다.
# request.GET  : dict 형태로 parameter 들의 name: value 받아옴
#   (QueryDict 타입객체다)
# 받아온 parameter 들은 무조건 문자열(str) 이다
# 숫자타입에 대한 산술,비교연산 하려면 반드시 형변환 하자.


def page1(request):
    # params/page1/?name=aaa&age=14
    # reqeust.GET['name']
    name = request.GET.get('name', '')
    age = request.GET.get('age', '')

    print('page1():', request.GET)

    return HttpResponse(f'''
        <h2>Page 1 : GET + query string</h2>
        name: {name} <br>
        age: {age} <br>
        성인여부: {int(age) > 19}<br>
    ''')
    
# 동일한 name 의 값이 여러개 전달되면?
# http://127.0.0.1:8000/page1/?name=aaa&name=bbb&age=20
# getlist() 메소드 사용


def page2(request):
	print('page2():', request.GET)    
  
	names = request.GET.getlist('name')  # neme= 의 value 들의 list 를 리턴
	namestr = ','.join(names)
	age = request.GET['age']
	return HttpResponse(f'''
	<h2>Page2 : 동일한 name 이 여러개</h2>
  name: {namestr}<br>
  age: {age}<br>
''')

def article1(request, year):   # URL 에 담긴 year 값을 받아온다.
	print('article 1:', request.path, year, type(year))
	return HttpResponse(f'''
		<h2>article 1: {year}</h2>
		2000년 이후? : {int(year) > 2000} <br>
''')
      
def article2(request, year, month):
	print('article 2:', request.path, year, type(year), month, type(month))
	return HttpResponse(f'''
		<h2>article 2: {year}년 {month}월</h2>
		2000년 이후? : {int(year) > 2000} <br>
''')

