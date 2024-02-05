# str

# literal assignment
first = 'John'
last = 'Doe'


# Concatenation
fullname = first + " " + last
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade)) 


# Casting a string to a number
zipcode = '1234'
zip_value = int(zipcode)
print(type(zip_value))

# Escaping special char with backward slash \
sentence = 'I\'m a president'
print(sentence)

# String Methods
default_words = 'lorem ipsum'
default_words.lower()
default_words.upper()
default_words.replace('lorem', 'dolor')
len(default_words)
