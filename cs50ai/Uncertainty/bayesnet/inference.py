from model import model

# Calculate predictions
# predictions = model.predict_proba({
#     "train": "delayed"
# })
# rain
#     none: 0.4583
#     light: 0.3069
#     heavy: 0.2348
# maintenance
#     no: 0.6432
#     yes: 0.3568
# train: delayed
# appointment
#     miss: 0.4000
#     attend: 0.6000

predictions = model.predict_proba({
    "rain":"heavy",
    "train": "delayed"
})
# rain: heavy
# maintenance
#     yes: 0.1176
#     no: 0.8824
# train: delayed
# appointment
#     attend: 0.6000
#     miss: 0.4000


# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")
