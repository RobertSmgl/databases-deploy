import psycopg2
import time

conn_list = []
# conn = psycopg2.connect(dbname='local_gitlab', user='local_gitlab_adm', password='HARDpassword$*211', host='94.26.228.63')
# cursor = conn.cursor()


conn_list = []

while True:
    try:
        conn_list.append(psycopg2.connect(dbname='postgres', user='testuser', password='test-user', host='158.160.102.37'))
    except:
        continue
    #     time.sleep(1)
    # cursor = conn_list[0].cursor()
    # cursor.execute('SELECT usename,COUNT(usename) as cnt FROM pg_stat_activity GROUP BY usename;')
    # print(cursor.fetchall())
    # cursor.close()

