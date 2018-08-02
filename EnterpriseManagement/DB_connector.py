import MySQLdb as mdb

from cassandra.cluster import Cluster
from cassandra.query import dict_factory, BatchStatement
from cassandra.auth import PlainTextAuthProvider
from collections import defaultdict

def mysql_connection():
    host = 'bloomsky.cul9sh5shsvw.rds.cn-north-1.amazonaws.com.cn'
    db = 'bloomsky_log'
    user = 'jia'
    passwd = 'Il0veweather'
    conn = mdb.connect( host=host, port=3306, user=user, passwd=passwd, db=db )
    cur = conn.cursor(mdb.cursors.DictCursor)
    conn.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    return conn, cur

class SimpleClient:
    session = None

    def connect(self, nodes):
        auth_provider = PlainTextAuthProvider(username='jia', password='Il0veweather')
        cluster = Cluster(nodes, auth_provider=auth_provider)
        metadata = cluster.metadata
        self.session = cluster.connect()

    def close(self):
        self.session.cluster.shutdown()
        self.session.shutdown()


def setup_connection():
    client = SimpleClient()
    client.connect(['10.0.4.8', '10.0.2.78', '10.0.30.218'])
    session = client.session
    session.row_factory = dict_factory
    session.set_keyspace('bloomsky_china')
    return client, session