import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.sub = self.create_subscription(
            Float32, '/random_number', self.on_receive, 10)

    def on_receive(self, msg):
        received = msg.data
        multiplied = received * 2
        self.get_logger().info(
            f'Received: {received:.2f}. Multiplied value: {multiplied:.2f}')

def main():
    rclpy.init()
    node = ListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()
