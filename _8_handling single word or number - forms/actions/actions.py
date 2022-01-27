import re
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        camera = tracker.get_slot('camera')
        ram = tracker.get_slot('ram')
        battery = tracker.get_slot('battery')

        dispatcher.utter_message(text='Here are your search results')
        dispatcher.utter_message(
            text='The features you entered: ' + str(camera) + ", " + str(ram) + ", " + str(battery))

        return []


class ActionShowLatestNews(Action):

    def name(self) -> Text:
        return "action_show_latest_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Calling the DB
        # calling an API
        # do anything
        # all caluculations are done
        dispatcher.utter_message(text='Here the latest news for your category')
        return []


class ProductSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "product_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["ram", "battery", "camera", "budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"ram": [self.from_text()],
                "camera": [self.from_text()],
                "battery": [self.from_text()],
                "budget": [self.from_text()]
                }

    def validate_ram(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        # 4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        try:
            ram_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            ram_int = 500000
            # Query the DB and check the max value, that way it can be dynamic
        if ram_int < 50:
            return {"ram": ram_int}
        else:
            dispatcher.utter_message(template="utter_wrong_ram")

            return {"ram": None}

    def validate_camera(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        # 4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        try:
            camera_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            camera_int = 500000
            # Query the DB and check the max value, that way it can be dynamic
        if camera_int < 150:
            return {"camera": camera_int}
        else:
            dispatcher.utter_message(template="utter_wrong_camera")

            return {"camera": None}

    def validate_budget(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        # 4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        try:
            budget_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            budget_int = 500000
            # Query the DB and check the max value, that way it can be dynamic
        if budget_int < 4000:
            return {"budget": budget_int}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")

            return {"budget": None}

    def validate_battery(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        # 4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        try:
            battery_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            battery_int = 500000
            # Query the DB and check the max value, that way it can be dynamic
        if battery_int < 8000:
            return {"battery": battery_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery")

            return {"battery": None}


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(text="Please find your searched items here.........")

        return []
