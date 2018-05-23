
from ldap3 import Server, \
    Connection, \
    AUTO_BIND_NO_TLS, \
    SUBTREE, \
    ALL_ATTRIBUTES

class AdConn(object):
    _server = "127.0.0.1"
    _port = 389
    _user = ''
    _domain = ''
    _password = ''
    _search_base=''

    def __init__(self, *args, **kwargs):
        self._server = kwargs["server"]
        self._port = kwargs["port"]
    
    @property
    def server(self):
        return self._server

    @property
    def port(self):
        return self._port

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value    

    @property   
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
        
    @property   
    def domainuser(self):
        return "{domain}\\{user}".format(domain=self._domain,user=self._user)
    
    @property   
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property   
    def search_base(self):
        return self._search_base

    @search_base.setter
    def search_base(self, value):
        self._search_base = value

    def findUser(self,samAccountName):
        result = ""
        with Connection(Server(self.server, port=self.port),
                        auto_bind=AUTO_BIND_NO_TLS,
                        read_only=True,
                        check_names=True,
                        user=self.domainuser, password=self._password) as c:
 
            result = c.search(search_base=self._search_base,
                     search_filter='(&(objectClass=user)(objectCategory=person)(samAccountName=' + samAccountName + '))',
                     search_scope=SUBTREE,
                     attributes=ALL_ATTRIBUTES,
                     get_operational_attributes=True)

        for user in c.response:
            if 'attributes' in user:
                print(user['attributes']['cn'])
                for attr in user['attributes']:
                    print('   {0} : {1}'.format(attr, user['attributes'][attr]))
 