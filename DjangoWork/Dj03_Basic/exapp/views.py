from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def func01(request):

    return HttpResponse(f'''
    <!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page01</title>
</head>
<body>
    <h1>Page01</h1>    
</body>
</html>

''')

# app 밑에 templates 디렉토리 생성하고
# 템플릿 파일(html 작성)

# page02.html 템플릿파일을 불러와서 렌더링하여 response 
def func02(request):
    return render(request, 'page02.html')

# /templates/ 하위 경로를 render()  에 명시 가능.
def func03(request):
    return render(request, 'aaa/bbb/page03.html')


'''
변수1
템플릿에 context 변수 보내기
   context 란? template 에 전달해줄 dict 형태의 데이터 
{{ .. }}  사용
https://docs.djangoproject.com/ko/4.0/topics/templates/#variables

Comments
{# ... #}  single-line comment
{% comment %} ~ {% endcomment %} multi-line comments.

없는 변수의 경우 rendering 되지 않는다 (에러 발생 없다)
'''
def func04(request):
    return render(request, 'page04.html', 
                  {"title": "Page04: variable", "summary": "템플릿 변수"})

'''
변수2
템플릿 시스템은 변수의 속성에 접근하기 위해 dot-lookup 문법을 사용

예제의 {{ question.question_text }} 구문을 보면, 

Django는 
1. Dictionary lookup
   먼저 question 객체에 대해 사전형으로 탐색합니다. 
2. Attribute lookup
   탐색에 실패하게 되면 속성값으로 탐색합니다. 
3. List-index lookup
   만약 속성 탐색에도 실패한다면 리스트의 인덱스 탐색을 시도하게 됩니다.  
https://docs.djangoproject.com/ko/4.0/intro/tutorial03/#use-the-template-system
'''
def func05(request):
    context = {
        "title" : "변수: Dot-Lookup",
        'summary' : '변수의 속성에 접근하기 위한 방법',

        # Dictionary lookup
        'album' : {
            'song' : '노래노래',
            'artist' : '가수가수',
        },

        # Attribute lookup
        'advisor' : User('김순희', 43),
        
        # List-index lookup
        'points' : [11, 22, 33, 44],

        'members' : [
            User('홍길동', 34),
            User('김만두', 19),
            User('차림표', {
                'main': '짜장면',
                'price': [5600, 7400, 9300] 
            })
        ],
    }
    return render(request, 'page05.html', context)

class User:
    def __init__(self, name, info):
        self.name = name
        self.info = info

    def __str__(self):
        return f'User 의 __str__ 값입니다 {self.name}-{self.info}'

''' -----------------------------------------------------------------------------
태그 (Tag)
구문: {% ... %}
태그는 다양한 렌더링 동작을 제공한다.
  ex) contents 삽입
  ex) if, for  와 같은 제어문 구조 
  ex) database  객체 접근
  ex) 다른 템플릿 태그에 접근

https://docs.djangoproject.com/ko/4.0/topics/templates/#tags

built-in tags: django 에서 기본적으로 제공되는 태그들
   https://docs.djangoproject.com/ko/4.0/ref/templates/builtins/#ref-templates-builtins-tags
custom tags : 
   https://docs.djangoproject.com/ko/4.0/howto/custom-template-tags/#howto-writing-custom-template-tags
'''

# if 태그
# https://docs.djangoproject.com/ko/4.0/ref/templates/builtins/#if
def func06(request):
    context = {
        "title": 'Tag: if',
        "summary": 'if 태그',

        "sentence": "Hello Django Framework!",

        "team_kim": ['김은정', '김선영', '김초희', '김경애', '김영미'],
        "short_track": ['황대헌', '최민정', '이준서'],

        "points": [(10, -1), (20, -2), (30, -3), (40, -4)],

        "info" : {"매물": '42평 4룸', "보증금": 2000, "세": 140},

    }
    context['fruits'] = ['apple', 'banana', '']

    return render(request, 'page06.html', context)

def func07(request):
    return
def func08(request):
    return
def func09(request):
    return
def func10(request):
    return