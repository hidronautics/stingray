#!/usr/bin/env python

from top_level_actions import AUV
import rospy
import rospkg

def main():
    rospy.init_node("action_test")
    rospack = rospkg.RosPack()
    rospack.list()
    path = rospack.get_path('stingray_pilot')

    auv = AUV()

    # auv.forward_locked(1000, 0.3)      # initial move from base position
    # auv.dive(95)
    #
    # # making a hexagonal "circle". # Done. Working
    # auv.circle(1500)
    #
    # auv.rotate(-180)            # return to base position
    # auv.forward_locked(1000, 0.3)
    # auv.rotate(180)

    # making a dodecagon "circle"
    auv.execute_pattern(path + "/movement_patterns/circle", 1000, 0.4, False, False)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
