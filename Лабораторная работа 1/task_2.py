# TODO Найдите количество книг, которое можно разместить на дискете
SIZE = 1024
disk_volume = 1.44
page_count = 100
count_str = 50
count_symbol = 25
weight_symbol = 4
print("Количество книг, помещающихся на дискету:",
      int(disk_volume * SIZE * SIZE // (page_count * count_str * count_symbol * weight_symbol)))
