print("Lista zakupow")
zakupy ={
    "piekarnia": ["chleb", "Pączek", "Bułiki"],
    "warzywniak": ["marchew", "seler", "Rukola"] 
}

for sklep in zakupy:
    sentence = ("idę do {sklep} i kupuję tam {zakupy[sklep]}")
    print(sentence.title())


