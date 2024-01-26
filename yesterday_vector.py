import spacy

nlp = spacy.load("en_core_web_lg")
tokens = nlp("Yesterday, All my troubles seemed so far away, Now it looks as though they're here to stay, Oh, I believe in yesterday, Suddenly, I'm not half the man I used to be, There's a shadow hanging over me, Oh, yesterday came suddenly, Why she had to go? I don't know, She wouldn't say, I said something wrong, now I long, For yesterday, Yesterday, Love was such an easy game to play, Now I need a place to hide away, Oh, I believe in yesterday, Why she had to go? I don't know, She wouldn't say, I said something wrong, now I long, For yesterday, Yesterday, Love was such an easy game to play, Now I need a place to hide away, Oh, I believe in yesterday")
  
vector = tokens[0].vector
print(vector)
