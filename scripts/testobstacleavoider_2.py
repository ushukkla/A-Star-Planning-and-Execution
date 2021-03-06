#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from time import sleep, time


def callback(msg):
   
     # Obstacle detection at left
    print msg.ranges[0]
     # Obstacle detection at left
    print msg.ranges[90]
     # Obstacle detection at center
    print msg.ranges[180]
    # Obstacle detection at right
    print msg.ranges[270]
    # Obstacle detection at right
    print msg.ranges[360]

    if msg.ranges[90]<1.5 and msg.ranges[180]<1.5 and msg.ranges[270]<1.5:
        while msg.ranges[90]!=2.0 and msg.ranges[180]!=2.5:
           speed.linear.x = 0.0
           speed.angular.z = 0.6
           velocity_publisher.publish(speed)
        
        speed.linear.x = 0.0
        speed.angular.z = -1
        time.sleep(5)
        velocity_publisher.publish(speed)
           
    if msg.ranges[90]>1.5 and msg.ranges[180]>1.5 and msg.ranges[360]>1.5:      
         speed.linear.x = 0.5
         speed.angular.z = 0.0


        

       
    




rospy.init_node("samplecodeobsavoid")

pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 30)
sub = rospy.Subscriber('/base_scan', LaserScan, callback)

speed = Twist()

r = rospy.Rate(30)


while not rospy.is_shutdown():
              
        pub.publish(speed)
        r.sleep()  