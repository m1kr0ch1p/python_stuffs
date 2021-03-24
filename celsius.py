try:
    c = float(input("Me dê a temperatura em Celsius:\n"))
    f = (c * (9/5)) + 32
    print("A temperatura em Farenheit é " + str(f) + "°.")
except:
    print("Me dê valores quantitativos")
# (0 °C × 9/5) + 32 = 32 °F