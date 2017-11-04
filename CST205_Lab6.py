#!/usr/bin/python
'''
Team 5 Hopper
CST205-40_FA17 Lab #6
November 1st 2017
'''

# Try to match requirments from assignment
def range(input):
  if input < 64:
    return 31
  elif input < 128:
    return 95
  elif input < 192:
    return 159
  elif input < 256:
    return 223


class image(object):
  def __init__(self, pic=None):
    '''
    Create a new image object
    '''
    if pic == None:
      self.getPic() # If an image is not passed in load one now

  def revertPic(self):
      self.pic = makePicture(self.filename) # reload the image

  def displayPic(self):
    repaint(self.pic)    # Display loaded image

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
      newR = 0.393 * r + 0.769 * g + 0.189 * b
      newG = 0.349 * r + 0.686 * g + 0.168 * b
      newB = 0.272 * r + 0.534 * g + 0.131 * b
      setRed(p, newR)
      setGreen(p, newG)
      setBlue(p, newB)

  # Problem 2, Jose to solve
  def ArtIFy(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      setRed(p, range(r))
      setGreen(p, range(g))
      setBlue(p, range(b))

  # Problem 3, Gabe initial solution, Grace Optimize
  def GreenScreen(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      if g > r and g > b:
        g = 255
        b = 255
        r = 255
      setRed(p, r)
      setGreen(p, g)
      setBlue(p, b)


def main():

  #Problem 1,
  sepia_test_image = image()
  sepia_test_image.Sepia()
  sepia_test_image.displayPic()

  #Problem 2,
  artify_test_image = image()
  artify_test_image.ArtIFy()
  artify_test_image.displayPic()

  #Problem 3,
  green_Screen_test_image = image()
  green_Screen_test_image.GreenScreen()
  green_Screen_test_image.displayPic()

main()