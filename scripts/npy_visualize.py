#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import std_msgs.msg
import sensor_msgs.point_cloud2 as pcl2
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2, PointField

import os, os.path
import numpy as np


class NPY_TO_ROS():
	def __init__(self, npy_path='', npy_file_list=''):
		self.npy_path = npy_path
#		self.npy_files_list_xyz = [name for name in os.listdir(self.npy_path)]
		self.npy_file_list = open(npy_file_list,'r').read().split('\n')
		
		self.npy_files = []
		for i in range(len(self.npy_file_list)-1):
			self.npy_files.append(self.npy_path + self.npy_file_list[i])

		self.len_files = len(self.npy_files)

		print("[+] There are {} .npy files".format(self.len_files))

		self.velo_pub = rospy.Publisher('/lidar_points', PointCloud2, queue_size=1)
		self.loop_rate = rospy.Rate(5)

		self.processing_xyz()


	def processing_xyz(self):
		for i in range(self.len_files):
			print("[+] {} th file name : {} ".format(i, self.npy_files[i]))
			bin_points = np.load(os.path.join(self.npy_path,self.npy_files[i])).reshape(-1,3)

			pc2_msg = PointCloud2()

			header = std_msgs.msg.Header()
			header.stamp = rospy.Time.now()
			header.frame_id = 'lidar_link'

			cloud_points = []

			cloud_points = np.true_divide(bin_points,1)

			pc2_msg = pcl2.create_cloud_xyz32(header, cloud_points)

			# ed: /velodyne_points_npy publish
			self.velo_pub.publish(pc2_msg)
			self.loop_rate.sleep()

			if rospy.is_shutdown():
				return



if __name__ == '__main__':
    rospy.init_node('npy_visualizer')

    npy_path = rospy.get_param('npy_path')
    npy_file_list = rospy.get_param('npy_file_list')

    npy_to_ros = NPY_TO_ROS(npy_path=npy_path, npy_file_list=npy_file_list)