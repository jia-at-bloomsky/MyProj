import MySQLdb as mdb

def mysql_connection():
    host = 'bloomsky.cul9sh5shsvw.rds.cn-north-1.amazonaws.com.cn'
    db = 'bloomsky_log'
    user = 'jia'
    passwd = 'Il0veweather'
    conn = mdb.connect( host=host, port=3306, user=user, passwd=passwd, db=db )
    cur = conn.cursor()
    con.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    return conn, cur