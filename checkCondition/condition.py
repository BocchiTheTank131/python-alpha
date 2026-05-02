temp = range(26,30)
hum = range(70,100)
status = ["Normal", "Alert", "Alarm"]

temp = int(input("Temperature: "))
hum = int(input("Humidity: "))

# Status Normal = temp > 32, hum < 70%
# Status Alert = temp >= 31, 32 and hum >= 65, 66, 67, 68, 69, 70
# Status Alarm = temp >= 26-30, hum >= 70-100

if temp >= 26 and temp <= 30 and hum >= 70 and hum <= 100:
    print("Alarm")
elif temp >= 31 and temp <= 32 and hum >= 65 and hum <= 70:
    print("Alert")
else:
    print("Normal")