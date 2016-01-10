names = input('Enter Your full name: ')

# split by space
list_of_names = names.split()

initials = []

# get first letters
for name in list_of_names:
    if name[0].isupper():
        initials.append(name[0])

print('Your initials are: ' + '.'.join(initials) + '.')