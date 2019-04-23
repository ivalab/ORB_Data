#!/usr/bin/env python
import sys
import roslib;
import rospy
import rosbag
from rospy import rostime
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(
        prog = 'extract_odom.py',
        description='Convert the odom message in a bagfile to TUM trajectory text.')
    parser.add_argument('-t', type=str, help='odom message name', 
        default = None, metavar = "odom_topic")
    parser.add_argument('-o', type=str, help='name of the output file', 
        default = None, metavar = "output_file")
    parser.add_argument('bagfile', type=str, help='path to a bagfile')
    args = parser.parse_args()
    return args



def odom_convert(bagfile, odom_topic, outfile):
    # 
    text_file = open(outfile, "w")
    #try:
    for topic, msg, t in rosbag.Bag(bagfile).read_messages(topics=odom_topic):
    	time_stamp = msg.header.stamp.secs + msg.header.stamp.nsecs * 1e-9
    	position = [msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z]
    	quaternion = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
        print "odom message: %f, %f, %f, %f, %f, %f, %f, %f" % (time_stamp, position[0], position[1], position[2], quaternion[0], quaternion[1], quaternion[2], quaternion[3])
        text_file.write("%0.6f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f\n" %  (time_stamp, position[0], position[1], position[2], quaternion[0], quaternion[1], quaternion[2], quaternion[3]))
    #finally:
    text_file.close()


def odom_with_vel_convert(bagfile, odom_topic, outfile):
    # 
    text_file = open(outfile, "w")
    #try:
    for topic, msg, t in rosbag.Bag(bagfile).read_messages(topics=odom_topic):
    	time_stamp = msg.header.stamp.secs + msg.header.stamp.nsecs * 1e-9
    	position = [msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z]
    	quaternion = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
	velocity = [msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.linear.z]
	angular_rate = [msg.twist.twist.angular.x, msg.twist.twist.angular.y, msg.twist.twist.angular.z]
        print "odom message: %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f" % (time_stamp, position[0], position[1], position[2], quaternion[0], quaternion[1], quaternion[2], quaternion[3], velocity[0], velocity[1], velocity[2], angular_rate[0], angular_rate[1], angular_rate[2])
        text_file.write("%0.6f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f %0.8f\n" %  (time_stamp, position[0], position[1], position[2], quaternion[0], quaternion[1], quaternion[2], quaternion[3], velocity[0], velocity[1], velocity[2], angular_rate[0], angular_rate[1], angular_rate[2]))
    #finally:
    text_file.close()


if __name__ == "__main__":
    args = parse_args()
    if args.t == None:
        print "odom message name required!"
        raise SystemExit()
    if args.o == None:
        print "name of the output file required!"
        raise SystemExit()
   # odom_convert(args.bagfile, 
   #     odom_topic = args.t, 
   #     outfile = args.o)
    odom_with_vel_convert(args.bagfile, 
        odom_topic = args.t, 
        outfile = args.o)
