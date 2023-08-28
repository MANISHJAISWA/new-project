import qrcode
features = qrcode.QRCode(version = 10,box_size = 8,border = 3)
features.add_data("https://www.geeksforgeeks.org/full-adder-in-digital-logic/")
features.make(fit=True)
generate_image = (features.make_image(fill_color ="blue",back_color = "black"))
generate_image.save('image5.png')
