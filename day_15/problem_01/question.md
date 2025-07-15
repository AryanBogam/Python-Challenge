Q1. Sensor Data Cleaner (IoT/AI use-case)
You get a comma-separated input of temperature sensor data:
"25.4, 27.2, error, 28.1, -300, 26.8"

Clean out invalid values ("error", or values < -50 or > 150)
Convert valid ones to floats
Return list of clean readings