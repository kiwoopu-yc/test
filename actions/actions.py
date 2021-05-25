# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Optional
import datetime as dt
import rasa_sdk
from rasa_sdk.events import FollowupAction
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # grab entities from sentences
        # entities = tracker.latest_message['entities']

        # compare value with intent
        # state = tracker.current_state()
        # intent = state["latest_message"]["intent"]["name"]
        # if intent == name of expected intent: pass
        # else: return error

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []


class Validate_share_about_day_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_share_about_day_form"

    # async def required_slots(
    #         self,
    #         slots_mapped_in_domain: List[Text],
    #         dispatcher: "CollectingDispatcher",
    #         tracker: "Tracker",
    #         domain: "DomainDict",
    # ) -> Optional[List[Text]]:
    #     first_name = tracker.slots.get("first_name")
    #     if first_name is not None:
    #         if first_name not in names:
    #             return ["name_spelled_correctly"] + slots_mapped_in_domain
    #     return slots_mapped_in_domain


    # 给button加API
    # async def extract_name_spelled_correctly(
    #         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    # ) -> Dict[Text, Any]:
    #     intent = tracker.get_intent_of_latest_message()
    #     if 判定： 如果intent == happy
    #     dispatcher.utter_message(text=f"That's a very short description. Can you try to speak like....")
    #     return {"name_spelled_correctly": intent == "affirm"}
    #     elif:

    # def validate_name_spelled_correctly(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `first_name` value."""
    #     if tracker.get_slot("name_spelled_correctly"):
    #         return {"first_name": tracker.get_slot("first_name"), "name_spelled_correctly": True}
    #     return {"first_name": None, "name_spelled_correctly": None}

    def validate_day_describe(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `day_describe` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")

        # 修改unexpected input判定条件 置信度阈值
        intent = tracker.get_intent_of_latest_message()
        if intent != 'day_description':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"day_describe": None}
        else:
            return {"day_describe": slot_value}

    def validate_day_fav_part(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `day_fav_part` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a very short description. Can you try to speak like....")
            return {"day_fav_part": None}
        else:
            return {"day_fav_part": slot_value}

    def validate_ask_back_howwasyourday(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `ask_back_howwasyourday` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a very short description. Can you try to speak like....")
            return {"ask_back_howwasyourday": None}
        else:
            return {"ask_back_howwasyourday": slot_value}

    def validate_ask_back_favpart(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `ask_back_favpart` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a very short description. Can you try to speak like....")
            return {"ask_back_favpart": None}
        else:
            return {"ask_back_favpart": slot_value}

    def validate_receive_thanks(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `receive_thanks` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a very short description. Can you try to speak like....")
            return {"receive_thanks": None}
        else:
            return {"receive_thanks": slot_value}

    # def validate_last_name(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     print(f"Last name given = {slot_value} length = {len(slot_value)}")
    #     if len(slot_value) <= 1:
    #         dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
    #         return {"last_name": None}
    #     else:
    #         return {"last_name": slot_value}

#jump to next topic
class ActionNextTopic(Action):
    #activate_questions = {}
    def name(self):
        return 'action_next_topic'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #redirect
        dispatcher.utter_message(text="What's your favorite food")
        # return next topic, can set a random number to decide 
        return [FollowupAction("invitation_form")]

#handle unexpected input
# class ActionRestart(Action):
#     activate_questions = {}
#     def name(self):
#         return 'action_restart'
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         #redirect
#             dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
#
#         return []