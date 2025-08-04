def alert_if_suspicious(object_detected):
    if object_detected == "gun" or object_detected == "knife" or object_detected == "intruder":
        print("ALERT: Suspicious Activity!")
    else:
        print("All Clear.")

alert_if_suspicious("gun")
alert_if_suspicious("person")
alert_if_suspicious("knife")