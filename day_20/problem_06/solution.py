def airpods_troubleshooter(connected, battery, error):
    if not connected:
        return "Reconnect via Bluetooth settings."
    if battery < 10:
        return "Charge your AirPods."
    if error:
        return "Reset AirPods and try again."
    return "AirPods are working fine."

# Example call
print(airpods_troubleshooter(connected=False, battery=80, error=False))
