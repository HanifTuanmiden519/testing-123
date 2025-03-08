def cat_and_mouse(x, y, z):
    distance_a = abs(x - z)  # ระยะทางจาก Cat A ไป Mouse C
    distance_b = abs(y - z)  # ระยะทางจาก Cat B ไป Mouse C

    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"  # ถ้าระยะทางเท่ากัน Mouse หนีได้
