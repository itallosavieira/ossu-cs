text = "X-DSPAM-Confidence:    0.8475"

number_position = text.find(':') + 1
number_striped = text[number_position:len(text)].strip()
number_float = float(number_striped)

print(number_float)