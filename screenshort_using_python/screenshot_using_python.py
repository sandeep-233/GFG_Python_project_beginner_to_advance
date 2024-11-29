import pyscreenshot as sc

# to capture the whole screen
img = sc.grab()

# to capture part of the screen 
# sc.grab(bbox=(x1, x2, y1, y2))
# img = sc.grab(bbox=(10, 10 , 500, 500))

# to display the captured screenshot
img.show()
# to save the screenshot
img.save("image1.png")