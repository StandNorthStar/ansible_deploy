#!/usr/bin/python
# coding=utf-8

from pyghmi.ipmi.command import Command
from pyghmi.ipmi.sdr import SDR
from ipdb import set_trace

#set_trace()


def all_info(func):
    def detail_info(measure,result):
        newvalue = {}
        for value in result:
            if measure in value.get('name'):
                 newvalue[value.get('name')] = value.get('value')
        return newvalue
    return detail_info

class IPMI(object):
    def __init__(self,bmc,userid,password):
        self.bmc = bmc
        self.userid = userid
        self.password = password
        self.con_command = Command(bmc=self.bmc, userid=self.userid, password=self.password)

    def info(self):
        # 1 FangAn
        #result = [i for i in self.con_command.get_sensor_data()]
        #return result

        # 2 FangAn
        #sdr = SDR(self.con_command)
        # result = []
        # for number in sdr.get_sensor_numbers():
        #     rsp = self.con_command.raw_command(command=0x2d, netfn=4, data=(number,))
        #
        #     if 'error' in rsp:
        #         continue
        #
        #     reading = sdr.sensors[number].decode_sensor_reading(rsp['data'])
        #     end = {}
        #     if reading is not None:
        #         value = eval(repr(reading))
        #         result.append(value)
        # return result
        result = [i for i in self.con_command.get_inventory()]
        return result


    def power_status(self):
        status = self.con_command.get_power()
        return status

    def p_user(self):
        user = self.con_command.get_users()
        for i in user.keys():
            uid = user[i].get('uid')
            result = self.con_command.get_user_access(uid)
        return result


# @all_info
# def cpu_info(cpu_in,result):
#     pass
#
# @all_info
# def mem_info(mem,result):
#     pass
#
# @all_info
# def fan(fan_in,result):
#     pass

# def detail():
#     pass

if __name__ == '__main__':
    bmc = '192.168.88.199'
    userid = 'root'
    password = 'admin'

    a = IPMI(bmc=bmc,userid=userid,password=password)
    k  = a.info()
    print k
    # print mem_info('-DIMM',result)
    # print cpu_info('CPU',result)
    # print fan('FAN',result)
    # print a.power_status()
    # print a.p_user()