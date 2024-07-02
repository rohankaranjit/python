


def calculate_damage(damage, speed, time_unit):
    time_units_in_seconds = {
        "second": 1,
        "minute": 60,
        "hour": 3600
    }
    
    if time_unit not in time_units_in_seconds:
        return "Invalid time unit"
    
    total_seconds = time_units_in_seconds[time_unit]
    total_damage = damage * speed * total_seconds
    
    return total_damage

print(calculate_damage(40, 5, "second"))  
print(calculate_damage(100, 1, "minute"))  
print(calculate_damage(2, 100, "hour"))  
    time_units_in_seconds = {
        "second": 1,
        "minute": 60,
        "hour": 3600
    }
    
    if time_unit not in time_units_in_seconds:
        return "Invalid time unit"
    
    total_seconds = time_units_in_seconds[time_unit]
    total_damage = damage * speed * total_seconds
    
    return total_damage

print(calculate_damage(40, 5, "second"))  
print(calculate_damage(100, 1, "minute"))  
print(calculate_damage(2, 100, "hour"))  
