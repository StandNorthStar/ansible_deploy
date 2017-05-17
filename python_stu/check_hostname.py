#!/usr/bin/python
# encoding=utf-8

# only use centos / reht

import paramiko
import time,datetime


class check_host(object):



    def __init__(self,hosts):
        self.hosts = hosts


    def ssh_con(self,command):
        '''
        host: {host:{"username":"user","password":"pwd","port":22}}
        根据页面选择的hosts,远程到主机上,然后获取这些主机名称.
        :return: 返回一个字典,{选择的主机:主机名称}
        '''

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hosts = self.hosts
        result= {}
        for host in hosts.keys():
            user = hosts[host].get("username")
            pwd = hosts[host].get("password")
            port = hosts[host].get("port")

            try:
               ssh.connect(hostname=host,port=port,username=user,password=pwd)
               stdin, stdout, stderr = ssh.exec_command(command)
               result[host] = stdout.read().strip()
               ssh.close()
            except paramiko.ssh_exception.NoValidConnectionsError as e:
               result[host] = "unable to connect"

        return result

    def get_hostname(self):
        hostname = self.ssh_con("fdisk -l")
        return hostname

    def get_time(self):
        hosttime = self.ssh_con("date '+%Y-%m-%d %H:%M'")
        return hosttime

        # result = {}
        #
        # dtime=hosttime.keys()
        # for i in range(len(dtime)-1):
        #     for j in range(len(dtime)-i-1):
        #         if hosttime[dtime[j]] == hosttime[dtime[j+1]]:
        #             result[dtime[j]] = "time ok"
        #         else:
        #             result[dtime[j]] = hosttime[dtime[j]]
        # return result

    def check_firewall(self):
        firewall = self.ssh_con("systemctl status firewalld | grep Active")
        selinux = self.ssh_con("getenforce")

        result = {'firewall':{},'selinux':{}}
        for host in firewall.keys():
            value = firewall[host]

            #if 'active' not in value:
            if value is '':
                result['firewall'][host] = "firewalld is not install"
            else:
                result['firewall'][host] = value
        for host in selinux.keys():
            value = selinux[host]
            result['selinux'][host] = value
        return result

    def check_os(self):
        ossys = self.ssh_con("cat /etc/centos-release")
        return ossys

    def check_net(self):
        net = self.ssh_con("ip route | grep default")

if __name__ == "__main__":

    _hosts = {"172.16.30.145":
                {
                    "username":"root",
                    "password":"123456",
                    "port":22
                },
        "172.16.30.70":
            {
                "username":"root",
                "password": "123456",
                "port": 22
            },
        "172.16.30.74":
            {
                "username":"root",
                "password":"123456",
                "port":22
            }
    }
    a = check_host(_hosts)
    #p = a.get_time()
    n = a.get_time()
    m = a.check_firewall()
    print m
    print "=============="
    print n

