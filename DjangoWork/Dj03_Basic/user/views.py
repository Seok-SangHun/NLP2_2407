from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):   # view 함수는 request 정보를 매개변수로 받는다  HttpRequest객체
	print('user/views.index() 호출됨')
	# view 함수는 response 를 리턴함.  HttpResponse객체
	return HttpResponse(f"""
		<h3>Hello Django</h3>
		<p>request path : {request.path}</p>
		<p>request method : {request.method}</p>
	""")

def list(request):
	print('user/views.list() 호출됨')
	return HttpResponse(f"""
		<h3>List</h3>
		<p>request path : {request.path}</p>
		<p>request method : {request.method}</p>
	""")	

def detail(request):
	print('user/views.deatil() 호출됨')
	return HttpResponse(f"""
		<h3>Detail</h3>
		<p>request path : {request.path}</p>
		<p>request method : {request.method}</p>
	""")	

def update(request):
	print('user/views.update() 호출됨')
	return HttpResponse(f"""
		<h3>Update</h3>
		<p>request path : {request.path}</p>
		<p>request method : {request.method}</p>
	""")	