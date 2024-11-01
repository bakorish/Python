# Function to check if p equals v times i
#def check_power_equation(p, v, i):
#    return p == v * i
# Function to calculate power

#def calculate_power(voltage, current):
 #   power = voltage * current
  #  return power
#voltage=10  
#current=5 
#power = calculate_power(voltage, current)
#print(f"The power is: {power}")

import math
def calculate_power_with_factor(voltage, current, power_factor_angle):
    angle_radians = math.radians(power_factor_angle)
    power = voltage * current * math.cos(angle_radians)
    return power
voltage = 10 
current = 10   
power_factor_angle = 30 
power = calculate_power_with_factor(voltage, current, power_factor_angle)
print(f"The power is: {power:.2f} watts")
