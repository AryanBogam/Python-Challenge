def check_missing(hours_recorded):
    expected = 24
    actual = len(hours_recorded)
    
    if actual < expected:
        missing = expected - actual
        print(f"Missing footage for {missing} hour(s)")
    else:
        print("All footage present")

test_data = ["ok"] * 22
check_missing(test_data)

test_data2 = ["ok"] * 24
check_missing(test_data2)