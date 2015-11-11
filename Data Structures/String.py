text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(':')
number = float(text[colon+1:])
print(number)
