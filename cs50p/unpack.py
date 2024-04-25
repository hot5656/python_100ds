# # unpack.py
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) *29 + knuts

# coins = [100, 50, 25]
# # * unpack list
# print(total(*coins), "Knuts")

# # python unpack.py
# #   50775 Knuts


# # unpack.py
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) *29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# # ** unpack dict
# print(total(**coins), "Knuts")

# # python unpack.py
# #   50775 Knuts

# # unpack.py
# def f(*args, **kwargs):
#     print("Positional:", args)
#     print("named:", kwargs)

# f(100, 50, 25)
# # return turple
# # Positional: (100, 50, 25)
# # named: {}
# f(100)
# # Positional: (100,)
# # named: {}

# f(galleons=100, sickles=50, knuts=25)
# # Positional: ()
# # return dict
# # named: {'galleons': 100, 'sickles': 50, 'knuts': 25}

# unpack.py
def print_mine(*args, **kwargs):
    print("Positional:", args)
    print("named:", kwargs)
print_mine("This", "is", "CS50", sep='_', end='*')


