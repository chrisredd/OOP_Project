import Snowboarding

class SlopeStyle(Snowboarding):
  mgold = "CAN Max Parrot"
  msilver = "CHN Yiming SU"
  mbronze = "CAN Mark Mcmorris"
  wgold = "NZL Zoi Sadowski"
  wsilver = "USA Julia Marino"
  wbronze = "AUS Tess Coady"
  def __init__(self, venue:str, scorestyle:str) -> None:
    super().__init__(self, venue, scorestyle)
    
  def __str__(self)->str:
  