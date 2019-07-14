def two_fer(name):
    print("One for " + name + ", one for me.")
def two_fer_you():
    print("One for you, one for me")

name = input("Enter your name: ")
if len(name) > 0:
    two_fer(name)
else:
    two_fer_you()
