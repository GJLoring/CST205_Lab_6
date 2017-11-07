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

#Christian

#Need help, I couldn't figure out how to pass the black and white 
#picture from the betterBnW function to the sepia function.  Is that even possible?

#What I done below is to first create a black and white picture by 
#by calling the BnW function inside the sepia function, it works but I don't think
#its the most efficient method

#per assignment requirements, only need to change the red and blue pixels values.

#creates a sepia-tone picture, it requires a black and white picture
def Sepia():
  print("calling Sepia")
  bw_pic = betterBnW(pic)
  pixels = getPixels(bw_pic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
  
    #value multiplier for red
    if r < 63:
      newR = 1.1 * r
    elif r > 62 and r < 192:
      newR = 1.15 * r
    else:
      newR = 1.08 * r 
      if newR > 255:
        newR = 255

    #value multiplier for blue
    if b < 63:
      newB = 0.9 * b
    elif b > 62 and b < 192:
      newB = 0.85 * b
    else:
      newB = 0.93 * b

    setRed(p, newR)
    setBlue(p, newB)

#creates a black and white picture
def betterBnW(pic):
  print("calling betterBnW")
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l =  r*0.299 + g*0.587 + b*0.114
    setRed(p, l)
    setGreen(p, l)
    setBlue(p, l)
  return pic
    
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
def chromaKey(pic, bgpic):
  pixels = getPixels(pic)
  bgPixels = getPixels(bgpic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    #l =  r*0.299 + g*0.587 + b*0.114
    # Green should dominate both red and green, by scaling the
    # value for gree, before comparing g * 0.75 we can then make sure
    # it exceeds levels of blue and red by a decent margin
    # There can be a lot of noise in dark areas of the image
    # so l > 64 makes sure we have a bright enough pixel to judge
    #if (g*0.75 > r) and (g*0.75 > b) and (l > 64) :
    if g > (b + r):
      # For testing just set flagged pixels to a magenta
      # that is not likely to occur by chance in the image
      # and will make flagged pixels easy to spot
      #g = 0
      #b = 255
      #r = 255
      # Only set the pixel value if it is a flagged one
      #otherwise we leave them alone this should be replaced with
      # a look up from the same x,y location in another image
      #that is atleast as tall and wide
      #setRed(p, r)
      #setGreen(p, g)
      #setBlue(p, b)
      setColor(p, getColor(getPixel(bgpic, getX(p), getY(p))))




#Problem 1,
filename = pickAFile()
pic = makePicture(filename)
Sepia()
repaint(pic)


  #Problem 2,
filename = pickAFile()
pic = makePicture(filename)
ArtIFy(pic)
repaint(pic)

  #Problem 3,
filename = pickAFile()
pic = makePicture(filename)
background = pickAFile()
bgpic = makePicture(background)
chromaKey(pic, bgpic)
repaint(pic)
