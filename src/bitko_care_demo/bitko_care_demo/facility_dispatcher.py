import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class FacilityDispatcher(Node):
    def __init__(self) -> None:
        super().__init__('facility_dispatcher')
        self.publisher_ = self.create_publisher(String, '/bitko/task_cmd', 10)
        self.timer = self.create_timer(3.0, self.publish_task)
        self.task_count = 0

    def publish_task(self) -> None:
        self.task_count += 1
        msg = String()
        msg.data = f"TASK #{self.task_count}: Hydrate check at Room 104"
        self.publisher_.publish(msg)
        self.get_logger().info(f'PRO.4 Sent -> "{msg.data}"')


def main(args=None) -> None:
    rclpy.init(args=args)
    node = FacilityDispatcher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
