rain_list = []
wind_list = []

while True:
    input_string = input("Enter rain and wind separated by a space (or -1 to stop): \n").strip()


    if input_string == "-1.0":
        break


    values = input_string.split()
    if len(values) != 2:
        print("Invalid input. Please enter exactly two numbers separated by a space.")
        continue

    try:
        rain_num, wind_num = map(float, values)
    except ValueError:
        print("Invalid input. Please enter numerical values only.")
        continue


    rain_list.append(rain_num)
    wind_list.append(wind_num)


def avg_rain(rainList):
    return sum(rainList) / len(rainList) if rainList else 0

def avg_wind(windList):
    return sum(windList) / len(windList) if windList else 0

def weather_severity(rain_avg, wind_avg):
    return (rain_avg * 10) + wind_avg


if rain_list:
    average_rain = avg_rain(rain_list)
    average_wind = avg_wind(wind_list)
    days = len(rain_list)
    severity = weather_severity(average_rain, average_wind)


    print(f"The average rain is {average_rain:.1f} inches")
    print(f"The average wind is {average_wind:.1f} mph")
    print(f"The weather severity for these {days} readings is: {severity:.1f}")
else:
    print("No valid readings entered.")