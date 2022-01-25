RASA NLU (Lookup and Entity Synonyms)
-------------------------------------

* Synonyms:
  * Let's say you had an entity phone that you used to look up the user's buy. One of the possible phone types is "mobile". Your users also refer to their "mobile" phone as "mobile" and "mobiles". 
  * In this case, you could define "mobile" and "mobiles" as synonyms to "phone"
  * Then, if either of these phrases is extracted as an entity, it will be mapped to the value phone

* Lookup tables:
  * You can use lookup tables to help extract entities which have a known set of possible values.
  * Keep your lookup tables as specific as possible.
  * For example, to extract category names, you could add a lookup table of all categories like phone, laptops, washing machine...etc
