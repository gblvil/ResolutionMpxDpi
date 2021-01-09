height_res = int(input("Insert Height Pixels: "))
width_res = int(input("Insert Width Pixels: "))
dpi = int(input("Dpi: "))


# 1px in cm = 0.042333333 for 60 dpi
# 1px in cm = 0.026458333 for 96 dpi
# 1px in cm = 0.021166667 for 120 dpi
# 1px in cm = 0.018814815 for 135 dpi
# 1px in cm = 0.016933333 for 150 dpi
# 1px in cm = 0.014111111 for 180 dpi
# 1px in cm = 0.011545455 for 220 dpi
# 1px in cm = 0.008466667 for 300 dpi


try:
    if dpi == 60:
        one_px = 0.042333333
    elif dpi == 96:
        one_px = 0.026458333
    elif dpi == 120:
        one_px = 0.021166667
    elif dpi == 135:
        one_px = 0.018814815
    elif dpi == 150:
        one_px = 0.016933333
    elif dpi == 180:
        one_px = 0.014111111
    elif dpi == 220:
        one_px = 0.011545455
    elif dpi == 300:
        one_px = 0.008466667
    else:
         "Please insert correct dpi: 60, 96, 120, 135, 150, 180, 220, 300"

    calculate_h = height_res * one_px
    calculate_w = width_res * one_px

    pixel_x = dpi * calculate_w / 25.4
    pixel_y = dpi * calculate_h / 25.4

    resolution = pixel_x * pixel_y / 10000
    print("Your resolution have", str(resolution)[0:4], "Mpx")
    print("Float accuracy: ", resolution, "Mpx for dpi: ", dpi)

except NameError:
    print("Please insert correct dpi: 60, 96, 120, 135, 150, 180, 220, 300")






