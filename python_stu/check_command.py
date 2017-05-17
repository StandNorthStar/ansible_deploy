#!/usr/bin/python
# coding=utf-8

import os

from collections import namedtuple
from ansible.vars import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.inventory import Inventory, Host, Group
from ansible.playbook.play import Play
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager

class My_inventory(Inventory):

    def __init__(self,resource, loader, variable_manager):
        '''
        resource :是一个字典格式 ，其实这个里面主要是 groups对应的主机地址，端口，用户名和密码
        loader : what ~~
        variable_manager:
        '''
        self.resource = resource
        self.inventory = Inventory(loader = loader,variable_manager= variable_manager)
        self.get_inventory()

    def get_inventory():
        '''
        把 hosts 加入到 inventory 中。
        :return:
        '''
        # resource 如果是一个列表，表示没有组，只有主机信息。把它加入到默认组中。
        if isinstance(self.resource,list):
            self.add_group(self.resource,'default_group')
        elif isinstance(self.resource,dict):
            for groupname,hosts_vars in self.resource.iteritems():
                self.add_group(hosts_vars.get("hosts"),groupname,hosts_vars.get("vars"))


    def add_group(self, hosts ,groupname, groupvars = None):
        '''
        把 hosts 加入到 group 中
        '''

        my_group = Group(name=groupname)

        # 默认是没有组变量（groupvars = None）,如果有组变量
        if groupvars:
            for  key, value  in groupvars.iteritems():
                # 设置组的变量
                my_group.set_variable(key,value)

        # 获取hosts , hosts应该是一个字典格式。host的key也是一个字典
        for host in hosts:

            hostname = host.get("hostname")
            hostip = host.get("ip",hostname)
            hostport = host.get("port")
            username = host.get("username")
            password = host.get("password")
            ssh_key = host.get("ssh_key")

            # 创建ansible host实例
            my_host = Host(name=hostname,port=hostport)
            my_host.set_variable('ansible_ssh_host', hostip)
            my_host.set_variable('ansible_ssh_port', hostport)
            my_host.set_variable('ansible_ssh_user', username)
            my_host.set_variable('ansible_ssh_pass', password)
            my_host.set_variable('ansible_ssh_private_key_file',ssh_key)

            # 设置其他的 host的变量
            for key ,value in host.iteritems():
                if key not in ['hostname','port','username','password']:
                    my_host.set_variable(key,value)

            # 把我当前获取到的host信息加入到组中。
            my_group.add_host(my_host)

        # 把这个组加入到 inventory 中。
        self.inventory.add_group(my_group)


class MyRunner(object):

    def __init__(self,resource,*args,**kwargs):
        self.resource = resource
        self.inventory = None
        self.variable_manager = None
        self.loader = None
        self.options = None
        self.passwords = None
        self.callback = None
        self.results = {}
        self._initansible()

    def _initansible(self):
        """
        初始化ansible
        :return:
        """

        # namedtuple 给元祖命名，防止由于索引出错。(里面给出的都是一个自定义的变量)
        options = namedtuple("options",['connection','module_path','forks','timeout','remote_user',
                                        'ask_pass','private_key_file','ssh_common_args','ssh_extra_args',
                                        'sftp_extra_args','scp_extra_args','become','become_method','become_user',
                                        'ask_value_pass','verbosity','check','listhosts','listtasks','listtags','syntax'
                                        ])

        # 初始化需要的对象
        self.variable_manager = VariableManager()
        # 转化为json 对象的工具
        self.loader = DataLoader()
        self.OPTION = options(connection='smart',module_path='/usr/share/ansible',forks=100,
                              timeout=10,remote_user='root',ask_pass=False,private_key_file=None,
                              ssh_common_args=None,ssh_extra_args=None,sftp_extra_args=None,scp_extra_args=None,
                              become=None,become_method=None,become_user='root',ask_value_pass=None,verbosity=None,
                              check=False,listhosts=False,listtasks=False,listtags=False,syntax=False
                              )
        self.passwords = dict(sshpass=None,becomepass=None)
        self.inventory = My_inventory(self.resource,self.loader,self.variable_manager).inventory
        self.variable_manager.set_inventory(self.inventory)

    def run(self,host_list,module_name,module_args ):
        '''


        :param host_list:
        :param module_name:
        :param module_args:
        :return:
        '''
        play_source = dict(
            name="Ansible Play",
            hosts=host_list,
            gather_facts = 'no',
            tasks=[dict(action=dict(module=module_name,args=module_args))]
        )

        play = Play().load(play_source,variable_manager=self.variable_manager,loader=self.loader)
        #c
        tqm = None
        # 获取结果
        self.callback = ResultsCollector()
        try:
            tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.OPTION,
                passwords=self.passwords
            )
            tqm._stdout_callback = self.callback
            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()

    def run_playbook(self,host_list,):





def check_command(command_list):

    check_list = []
    for command in command_list:

        command_path = os.popen("which"+ command,).read().strip()
        if command_path is not None:
            check_list.append(command_path)

    return check_list




