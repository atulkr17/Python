# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.


def display(**kwargs):

    for (key,value) in kwargs.items():
        print(key,'->',value)
display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad')        