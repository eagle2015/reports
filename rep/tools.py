# -*- coding: utf-8 -*- 
__author__ = 'jwh5566'

import psycopg2
# 数据库连接参数


def conn(database, user, password, host, port, sql):
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    x = []
    y = []
    for i in rows:
        if type(i[1]) == int:
            y.append(i[1])
        else:
            y.append(int(i[1]))
        if type(i[0]) == int or type(i[0]) == str:
            x.append(i[0])
        else:
            x.append(i[0].strftime('%Y-%m-%d'))
    conn.commit()
    cur.close()
    conn.close()
    return x, y