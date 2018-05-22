

import adLib

conn=adLib.AdConn(server='127.0.0.1',port=389)
conn.domain = ''
conn.user=''
conn.search_base=''
conn.sample('user')

