def calculate_hour_angle(h, m, s):

    if not (0 < h <= 23 and 0 <= m < 60 and 0 <= s < 60):
        raise ValueError("Некорректные значения времени.")

    if h >= 12:
        h -= 12

    angle = (h * 30) + (m * 0.5) + (s * (0.5 / 60))

    return angle


h = int(input("Введите часы (0 < h ≤ 23): "))
m = int(input("Введите минуты (0 ≤ m < 60): "))
s = int(input("Введите секунды (0 ≤ s < 60): "))

try:
    angle = calculate_hour_angle(h, m, s)
    print("Угол между часовыми стрелками:", angle, "градусов")
except ValueError as e:
    print(e)
