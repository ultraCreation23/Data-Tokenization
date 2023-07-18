import pandas as pd
# from google.colab import drive

basedir = "C:/Users/kshitish/Code Files/data-set-csv.csv"

#Load the data
df = pd.read_csv(basedir)
for name in df["Name"]:
  name = "".join(name.split())
  nameAscList = [str(ord(x)) for x in name]
  finalString = ""
  for i in nameAscList:
      finalString += i
  finalString1 = finalString[::-1]
  #print(finalString1)
  masked = ''
  n=2
  stringParts = [(finalString1[i:i+n]) for i in range(0, len(finalString1), n)]
  #print(stringParts)
  for i in range(int(len(stringParts))):
      a = int(stringParts[i])
      b = a%26
      c = b + 65
      masked += chr(c)

  print(masked)
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
currentdate = day+month+year
print(currentdate)
def test(n, shift):
    s = str(n)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]

maskedCard = []
for card,exp in zip(df["Credit Card Number"],df["Expiry-Date"]):
  card = "".join(card.split())
  exp = exp.split("/")[0]+exp.split("/")[1]
  second = "0000"+currentdate+exp
  hash = (int(card)^int(second))
  maskedCard.append(hash)

