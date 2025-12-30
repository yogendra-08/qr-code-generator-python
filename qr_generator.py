import qrcode

#taking url as input from user 

url = input("Enter the URL to generate QR code: ")

img = qrcode.make(url)

img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")