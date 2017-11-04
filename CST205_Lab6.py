#!/usr/bin/python
'''
Team 5 Hopper
CST205-40_FA17 Lab #6
November 1st 2017
'''

def range(input):
  if input < 64:
    return 31
  elif input < 128:
    retun 95
  elif input < 192:
    retun 159
  elif input < 256:
    retun 223


class image(object):
  def __init__(self, pic=None):
    if pic == None:
      self.getPic()

  def revertPic(self):
      self.pic = makePicture(self.filename)

  def displayPic(self):
    repaint(self.outPic)

  def getPic(self):
    self.filename = pickAFile()
    self.pic = makePicture(self.filename)

  def Sepia(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      newR = 0.393r + 0.769g + 0.189b
      newG = 0.349r + 0.686g + 0.168b
      newB = 0.272r + 0.534g + 0.131b
      setRed(p, newR)
      setGreen(p, newG)
      setBlue(p, newB)

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

  def GreenScreen(self):
    assert(self.pic)
    pixels = getPixels(self.pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      setRed(p, r)
      setGreen(p, g)
      setBlue(p, b)


def main():
  test_image = image()

  #Problem 1,
  test_image.Sepia()
  test_image.displayPic()

  #Problem 2,
  test_image.revertPic()
  test_image.ArtIFy()
  test_image.displayPic()

  #Problem 3,
  test_image.revertPic()
  test_image.GreenScreen()
  test_image.displayPic()

main()