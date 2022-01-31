import qrcode

website = "http://172.20.10.10:5000/"

filename = "site.png"

img = qrcode.make(website)

img.save(filename)