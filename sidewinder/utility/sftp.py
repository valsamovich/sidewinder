#!/usr/bin/env python2.7
# coding=utf-8

import pysftp

ftp_host = '***'
ftp_user = '***'
ftp_pass = '***'
ftp_port = '***'


def sftp_conn():
    try:
        # open connection to ftp server
        sftp = pysftp.Connection(host=ftp_host,
                                 username=ftp_user,
                                 password=ftp_pass,
                                 port=int(ftp_port))

        sftp.pwd()

        # close the ftp connection
        sftp.close()
    except Exception, e:
        print str(e)


if __name__ == '__main__':
    sftp_conn()
