RASA NLU (Natural Language Understanding)
-----------------------------------------

* Understand user's inputs which is usually unstructured text
* Output: Structured data for further processing 
  * Intent
  * Entities

  
* Intent:
  * An intent is the intention of the user or the user's interacting with the chatbot
  * Intent Classification is nothing but training a classifier
  * Intent is the predicted class of the user's input
  * Example: 
    * What's the price of IphoneX?
      * class/intent: ask_price
  
* Entities:
  * Entites are objects/topics useful in further knowing the purpose of user's input
  * What's the price of IphoneX?
    * We figured user wants to know the price through intent classification but price of what?
      * IphoneX <-- Entity(smarthphone)
      
* Rasa NLU pipeline
  * Define the steps for classifying an intent and extracting an entities
  * Rasa has inbuilt models for doing this
  * This is done in config.yml file


* Train RASA: python -m rasa train nlu/rasa train nlu


* Test RASA: python -m rasa shell/ rasa shell




