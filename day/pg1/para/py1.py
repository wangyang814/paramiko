#!/usr/bin/env python
#! -*-coding:utf-8-*-

#一次性通过用户密码连接
import paramiko
import sys,os

host="192.168.137.111"
user="root"
passwd="centos"

cmd="uname -r"

s=paramiko.SSHClient() #绑定实例
s.load_system_host_keys() #加载本地主机文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #如果本地没有key，可以让它自己加载

s.connect(host,22,user,passwd,timeout=5)
stdin,stdout,stderr=s.exec_command(cmd)
cmd_result=stdout.read(),stderr.read()

for line in cmd_result:
    print line
s.close()
