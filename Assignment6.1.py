text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(' ')
text1 = text[pos:]
text1 = text1.strip()
output = float(text1)
print(output)