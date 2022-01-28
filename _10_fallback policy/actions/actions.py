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
        if tracker.get_slot('category') == 'phone':
            return ["ram", "battery", "camera", "budget"]
        elif tracker.get_slot('category') == 'laptop':
            return ["ram", "battery_backup", "storage_capacity", "budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"ram": [self.from_text()],
                "camera": [self.from_text()],
                "battery": [self.from_text()],
                "budget": [self.from_text()],
                "battery_backup": [self.from_text()],
                "storage_capacity": [self.from_text()]
                }

    def validate_battery_backup(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        try:
            battery_backup_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            battery_backup_int = 500000
        if battery_backup_int < 50:
            return {"battery_backup": battery_backup_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery_backup")

            return {"battery_backup": None}

    def validate_storage_capacity(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        try:
            storage_capacity_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            storage_capacity_int = 500000
        # Query the DB and check the max value, that way it can be dynamic
        if storage_capacity_int < 2000:
            return {"storage_capacity": storage_capacity_int}
        else:
            dispatcher.utter_message(template="utter_wrong_storage_capacity")

            return {"storage_capacity": None}

    def validate_ram(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        try:
            ram_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            ram_int = 500000
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
        try:
            camera_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            camera_int = 500000
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
        try:
            budget_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            budget_int = 500000
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

        if tracker.get_slot('category') == 'phone':
            dispatcher.utter_message(text="Please find your searched items here......... Phones..")

        elif tracker.get_slot('category') == 'laptop':
            dispatcher.utter_message(text="Please find your searched items here......... Laptops..")

        return []


class MyFallback(Action):

    def name(self) -> Text:
        return "action_my_fallback"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_fallback")

        return []