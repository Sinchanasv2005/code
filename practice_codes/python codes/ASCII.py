#0 to 9-----48 to 57
# A to Z----65 to 90
# a to z----97 to 122


# digit to character
digit=67
print(chr(digit))

# output
C

# character to digit
ch='x'
print(ord(ch))
# 120


ch1='S'
print(ord(ch1))
# 83

# lower to upper -32
n='a'
print(chr(ord(n)-32))
# A

# upper to lower +32
N='A'
print(chr(ord(N)+32))
# a

#  find char between 0 and 9
order='5' #5 is 53 life between 48 and 57
print('0'<=order<='9')
# true

# output
# C
# 120
# 83
# A
# a
# True