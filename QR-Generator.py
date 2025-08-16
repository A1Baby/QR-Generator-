from wifi_qrcode_generator import wifi_qrcode
qr_code = wifi_qrcode("clcoding", hidden=False,
          authentication_type="WPA", password="CLB422F061")
qr_code_image = qr_code.make_image()
qr_code_image.save("wifi_qr_code.png")
