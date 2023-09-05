def main():
    past_temp = 70
    current_temp = past_temp
    k = 0.019
    ambient_temperature = 20
    change_in_time = 2
    for i in range(0, 21, 2):
        derivative = -k * (current_temp - ambient_temperature)
        current_temp = past_temp + (derivative * change_in_time)
        print(current_temp)
        past_temp = current_temp

if __name__ == "__main__":
    main()