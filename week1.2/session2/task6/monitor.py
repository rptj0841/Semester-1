# Week 1.2, Session 2: Task 6

temperature = int(input("Enter the machine's temperature: "))
pressure = int(input("Enter the machine's pressure: "))
operating_status = int(input("Enter the machine's operational status (1 for operating, 0 for stopped): "))

if temperature > 80:
    print("Temperature too high.")
    print("Recommend shutting down machine.")
elif temperature > 50:
    print("Temperature is within safe limits.")
else:
    print("Temperature is low.")
    print("No action is needed.")


if pressure > 100:
    print("Pressure too high.")
    print("Maintenance is recommended.")
elif pressure > 70:
    print("Pressure is stable.")
else:
    print("Pressure is low.")
    print("Machine is operating normally.")
