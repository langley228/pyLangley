# pyLangley

<H3>package<H3>

```
adLib
```


<H3>adLib Sample</H3>

```
import adLib
conn=adLib.AdConn(server='127.0.0.1',port=389)
conn.domain = 'com'
conn.user='admin'
conn.password='password'
conn.search_base='DC=com,DC=tw'
conn.findUser('admin')
```
