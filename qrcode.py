import pyqrcode
from pyqrcode import QRCode
s="https://www.youtube.com/channel/UCE8UOpPsYGMgsniB8IaIJJQ"
url=pyqrcode.create(s)
url.svg("myyoutube.svg", scale = 8) 