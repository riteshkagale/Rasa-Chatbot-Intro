Custom components in RASA NLU
-----------------------------

* Rasa provides good inbuilt NLU models for intent classification and entity extraction


* But it comes with an option of making our own components
  * Use case 1: We want to use a pretrained embedding model trained on user reviews? so that we can use it while training our embeddings
  * Use case 2: Want to censor the language of the user while he is talking! A language censor or a profanity filter...

In short it censors the bad text, "ohh shit" so it's a profanity sentence (Profane word extraction done)


* import the profanity analyzer in "config.yml"


* Train: python -m rasa train nlu


* Test: python -m rasa shell
