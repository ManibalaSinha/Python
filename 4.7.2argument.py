# *name: receives a tuple.(consists number of values)
# when a final parameter of the form **name is present, it receives a dictionary.
# *name must occur before **name
def cheeseshop(name, *arguments, **keywords):
    print("Do you have any ", name, "?")
    print("I'm sorry, we're all out of", name)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "it's very runny, sir.",
"it's really very, VERY runny, sir. ",
shopkeeper="Michael John",
client="John Smith",
sketch="cheese Shop sketch", nme="mani")
