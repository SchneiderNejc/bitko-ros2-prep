import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class BitkoExecutor(Node):
    def __init__(self) -> None:
        super().__init__('bitko_executor')
        self.subscription = self.create_subscription(
            String,
            '/bitko/task_cmd',
            self.handle_task,
            10
        )

    def handle_task(self, msg: String) -> None:
        self.get_logger().info(f'BITKO Received <- "{msg.data}" | Navigating to room...')


def main(args=None) -> None:
    rclpy.init(args=args)
    node = BitkoExecutor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
