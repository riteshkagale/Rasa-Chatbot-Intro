Slots - Bot Memory
---------

* Slots are basically bots memory
* Using them we can keep important things the bot has to remember for a later part of the conversation


* How do we define slots?
  * Through Entities: Can remember important values provided by users through Entities
  * Custom Actions: Information from the outside for example results extracted from the external database


* Types of slots:
  * text
  * bool
    * is_authenticated:
      - type: bool
  * categorical
    * color:
      * type: categorical
      * values:
        * low
        * medium
        * high
  * float
    * price:
      * type: float
        * min_value: 0.0
        * max_value: 1000000
  * list
  * unfeaturized

  
* Train: python -m rasa train


* Test: 
  * python -m rasa run action 
  * python -m rasa shell --debug 


* Slots (things to remember)
  * Slots can be used in utterance templates -> {phone_name}
  * Can be used in custom action -> tracker.get_slot('phone_name')
  * Can be set using custom actions -> return [Slotset('phone_name', 'Iphone X')]
  * Slots which are set using custom actions have to be reflected in training stories
    * action: action_set_phone
    * slot_was_set: 
      - phone_name: 'Iphone X'
  * All slots have to be listed in the domain
  * Slots values are kept in memory (until they reset)