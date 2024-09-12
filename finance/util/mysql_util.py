import pymysql


# db connect
def db_init(db_host: str, db_user: str, db_passwd: str, db_db: str):
    global conn
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
    cur.execute(query)
    rows = cur.fetchall()
    print(f'fetched data = {len(rows)}')
    for row in rows:
        print(row)
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
    for stock in stocks:
        cmd = f'insert into {table} values({(values)})'
        cur.execute(cmd)
    conn.commit()
    cur.close()
