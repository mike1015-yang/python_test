#! /usr/bin/env python
# coding:utf-8
import rospy
from time import sleep
rospy.init_node("hello_python_node")
n=10
while n>0:
   if n==1:
      sleep(1)
      print("幫你撐十秒囉！！")
      n-=1
   elif n>1:
      sleep(1)
      print(n)
      n-=1
