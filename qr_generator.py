import qrcode

#taking url as input from user 
url = input("Enter the URL to generate QR code: ")

#taking filename as input from user
filename = input("Enter the filename to save the QR code (with .png extension): ")

#check the url is valid or not
if not url.startswith("http://") and not url.startswith("https://"):
    print("Invalid URL. Please enter a valid URL.")
    exit()

#generating qr code
img = qrcode.make(url)

#saving the qr code as png file
img.save(f"{filename}".png)

#displaying the message
print("QR code generated and saved as qr_code.png")