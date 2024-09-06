from ev3dev2.sensor import Sensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import LargeMotor, OUTPUT_A

# Cria instâncias dos sensores e do motor
distance_sensor = UltrasonicSensor()
motor = LargeMotor(OUTPUT_A)

while True:
    # Lê a distância do sensor
    distance = distance_sensor.distance_centimeters
    
    # Ajusta a velocidade do motor com base na distância
    if distance < 10:
        speed = 0
    else:
        speed = 50
    
    # Define a velocidade do motor
    motor.on(speed=speed)