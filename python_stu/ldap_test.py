#!/usr/bin/python

import ldap

ldapserver = "ldap://172.16.30.70:389"
baseDN = "dc=magicstack,dc=com"
ldapuser = "root"
ldappwd = "111111"

# 获取用户DN
def get_userDN(user):
   
    conn = ldap.initialize(ldapserver)
    conn.protocal_version = ldap.VERSION3
    conn.simple_bind(ldapuser,ldappwd)

    searchScope = ldap.SCOPE_SUBTREE
    searchFiltername = ""
