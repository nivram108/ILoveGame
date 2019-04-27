import win32gui
import win32ui 
import win32con
from PIL import Image

def screenshot():
	windowname = 'Windows 7 x64 - VMware Workstation 12 Player (Non-commercial use only)'
	bmpfilenamename = 'src/screenshot.bmp'

	hwnd = win32gui.FindWindow(None, windowname)
	wDC = win32gui.GetWindowDC(hwnd)

	w = 800
	h = 676
	dcObj=win32ui.CreateDCFromHandle(wDC)
	cDC=dcObj.CreateCompatibleDC()
	dataBitMap = win32ui.CreateBitmap()
	dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
	cDC.SelectObject(dataBitMap)
	cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
	dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
	# Free Resources
	dcObj.DeleteDC()
	cDC.DeleteDC()
	win32gui.ReleaseDC(hwnd, wDC)
	win32gui.DeleteObject(dataBitMap.GetHandle())
	#transfer to jpg

	img = Image.open('A:/sort_art_online/src/screenshot.bmp')
	img.save('A:/sort_art_online/src/screenshot.jpg', 'jpeg')