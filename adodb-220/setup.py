#!/usr/bin/env python

from distutils.core import setup

setup(name="adodb",
      version="2.10",
      description="ADOdb Python",
      author="John Lim",
      author_email="jlim#natsoft.com",
      packages=["adodb"],
      url="http://adodb.sourceforge.net/#pydownload",
     )

import sys,os

def trydel(f):
    try:
        os.unlink(f)
        print "Deleted %s" % f
    except:
        pass

    try:
        os.unlink(f+'c')
    except:
        pass


for p in sys.path:
    if p.find('site-packages')>0:
        trydel(p+os.sep+'adodb.py')
        trydel(p+os.sep+'adodb_access.py')
        trydel(p+os.sep+'adodb_mssql.py')
        trydel(p+os.sep+'adodb_mxodbc.py')
        trydel(p+os.sep+'adodb_mxoracle.py')
        trydel(p+os.sep+'adodb_mysql.py')
        trydel(p+os.sep+'adodb_oci8.py')
        trydel(p+os.sep+'adodb_odbc.py')
        trydel(p+os.sep+'adodb_odbc_mssql.py')
        trydel(p+os.sep+'adodb_postgres.py')
        trydel(p+os.sep+'adodb_vfp.py')