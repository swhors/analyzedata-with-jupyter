from util import db_init, db_fint, select_datas, insert_datas, insert_data
import os
from config import db_host, db_port, db_user, db_passwd, db_db, charset
from model.wanted_com import WantedCom


"""
read wanted company list
"""
def get_wantedcoms_from_file():
    coms_list = []
    print(f"current_path = {os.getcwd()}")
    with open("coms_list.txt") as listfd:
        lines = listfd.readlines()
        for line in lines:
            line = line.replace('\n', '')
            code, name, market = line.split(',')
            coms_list.append(WantedCom(code=code, name=name, market=market))
        listfd.close()
        return coms_list


def get_wantedcoms_from_db():
    coms_list = []
    conn = db_init(db_host=db_host, db_passwd=db_passwd, db_user=db_user, db_db=db_db)
    cursor = conn.cursor()
    datas = select_datas(conn=conn, cursor=cursor, table="wanted_com", where=None)
    for data in datas:
        coms_list.append(WantedCom(*data))
    cursor.close()
    db_fint(conn)
    return coms_list


def put_wantedcom_to_db(wanted_com):
    conn = db_init(db_host=db_host, db_passwd=db_passwd, db_user=db_user, db_db=db_db)
    cur = conn.cursor()
    insert_data(conn=conn, cursor=cur, table="wanted_com", values=wanted_com)
    db_fint(conn)


def get_wantedcoms():
    coms_list_file = get_wantedcoms_from_file()
    coms_list = get_wantedcoms_from_db()
    for com in coms_list_file:
        if com not in coms_list:
            coms_list.append(com)
            put_wantedcom_to_db(com)
    return coms_list
