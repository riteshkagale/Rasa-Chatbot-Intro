Rasa CORE
---------

* Rasa core predicts what bot should say for a given user input
* We can not write rules for every user path
* Instead of using rules and enforcing them on the user Rasa uses machine learning to learn the conversational patterns
* Generally process of handling the conversation flow and responding in a chatbot is called Dialogue Management


* Responses:
  * Similar to how we define user inputs we have to define our bot responses
  * These are the set of words/replies the knows and are picked based on the prediction by the policies
  * Responses are either defined as utterances or actions
    * Utterance: Hard coded messages
      * Can have multiple messages per utterance 
      * examples: 
        * utter_greet:
        - "Welcome, how can I help you?"
        - "Hey, How do you do?"
      - Various formats: Text, Images, Buttons
        

* Custom Actions
  * Allows you to use python code
    * call the DB
    * Calling an API
    * Writing to the DB
    * Do some calculation


* Stories
  * Example conversations between the user and assistant
  * Can have multiple stories
  * Each story is sample conversation the bot can have with the user
  * Provides training data for the Dialogue management system of rasa


* Domain
  * It is the universe in which the bot operates.
  * it defines all the things your bot should know about
    * Has intents (what the user means)
    * Responses (What the bot should say)
    * What info. to remember
    * what entities to extract


* Dialogue policies
  * A policy is responsible for making a decision of how an assistant should respond next
  * Not always we use machine learning to predict the next action/response
  * Apart from machine learning we have certain other policies defined which help us with selecting the next response.
    * Max History: Controls how much dialogue history the model looks at to decide which action to take next
    * Data Augmentation: An amount of new stories to create from the existing stories
    * Memoization Policy: Mimics the stories
    * Mapping: maps certain intent to action irrespective of whatever conversation is going on it certain intent has a mapped action, bot triggers that action
    * Keras/Embedding/Sklearn: which uses machine learning and deep learning to predict next action
    * Fallback Policy: bot isn't confident what user is telling or something is out of scope, the bot fall backs
    

* Policy priority:
  * rank 1: Form policy
  * rank 2: Fallback and two stage fallback policy
  * rank 3: Memoization policy and Augmented memoization
  * rank 4: Mapping 
  * rank 5: Embedding, Keras, Sklearn


* Train: python -m rasa train


* Test: 
  * python -m rasa run action 
  * python -m rasa shell --debug 