Introduction to Form
---------

* Forms are nothing but Slots filling
* If you need to collect multiple pieces of information in a row, we should use FormValidationAction.
* Single action which contains the logic to loop over the required slots and ask the user for this information


* Rule Policy:
  * Once the form action gets called for the first time, the form gets activated and the Rule policy jumps in.
  * The rule policy is extremely simple and just always predicts the form actions


* Submit method:
  * Once all the slots are filled the submit() method is called

  
* Custom Slot Mapping
  * By default, slots will be only filled by entities with the same name as the slot that are picked up from the user input
  * slot_mapping method defines how to extract slot values from user responses
  * from_entity: will look for an entity called entity_name to fill a slot slot_name regardless of user intent/Only if the users intent is intent_name
  * from_intent: will fill a slot slot_name with value if user intent is intent_name
  * from_text: will use the next user utterance to fill the text slot slot_name regardless of user intent/ if user intent is intent_name


* Handling conditional slots logic
  * Can achieve this by writing some logic into the required_slots() method


* Validation
  * By default validation only checks if the requested slots was successfully extracted from the slot mappings
  * If you want to add custom validation use helper validation function with the name validate_{slot_name}

  
* Train: python -m rasa train


* Test: 
  * python -m rasa run action 
  * python -m rasa shell --debug 


