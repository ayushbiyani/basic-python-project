import qrcode as qr
img = qr.make("https://leetcode.com/problemset/all/")
img.save("QR_Code.png")

