import sqlite3
import logging

class Database:
  def __init__(self, db_file):
    self.db_file = db_file  # sqlite3 데이터베이스 파일명
    self.conn = None  # 데이터 베이스 connection 객체.  이를 통해 query 수행 

  # DB 연결
  def connect(self):
    if self.conn != None:
      return 

    self.conn = sqlite3.connect(self.db_file)
    self.conn.row_factory = sqlite3.Row # SELECT 결과를 Row 객체로 받게 함. => Row객체는 나중에 dict, tuple 형태로 변환 가능.
    print("DB 연결 성공")

  # DB 연결 닫기
  def close(self):
    if self.conn is None: return

    self.conn.close()
    self.conn = None
    print("DB 연결 닫기 성공")

  # SQL 구문 실행 (DDL, INSERT, UPDATE, DELETE <- DML)
  def execute(self, sql):
    last_row_id = -1   # 마지막으로 INSERT 된 id값 (PK값)
    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)  # sql 쿼리 실행!
      self.conn.commit()   # 커밋 수행 (변경내용 DB 에 저장,반영)
      last_row_id = cursor.lastrowid  # 마지막으로 INSERT 된 PK 값
    except Exception as ex:
      print("예외]", ex)
      logging.error(ex)

    finally:
      return last_row_id

  # SELECT 구문 실행, 1개의 Row 만 불러오기
  def select_one(self, sql):
    result = None

    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)  # SELECT 의 결과는 table 형태 (row 들..)
      result = dict(cursor.fetchone())  # 위 결과에서 첫번째 Row 를 읽어와 dict 로 변환

    except Exception as ex:
      print("예외]", ex)
      logging.error(ex)
    finally:
      return result

  # SELECT 구문 실행.  전체 Row(들) 불러오기.  dict 의 list 형태로 리턴 
  def select_all(self, sql):
    results = None

    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)  # SELECT 의 결과는 table 형태 (row 들..)
      results = [dict(row)  for row in cursor.fetchall()]

    except Exception as ex:
      print("예외]", ex)
      logging.error(ex)
    finally:
      return results

  def createTable(self):
    print('createTable() 테이블 생성 시도')
    sql = '''
    CREATE TABLE `board` (
      `id` INTEGER PRIMARY KEY AUTOINCREMENT,
      `subject` TEXT NOT NULL,
      `user` TEXT NOT NULL,
      `content` TEXT,
      `view_cnt` INTEGER DEFAULT 0,
      `reg_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    '''
    self.execute(sql)
    print('createTable() 테이블 생성 완료')


