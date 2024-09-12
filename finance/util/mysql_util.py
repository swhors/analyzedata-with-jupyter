import pymysql

charset="utf8"


# db connect
def db_init(db_host: str, db_user: str, db_passwd: str, db_db: str):
    conn = pymysql.connect(host=db_host, user=db_user, password=db_passwd, db=db_db, charset=charset)
    return conn


# close connection
def db_fint(conn):
    if conn != None:
        conn.close()


"""
select data

args:
  conn = connection
  query = input query
    ex ) query : "select * from finance.stock_list;"
"""
def select_datas(conn, table: str, where: str) -> []:
    cur = conn.cursor()
    datas = []
    query = f'select * from {table}'
    if where is not None and len(where) > 6:
        query = query + f' where {where}'
    #print(f'query={query}')
    cur.execute(query)
    rows = cur.fetchall()
    #print(f'fetched data = {len(rows)}')
    for row in rows:
        datas.append(row)
    cur.close()
    return datas


"""
insert data

args: 
  conn = connection
  table = string, table name
  values = string, values
"""
def insert_datas(conn, table, values):
    cur = conn.cursor()
    for value in values:
        query = f'insert into {table} values({str(value)})'
        #print(f'query={query}')
        cur.execute(query)
    conn.commit()
    cur.close()

def insert_data(conn, table, value):
    cur = conn.cursor()
    query = f'insert into {table} values({str(value)})'
    #print(f'query={query}')
    cur.execute(query)
    conn.commit()
    cur.close()
