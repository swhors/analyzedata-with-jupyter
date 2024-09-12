from util import db_init, db_fint, select_datas, insert_datas, insert_data
import os
from config import db_host, db_port, db_user, db_passwd, db_db, charset
from model.wanted_com import WantedCom


def get_market_value_from_db():
    coms_list = []
    conn = db_init(db_host=db_host, db_passwd=db_passwd, db_user=db_user, db_db=db_db)
    datas = select_datas(conn, "wanted_com", None)
    for data in datas:
        coms_list.append(WantedCom(*data))
    db_fint(conn)
    return coms_list


def put_market_value_to_db(wanted_com):
    conn = db_init(db_host=db_host, db_passwd=db_passwd, db_user=db_user, db_db=db_db)
    insert_data(conn, "wanted_com", wanted_com)
    db_fint(conn)


def get_market_value():
    coms_list_file = get_wantedcoms_from_file()
    coms_list = get_wantedcoms_from_db()
    for com in coms_list_file:
        if com not in coms_list:
            coms_list.append(com)
            put_wantedcom_to_db(com)
    return coms_list
