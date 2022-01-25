Custom components in RASA NLU
-----------------------------

* Rasa provides good inbuilt NLU models for intent classification and entity extraction


* But it comes with an option of making our own components
  * Use case 1: We want to use a pretrained embedding model trained on user reviews? so that we can use it while training our embeddings
  * Use case 2: Want to censor the language of the user while he is talking! A language censor or a profanity filter...


* Use case 1: Transfer Learning and Pre-trained word embedding
  * Transfer learning is a machine learning method where a model developed for a task is reused as the starting point for a model on a second task.
  * In NLP, Transfer learning is generally done through pre-trained word embedding.
  * Words like smartphone and mobile are considered similar if there's enough evidence in the data that they appear in similar context
  * Thus giving us options to augment our current model with new information which otherwise wouldn't be present in the existing model
  * which in turn increases the model classification accuracy as well as the coverage of the vocabulary

  
* When to use Pre-trained model as a starting point?
  * Pre-trained model is on a similar language and domain dataset
  * This process will tend to work if the features are general meaning suitable to both base and target tasks, instead of specific to base task
  

* Export the model (.txt and .txt.gz)
  * Run: word2vec Model.ipynb


* convert .txt.gz format in spacy
  * python -m spacy init-model en spacy.word2vector.model --vectors-loc word2vec_shopping.txt.gz


* import the pre-trained model in "config.yml"


* Train: python -m rasa train nlu


* Test: python -m rasa shell
