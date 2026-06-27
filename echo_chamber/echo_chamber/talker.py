import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(Float32, '/random_number', 10)
        self.timer = self.create_timer(1.0, self.publish_number)

    def publish_number(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 100.0)
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data:.2f}')

def main():
    rclpy.init()
    node = TalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()
