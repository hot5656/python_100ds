from logic import *

rain = Symbol("rain")
hargrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

# sentence = And(rain, hargrid)
# print(sentence.formula())

knowledge = And(
    Implication(Not(rain), hargrid),
    Or(hargrid, dumbledore),
    Not(And(hargrid, dumbledore)),
    dumbledore
)
# print(knowledge.formula())
print(model_check(knowledge, rain)) # True
# print(model_check(knowledge, hargrid)) # False
# print(model_check(knowledge, dumbledore)) # True
