import nlpcloud

client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False, lang="en")
client.sentiment("Look what's just come on the market in #ValThorens! A recently renovated, charming 6 bed duplex apartment in the heart of the resort with superb views!")