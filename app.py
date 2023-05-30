from PIL import Image
import tkinter as tk

# Открыть изображение карты
map_image = Image.open('map.png')

# Создать окно для отображения карты
root = tk.Tk()
canvas = tk.Canvas(root, width=map_image.width, height=map_image.height)
canvas.pack()

# Отобразить карту на экране
image_tk = tk.PhotoImage(file='map.png')
canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

# координаты углов карты
lat1, lon1 = 55.753215, 37.622504  # верхняя левая точка
lat2, lon2 = 55.745405, 37.636101  # нижняя правая точка

# Размеры карты в пикселях
map_width, map_height = map_image.size


def pixel_to_coords(x, y):
    # Размеры карты в пикселях
    map_width, map_height = map_image.size

    # Широта и долгота углов карты
    lat1, lon1 = 55.753215, 37.622504  # верхняя левая точка
    lat2, lon2 = 55.745405, 37.636101  # нижняя правая точка

    # Преобразование координат из пикселей в градусы широты и долготы
    lat = lat1 - (lat1 - lat2) * y / map_height
    lon = lon1 + (lon2 - lon1) * x / map_width

    return lat, lon

# Обработчик событий клика мыши на изображении
def on_click(event):
    # Получить координаты точки клика
    x = event.x
    y = event.y

    # Преобразовать координаты точки в координаты на карте
    map_x = x * map_image.width // canvas.winfo_width()
    map_y = y * map_image.height // canvas.winfo_height()

    # Преобразовать координаты участка карты в градусы широты и долготы
    lat, lon = pixel_to_coords(map_x, map_y)

    # Вывести координаты участка карты
    print('Координаты участка карты: ({}, {})'.format(lat, lon))


# Привязать обработчик событий клика мыши к изображению
canvas.bind('<Button-1>', on_click)

# Запустить главный цикл приложения
root.mainloop()