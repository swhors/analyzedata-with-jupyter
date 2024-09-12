from util import db_init, db_fint, select_datas, insert_datas, insert_data
import os
from config import db_host, db_port, db_user, db_passwd, db_db, charset
from model.wanted_com import WantedCom
from datetime import datetime, timedelta


def get_market_value_from_db(from_date: datetime, to_date: datetime):
    value_list = []
    conn = db_init(db_host=db_host, db_passwd=db_passwd, db_user=db_user, db_db=db_db)
    datas = select_datas(conn, "market_value", None)
    for data in datas:
        value_list.append(WantedCom(*data))
    db_fint(conn)
    return value_list


def select_market_value(conn, cursor=None, value=None):
    value_list = []
    values = select_datas(conn, cursor=cursor, table="market_value", where=value.where_by_code_and_openv_and_updated())
    for val in values:
        value_list.append(val)
    return value_list


def insert_market_value(conn=None, cursor=None, value=None, auto_commit=True):
    if conn == None:
        conn1 = db_init(db_host=db_host, db_passwd=db_passwd, db_user=db_user, db_db=db_db)
    else:
        conn1 = conn

    if cursor == None:
        cur = conn1.cursor()
    else:
        cur = cursor

    ret = select_market_value(conn=conn1, cursor=cur, value=value)
    if len(ret) == 0:
        insert_data(conn=conn1, cursor=cur, table="market_value", value=value, auto_commit=auto_commit)

    if conn == None:
        db_fint(conn1)


def inset_market_values(values):
    conn = db_init(db_host=db_host, db_passwd=db_passwd, db_user=db_user, db_db=db_db)
    cursor = conn.cursor()
    for value in values:
        insert_market_value(conn=None, cursor=None, value=value, auto_commit=True)
    conn.commit()
    db_fint(conn)
