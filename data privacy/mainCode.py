from datetime import datetime
import pandas as pd

basedir = "C:/Users/kshitish/Code Files/data-set-csv.csv"

# Load the data
df = pd.read_csv(basedir)
df

maskedName = []
for name in df["Name"]:
    name = "".join(name.split())
    nameAscList = [str(ord(x)) for x in name]
    finalString = ""
    for i in nameAscList:
        finalString += i
    finalString1 = finalString[::-1]
    # print(finalString1)
    masked = ''
    n = 2
    stringParts = [(finalString1[i:i+n])
                   for i in range(0, len(finalString1), n)]
    # print(stringParts)
    for i in range(int(len(stringParts))):
        a = int(stringParts[i])
        b = a % 26
        c = b + 65
        masked += chr(c)
    maskedName.append(masked)


now = datetime.now()  # current date and time

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
currentdate = day+month+year
print(currentdate)


def shiftrows(n, shift):
    s = str(n)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]


maskedCard=[]
for card,exp in zip(df["Credit Card Number"],df["Expiry-Date"]):
  card = "".join(card.split())
  exp = exp.split("/")[0]+exp.split("/")[1]
  second = "0000"+currentdate+exp
  hash = (int(card)^int(second))
  hash = str(shiftrows(hash,2))
  hash = hash[0:4]+" "+hash[4:8]+" "+hash[8:12]+" "+hash[12::]
  maskedCard.append(hash)

maskedExp = []
for ex in df["Expiry-Date"]:
    then = datetime(2001, 3, 5, 23, 8, 15)        # Random date in the past
    # Now
    now = datetime(int("20"+ex.split("/")[1]),
                   int(ex.split("/")[0]), 28, 12, 12, 12)
    duration = now - then
    days = duration.days                         # Build-in datetime function
    # days  = divmod(duration_in_s, 86400)[0]
    duration_in_s = duration.total_seconds()
    hours = divmod(duration_in_s, 3600)[0]
    maskedExp.append(int(hours))

tokenVault = []
for card, exp in zip(df["Credit Card Number"], df["Expiry-Date"]):
    card = "".join(card.split())
    exp = exp.split("/")[0]+exp.split("/")[1]
    second = "00000000"+exp+exp
    hash = (int(card) ^ int(second))
    hash = str(shiftrows(hash, 2))
    hash = hash[0:4]+" "+hash[4:8]+" "+hash[8:12]+" "+hash[12::]
    tokenVault.append(hash)


maskedData = {"Name": maskedName, "Credit Card Number": maskedCard,
              "Expiry-Date": maskedExp, "CVV": df["CVV"], "Token Vault": tokenVault}

df2 = pd.DataFrame.from_dict(maskedData)


df2["CVV"] = "XXX"


df2.to_csv(r"C:/Users/kshitish/Code Files/finalData5.csv")
