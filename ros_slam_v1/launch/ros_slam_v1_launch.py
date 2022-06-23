from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    node = Node(package = "tf2_ros",
            executable = "static_transform_publisher",
            output = "screen",
            arguments = ["0","0","0","0","0","0","odom","camera_link"]
            )
    ld.add_action(node)
    node = Node(package = "tf2_ros",
            executable = "static_transform_publisher",
            output = "screen",
            arguments = ["0","0","0","0","0","0","map","camera_link"]
            )
    ld.add_action(node)
    return ld
