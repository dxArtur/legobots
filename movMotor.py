from ev3dev2.motor import LargeMotor, OUTPUT_A

# Cria uma instância do motor
motor = LargeMotor(OUTPUT_A)

# Gira o motor para frente
motor.on_for_seconds(speed=50, seconds=2)

# Para o motor
motor.off()

# Gira o motor para trás
motor.on_for_seconds(speed=-50, seconds=2)

# Para o motor
motor.off()
