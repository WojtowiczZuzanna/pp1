time_24 = input("Enter time in 24-hour format (hh:mm): ")

if len(time_24) == 5:
    hour = int(time_24[:2])
    minute = int(time_24[3:])
    
    hour in range(0,25)
    minute in range(0,60)

    if 12 < hour <= 24:
        print(f"Time in 12-hour format: {hour - 12}:{minute}pm")
    elif 0 < hour <= 12:
        print(f"Time in 12-hour format: {hour}:{minute}am")
    else:
        print("Invalid time format")
else:
    print("Invalid time format")

