from django.shortcuts import render
from utils.Database import Database

def write(request):
    print(f'{request.path} {request.method} 요청')

    if request.method == "GET":
        return render(request, 'write.html')  # 글 작성 폼
    elif request.method == 'POST':
        # 폼에 작성한 내용을 읽어와서
        user = request.POST['user']   # name='user'
        subject = request.POST['subject']  # name='subject'
        content = request.POST['content']  # name='content'

        # DB 에 저장!
        conn = Database()
        conn.connect()
        # INSERT 직후 생성된 id(pk) 값 리턴받는다.
        id = conn.execute("INSERT INTO board(user, subject, content) VALUES('%s', '%s', '%s')" % (user, subject, content))
        conn.close()

        context = {
            "result": 1,
            "post": {"id": id},
        }

        return render(request, 'writeOk.html', context)



def list(request):
    print(f'{request.path} {request.method} 요청')

    conn = Database()
    conn.connect()
    # 목록 읽어오기 SELECT
    posts = conn.select_all("SELECT id, content, user, subject, view_cnt, reg_date FROM board ORDER BY id DESC")
    conn.close()

    return render(request, 'list.html', {'list': posts})  # 글 목록

def detail(request, id):
    print(f'{request.path} {request.method} 요청, id:{id}')

    conn = Database()
    conn.connect()
    # 조회수 증가 UPDATE
    conn.execute("UPDATE board SET view_cnt = view_cnt + 1 WHERE id = %d" % (id))
    # 읽어오기 SELECT
    post = conn.select_one("SELECT id, content, user, subject, view_cnt, reg_date FROM board WHERE id = %d" % (id))
    conn.close()

    return render(request, 'detail.html', {'post': post})  # 글 상세 페이지

def update(request, id=None):
    print(f'{request.path} {request.method} 요청, id:{id}')

    if request.method == "GET":  # 글 수정 폼
        conn = Database()
        conn.connect()
        # 읽어오기 SELECT
        post = conn.select_one("SELECT id, content, user, subject, view_cnt, reg_date FROM board WHERE id = %d" % (id))
        conn.close()

        return render(request, 'update.html', {'post': post})  # 글 수정 폼
    elif request.method == "POST":  # 글 수정 완료
        id = int(request.POST['id'])
        subject = request.POST['subject']
        content = request.POST['content']

        conn = Database()
        conn.connect()
        # UPDATE 글 수정
        conn.execute("UPDATE board SET subject='%s', content='%s' WHERE id = %d" % (subject, content, id))
        conn.close()

        return render(request, 'updateOk.html', {'result': 1, 'post': {"id": id}})
    

def delete(request):
    print(f'{request.path} {request.method} 요청')

    if request.method == "POST":
        id = int(request.POST['id'])    

        conn = Database()
        conn.connect()
        # DELETE 삭제
        conn.execute("DELETE FROM board WHERE id = %d" % (id))
        conn.close()

        return render(request, 'deleteOk.html', {'result': 1})
