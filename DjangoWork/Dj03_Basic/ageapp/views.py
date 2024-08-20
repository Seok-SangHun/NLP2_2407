from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def age_input(request):
    return HttpResponse(f'''
    <form action="/ages/age_check/">
		당신의 나이를 입력하세요<br/>
		<input type="text" name="age" size=4/><br/>
		<input type="submit" value = "전송"/>	
	</form>
''')


# view 함수에서 redirect(url) 함수결과를 리턴하면 redirect 발생!
def age_check(request):
    age = int(request.GET['age'])
    if age > 19:
        return redirect(f'/ages/adult/?age={age}')
    else:
        return redirect(f'/ages/underage/?age={age}')
    
def adult(request):
    age = int(request.GET['age'])
    return HttpResponse(f'''
    <h2>성년입니다</h2>
    당신은 {age}세 입니다.
	당신은 성인 입니다... 사이트를 이용하실 수 있습니다..<br>
	<a href="/ages/age_input/">처음으로</a>
''')

def underage(request):
    age = int(request.GET['age'])
    return HttpResponse(f'''
    <h2>미성년자입니다</h2>
	당신은 {age}세 입니다.
	당신은 미성년자 입니다....사이트 이용이 불가능합니다...<br>
	{19 - age}년 뒤에 사용 가능합니다 <br>
	<a href="/ages/age_input/"> 처음으로</a>
''')