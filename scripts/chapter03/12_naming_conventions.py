"""
Numbers, Variables and Units - Naming Conventions
"""

# Conventional -- every name announces what it is
MAX_CURRENT = 0.02              # a constant
supply_voltage = 5.0            # a variable
led_voltage = 2.0

def series_resistor(v_supply, v_led, current):   # a function
    return (v_supply - v_led) / current

# Inconsistent -- legal, but every name must be investigated
MaxCurrent = 0.02
SupplyVoltage = 5.0
def SeriesResistor(VSupply, VLed, Current):
    return (VSupply - VLed) / Current
