#!/usr/bin/python
'''
Team 5 Hopper
    Jose Garcia Ledesma
    Grace Alvarez
    Christian Guerrero
    Gabriel Loring
CST205-40_FA17 Lab #6
November 1st 2017
'''

# Problem One, Christian to solve
def Sepia(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    # These values below are not from the assingment, just an aprox to get started
    newR = 0.393 * r + 0.769 * g + 0.189 * b
    newG = 0.349 * r + 0.686 * g + 0.168 * b
    newB = 0.272 * r + 0.534 * g + 0.131 * b
    if newR > 255:
      newR = 255
    if newG > 255:
      newG = 255
    if newB > 255:
      newB = 255
    setRed(p, newR)
    setGreen(p, newG)
    setBlue(p, newB)

def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l =  r*0.299 + g*0.587 + b*0.114
    setRed(p, l)
    setGreen(p, l)
    setBlue(p, l)

# Problem 2, Jose to solve
def ArtIFy(pic):
  pixels = getPixels(pic)
  for p in pixels:
    # Fetch the existing pixel values and pass them
    # to the transform before setting to the new val
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if r < 64:
      setRed(p, 31)
    elif r < 128:
      setRed(p, 95)
    elif r < 192:
      setRed(p, 159)
    else:
      setRed(p, 223)
    if g < 64:
      setGreen(p, 31)
    elif g < 128:
      setGreen(p, 95)
    elif g < 192:
      setGreen(p, 159)
    else:
      setGreen(p, 223)
    if b < 64:
      setBlue(p, 31)
    elif b < 128:
      setBlue (p, 95)
    elif b < 192:
      setBlue(p, 159)
    else:
      setBlue(p, 223)

# Problem 3, Gabe initial solution, Grace Optimize or add
#background underlay
def chromaKey(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l =  r*0.299 + g*0.587 + b*0.114
    # Green should dominate both red and green, by scaling the
    # value for gree, before comparing g * 0.75 we can then make sure
    # it exceeds levels of blue and red by a decent margin
    # There can be a lot of noise in dark areas of the image
    # so l > 64 makes sure we have a bright enough pixel to judge
    if (g*0.75 > r) and (g*0.75 > b) and (l > 64) :
      # For testing just set flagged pixels to a magenta
      # that is not likely to occur by chance in the image
      # and will make flagged pixels easy to spot
      g = 0
      b = 255
      r = 255
      # Only set the pixel value if it is a flagged one
      #otherwise we leave them alone this should be replaced with
      # a look up from the same x,y location in another image
      #that is atleast as tall and wide
      setRed(p, r)
      setGreen(p, g)
      setBlue(p, b)




#Problem 1,
filename = pickAFile()
pic = makePicture(filename)
Sepia(pic)
repaint(pic)


  #Problem 2,
filename = pickAFile()
pic = makePicture(filename)
ArtIFy(pic)
repaint(pic)

  #Problem 3,
filename = pickAFile()
pic = makePicture(filename)
chromaKey(pic)
repaint(pic)
