input_time = int(input("Enter the time to convert: "))

hours = input_time // 3600
remainder = input_time % 3600

minutes = remainder // 60
seconds = remainder % 60

print(f"{hours}:{minutes}:{seconds}")
print("{hours}:{minutes}:{seconds}")
print(hours, minutes, seconds, sep = ':')
