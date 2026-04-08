temps = [28.5,31.0,29.8,33.5,27.0,35.2,30.0]

for temp in temps:
    if temp > 30.0:
        print(f"ALERTA: temperatura critica! ({temp}")
    else:
        print(f"temperatura normal! ({temp})")