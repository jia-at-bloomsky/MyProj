from DB_connector import mysql_connection

def getsummary(cur,date):
    cur.execute("SELECT * FROM log_super_admin WHERE date='%s'" % date)
    res = pd.DataFrame(list(cur.fetchall()))
    return res.num_all_organizations[0], res.num_all_spots[0], res.pct_online_spots[0], res.num_all_rainbuckets[0], \
           res.pct_online_rainbuckets[0]

try:
    conn, cur = mysql_connection()
except:
        print('Failed to connect to MySQL')
        exit(0)

date = str( input("please input date in 'YYYYMMDD':  ") )
date = date[:4]+'-'+date[4:6]+'-'+date[6:]
corg, cspots, rspots, crb, rrb = getsummary(cur,date)
print date
print '\n'
print 'number of organizations:  ', corg
print '\n'
print 'number of spots:  ', cspots
print 'spots online rate:  ', rspots
print '\n'
print 'number of rainbuckets:  ', crb
print 'rainbuckets online rate:  ', rrb