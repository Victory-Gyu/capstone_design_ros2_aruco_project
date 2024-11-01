import rclpy, sys, serial
from rclpy.node import Node
from rclpy.qos import QoSProfile

from std_msgs.msg import String



sp  = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
class SubCTRL_MSG(Node):

    def __init__(self):
        super().__init__('sub_lift_msg')
        qos_profile = QoSProfile(depth=10)
        self.subscription = self.create_subscription(
            String, '/lift_ctrl_msg', self.get_ctrl_msg, qos_profile )
        self.ctrl_msg = String()
        

                    
    def get_ctrl_msg(self, msg):
        self.ctrl_msg = msg.data
        
        if self.ctrl_msg == "lift_up":
            sp.write(b'1')
            print("1")
        elif self.ctrl_msg == "lift_down":
            sp.write(b'0')
            print("0")
        
        print(self.ctrl_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SubCTRL_MSG()
    try:    
        #while rclpy.ok():
            #pass
        #sys.exit(1)
        rclpy.spin(node)
    except KeyboardInterrupt:
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
