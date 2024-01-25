import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Yesterday, All my troubles seemed so far away, Now it looks as though they're here to stay, Oh, I believe in yesterday, Suddenly, I'm not half the man I used to be, There's a shadow hanging over me, Oh, yesterday came suddenly, Why she had to go? I don't know, She wouldn't say, I said something wrong, now I long, For yesterday, Yesterday, Love was such an easy game to play, Now I need a place to hide away, Oh, I believe in yesterday, Why she had to go? I don't know, She wouldn't say, I said something wrong, now I long, For yesterday, Yesterday, Love was such an easy game to play, Now I need a place to hide away, Oh, I believe in yesterday")

for token in doc:
  print("Token text: ", token.text, 
        "\nToken lemma: ", token.lemma_, 
        "\nToken tag: ", token.tag_, 
        "\nToken shape: ", token.shape_, 
        "\nToken is alpha: ", token.is_alpha, 
        "\nToken pos: ", token.pos_, 
        "\nToken dep: ", token.dep_,
        "\nToken is stop: ", token.is_stop)
  
for ent in doc.ents:
  print(ent.text, ent.label_)
