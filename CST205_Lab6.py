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


def artRange(input):
  '''
  The artify transform requires a somewhat
  abritray transform of an input value
  preform that transform here
  '''
  if input < 64:
    return 31
  elif input < 128:
    return 95
  elif input < 192:
    return 159
  elif input < 256:
    return 223


def capValueByte(value):
  '''
  Keep a value in the range of valid values
  for a byte.
  '''
  if value > 255:
    return 255
  elif value < 0:
    return 0
  return value


class image(object):
  '''
  The image object will prompt the operator for an image upon creation
  Once the image object has a valid image, it can apply transforms,
  display or reload the image
  '''
  def __init__(self, pic=None):
    '''
    Create a new image object
    '''
    self.filename = None
    if pic == None:
      self.getPic() # If an image is not passed in load one now

  def revertPic(self):
    '''
    Reload what eve image was loaded last
    if a picture has not been loaded yet
    have the operator select one.
    '''
    if self.filename == None:
      self.getPic()
    else:
      self.pic = makePicture(self.filename)

  def displayPic(self):
    '''
    Have image object display itself
    '''
    repaint(self.pic)

  def getPic(self):
    self.filename = pickAFile()
    self.pic = makePicture(self.filename)   # put up user selection dialog

  # Problem One, Christian to solve
  def Sepia(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      # These values below are not from the assingment, just an aprox to get started
      newR = capValueByte(0.393 * r + 0.769 * g + 0.189 * b)
      newG = capValueByte(0.349 * r + 0.686 * g + 0.168 * b)
      newB = capValueByte(0.272 * r + 0.534 * g + 0.131 * b)
      setRed(p, newR)
      setGreen(p, newG)
      setBlue(p, newB)

  def betterBnW(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      l =  r*0.299 + g*0.587 + b*0.114
      setRed(p, l)
      setGreen(p, l)
      setBlue(p, l)

  # Problem 2, Jose to solve
  def ArtIFy(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
    for p in pixels:
      # Fetch the existing pixel values and pass them
      # to the transform before setting to the new val
      setRed(p, artRange(getRed(p)))
      setGreen(p, artRange(getGreen(p)))
      setBlue(p, artRange(getBlue(p)))
    if r < 64:
      setRed (p, 31)
    elif r < 128:
      setRed (p, 95)      
    elif r < 192:
      setRed (p, 159)
    else:
      setRed (p, 223)
    if g < 64:
      setGreen (p, 31)
    elif g < 128:
      setGreen (p, 95)      
    elif g < 192:
      setGreen (p, 159)
    else:
      setGreen(p, 223)
    if b < 64:
      setBlue (p, 31)
    elif b < 128:
      setBlue (p, 95)      
    elif b < 192:
      setBlue (p, 159)
    else:
      setBlue (p, 223)
  # Problem 3, Gabe initial solution, Grace Optimize or add
  #background underlay
  def GreenScreen(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
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
        #otherwise we leave them alone
        setRed(p, r)
        setGreen(p, g)
        setBlue(p, b)



def main():
  '''
  Just step through each of the problems
  if focusing on one, comment out the others.
  '''
  '''
  #Problem 1,
  sepia_test_image = image()
  sepia_test_image.Sepia()
  sepia_test_image.displayPic()

  #Problem 2,
  artify_test_image = image()
  artify_test_image.ArtIFy()
  artify_test_image.displayPic()
  '''
  #Problem 3,
  green_Screen_test_image = image()
  green_Screen_test_image.GreenScreen()
  green_Screen_test_image.displayPic()

# This way we will run by clicking the load button instead
#of needing to type a entry function every time
main()
