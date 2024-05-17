import serial
from pyPS4Controller.controller import Controller

class MyController(Controller):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Configura la comunicación serial con el Arduino transmisor
        self.serial = serial.Serial('/dev/ttyUSB1', 9600)  # Asegúrate de ajustar la velocidad de baudios según tu configuración

    def send_command_to_arduino(self, command):
        self.serial.write(command.encode())

    def send_button_press_to_arduino(self, button):
        self.send_command_to_arduino(button)

    def on_x_press(self):
        print("on_x_press")
        self.send_button_press_to_arduino('X')

    def on_x_release(self):
        print("on_x_release")

    def on_triangle_press(self):
        print("on_triangle_press")
        self.send_button_press_to_arduino('T')

    def on_triangle_release(self):
        print("on_triangle_release")

    def on_circle_press(self):
        print("on_circle_press")
        self.send_button_press_to_arduino('O')

    def on_circle_release(self):
        print("on_circle_release")

    def on_square_press(self):
        print("on_square_press")
        self.send_button_press_to_arduino('S')

    def on_square_release(self):
        print("on_square_release")

    def on_L1_press(self):
        print("on_L1_press")
        self.send_button_press_to_arduino('L1')

    def on_L1_release(self):
        print("on_L1_release")

    def on_L2_press(self, value):
        print("on_L2_press: ", value)
        self.send_button_press_to_arduino('L2')

    def on_L2_release(self):
        print("on_L2_release")

    def on_R1_press(self):
        print("on_R1_press")
        self.send_button_press_to_arduino('R1')

    def on_R1_release(self):
        print("on_R1_release")

    def on_R2_press(self, value):
        print("on_R2_press: ", value)
        self.send_button_press_to_arduino('R2')

    def on_R2_release(self):
        print("on_R2_release")

    def on_up_arrow_press(self):
        print("on_up_arrow_press")
        self.send_button_press_to_arduino('UP')

    def on_up_down_arrow_release(self):
        print("on_up_down_arrow_release")

    def on_down_arrow_press(self):
        print("on_down_arrow_press")
        self.send_button_press_to_arduino('DOWN')

    def on_left_arrow_press(self):
        print("on_left_arrow_press")
        self.send_button_press_to_arduino('LEFT')

    def on_left_right_arrow_release(self):
        print("on_left_right_arrow_release")

    def on_right_arrow_press(self):
        print("on_right_arrow_press")
        self.send_button_press_to_arduino('RIGHT')

    def on_L3_up(self, value):
        print("on_L3_up: ", value)
        self.send_button_press_to_arduino('L3U')

    def on_L3_down(self, value):
        print("on_L3_down: ", value)
        self.send_button_press_to_arduino('L3D')

    def on_L3_left(self, value):
        print("on_L3_left: ", value)
        self.send_button_press_to_arduino('L3L')

    def on_L3_right(self, value):
        print("on_L3_right: ", value)
        self.send_button_press_to_arduino('L3R')

    def on_R3_up(self, value):
        print("on_R3_up: ", value)
        self.send_button_press_to_arduino('R3U')

    def on_R3_down(self, value):
        print("on_R3_down: ", value)
        self.send_button_press_to_arduino('R3D')

    def on_R3_left(self, value):
        print("on_R3_left: ", value)
        self.send_button_press_to_arduino('R3L')

    def on_R3_right(self, value):
        print("on_R3_right: ", value)
        self.send_button_press_to_arduino('R3R')

    def on_options_press(self):
        print("on_options_press")
        self.send_button_press_to_arduino('OPTIONS')

    def on_options_release(self):
        print("on_options_release")

# Inicia el controlador
MyController(interface="/dev/input/js0").listen()
