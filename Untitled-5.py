import math
def calculate_power_with_factor(Vrms, Irms,angle):
    angle_radians = math.radians(angle)
    power = Vrms * Irms * math.cos(angle_radians)
    return power
Vrms = 10 
Irms = 10   
angle = 30 
power =(Vrms,Irms,angle)
print(f"The power is: {power:.2f} watts")