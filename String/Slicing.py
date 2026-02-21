username = "Spotify"
print(username[0:3])
print(username[0:])
print(username[:3])
print(username[-1:3])
print(username[0:-1])
words = ["I", "love", "Python"]
result = " ".join(words)
print(result)
print(list[result])
# 1️⃣ strip()
# Removes spaces (or specified characters) from both sides of a string.
text1 = "   Hello Python   "
print(text1.strip())
# Remove specific character:
text2 = "###Hello###"
print(text2.strip("#"))
# 2️⃣ lstrip()
# Removes characters from the left side only.
text3 = "   Hello"
print(text3.lstrip())
# 3️⃣ rstrip()
# Removes characters from the right side only.
text4 = "Hello   "
print(text4.rstrip())
# 4️⃣ split()
# Breaks a string into a list.
text5 = "I love Python"
print(text5.split())
# Split using comma
text6 = "apple,banana,mango"
print(text6.split(","))

# 5️⃣ partition()
# Splits string into 3 parts:
# 1.Before separator
# 2.Separator
# 3.After separator
text7 = "apple-banana-mango"
print(text7.partition("-"))#It only splits at the first occurrence.
#s[start:stop:step]
s = "abcdefghijk"
print(s[1::3])