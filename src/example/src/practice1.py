#! /usr/bin/env python
# coding:utf-8
import rospy
from time import sleep
rospy.init_node("hello_python_node")
print("帳號 ： iclab_xiao_ming666")
s=raw_input("密碼：")
if s=="aa":
   print("歡迎！使用者iclab_xiao_ming666")
else:
   print("密碼或帳號有誤，請重試")
