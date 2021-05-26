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

class Validate_seek_clarification_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_seek_clarification_form"

    def seek_clarification_q1(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'seek_clarification_a1':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"seek_clarification_q1": None}
        else:
            return {"seek_clarification_q1": slot_value}

    def seek_clarification_q2(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'seek_clarification_a2':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"seek_clarification_q2": None}
        else:
            return {"seek_clarification_q2": slot_value}

    def seek_clarification_q3(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'seek_clarification_a3':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"seek_clarification_q3": None}
        else:
            return {"seek_clarification_q3": slot_value}

    def seek_clarification_q4(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"seek_clarification_q3": slot_value}

    def seek_clarification_q5(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"seek_clarification_q3": slot_value}

    def seek_clarification_q6_1(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'affirm':
            return {"seek_clarification_q6_1": slot_value,
                    "seek_clarification_q6_2": slot_value}
        elif intent == 'deny':
            return {"seek_clarification_q6_1": slot_value}

    def seek_clarification_q6_2(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'affirm':
            return {"seek_clarification_q6_2": slot_value,
                    "seek_clarification_q7": slot_value,
                    "seek_clarification_q8": slot_value,
                    "seek_clarification_q9": slot_value}
        else:
            return {"seek_clarification_q6_2": None}

    def seek_clarification_q7(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"seek_clarification_q7": slot_value}

    def seek_clarification_q8(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'affirm':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"seek_clarification_q8": None}
        else:
            return {"seek_clarification_q8": slot_value}


class Validate_encountering_problem_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_encountering_problem_form"

    def encountering_problem_q1(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'encountering_problem_a1':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"encountering_problem_q1": None}
        else:
            return {"encountering_problem_q1": slot_value}

    def encountering_problem_q2(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'encountering_problem_a2':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"encountering_problem_q2": None}
        else:
            return {"encountering_problem_q2": slot_value}

    def encountering_problem_q3(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'encountering_problem_a3':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"encountering_problem_q3": None}
        else:
            return {"encountering_problem_q3": slot_value}

    def encountering_problem_q4(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'affirm' | intent == 'deny':
            return {"encountering_problem_q4": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"encountering_problem_q4": None}

    def encountering_problem_q5(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'affirm' | intent == 'deny':
            return {"encountering_problem_q5": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"encountering_problem_q5": None}

    def encountering_problem_q6(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"encountering_problem_q6": slot_value}

    def encountering_problem_q7(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"encountering_problem_q7": slot_value}

    def encountering_problem_q8(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"encountering_problem_q8": slot_value}

class Validate_meeting_appointment_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_meeting_appointment_form"

    def meeting_appointment_q1(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a1':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q1": None}
        else:
            return {"meeting_appointment_q1": slot_value}

    def meeting_appointment_q2(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a2':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q2": None}
        else:
            return {"meeting_appointment_q2": slot_value}

    def meeting_appointment_q3(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"meeting_appointment_q3": slot_value}

    def meeting_appointment_q4(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a4':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q4": None}
        else:
            return {"meeting_appointment_q4": slot_value}

    def meeting_appointment_q5(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"meeting_appointment_q5": slot_value}

    def meeting_appointment_q6(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a6':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q6": None}
        else:
            return {"meeting_appointment_q6": slot_value}

    def meeting_appointment_q7(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a7':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q7": None}
        else:
            return {"meeting_appointment_q7": slot_value}

    def meeting_appointment_q8(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a7':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q8": None}
        else:
            return {"meeting_appointment_q8": slot_value}

    def meeting_appointment_q9(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a9':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q9": None}
        else:
            return {"meeting_appointment_q9": slot_value}

    def meeting_appointment_q10(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'meeting_appointment_a10':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"meeting_appointment_q10": None}
        else:
            return {"meeting_appointment_q10": slot_value}


class Validate_greeting_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_greeting_form"

    def validate_greeting_q1(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'greeting_a1':
            return {"greeting_q1": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"greeting_q1": None}

    def validate_greeting_q2(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'mood_unhappy' | intent == 'mood_great':
            return {"greeting_q2": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"greeting_q2": None}

    def validate_greeting_q3(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'greeting_a2':
            return {"greeting_q3": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"greeting_q3": None}

    def validate_greeting_q4(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return{"greeting_q4": slot_value}




class Validate_interview_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_interview_form"

    def validate_interview_q1(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a1':
            return {"interview_q1": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q1": None}

    def validate_interview_q2(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"interview_q2": slot_value}

    def validate_interview_q3(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"interview_q3": slot_value}

    def validate_interview_q4(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a4':
            return {"interview_q4": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q4": None}

    def validate_interview_q5(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a5':
            return {"interview_q5": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q5": None}

    def validate_interview_q6(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a6':
            return {"interview_q6": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q6": None}

    def validate_interview_q7(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a7':
            return {"interview_q7": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q7": None}

    def validate_interview_q8(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a8':
            return {"interview_q8": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q8": None}

    def validate_interview_q9(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a9':
            return {"interview_q9": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q9": None}

    def validate_interview_q10(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'interview_a10':
            if len(slot_value) <= 5:
                dispatcher.utter_message(text=f"That's a very short expression. Let's try try to say something more")
                return {"interview_q10": None}
            else:
                return {"interview_q10": slot_value,
                        "interview_q11": slot_value,
                        "interview_q12": slot_value
                        }
        else:
            return {"interview_q10": slot_value}

    def validate_interview_q11(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a11':
            return {"interview_q11": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"interview_q11": None}

    def validate_interview_q12(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent != 'interview_a12':
            if len(slot_value) <= 5:
                dispatcher.utter_message(text=f"That's a very short expression. Let's try try to say something more")
                return {"interview_q12": None}
            else:
                return {"interview_q12": slot_value}
        else:
            return {"interview_q12": slot_value}

    def validate_interview_q13(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'interview_a13':
            return {"interview_q13": slot_value}
        elif intent == 'affirm':
            return {"interview_q13": slot_value,
                    "interview_q14": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return{"interview_q13": None}

    def validate_interview_q14(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if len(slot_value) > 5:
            return{"interview_q14": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return{"interview_q14": None}

    def validate_interview_q15(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        return {"interview_q15": slot_value}












class Validate_favorite_things_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_favorite_things_form"

    def validate_favorite_things_q1(
                                    self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a1':
            return {"favorite_things_q1": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q1": None}

    def validate_favorite_things_q2(self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a2':
            return {"favorite_things_q2": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q2": None}

    def validate_favorite_things_q3(self,
                                    slot_value: Any,
                                    dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a3':
            return {"favorite_things_q3": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q3": None}

    def validate_favorite_things_q4(self,
                                    slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a4':
            return {"favorite_things_q4": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q4": None}

    def validate_favorite_things_q5(self,
                                    slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a4':
            return {"favorite_things_q5": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q5": None}

    def validate_favorite_things_q6(self,
                                    slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a6':
            return {"favorite_things_q6": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q6": None}

    def validate_favorite_things_q7(self,
                                    slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a7':
            return {"favorite_things_q7": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q7": None}

    def validate_favorite_things_q8(self,
                                    slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                    tracker: Tracker,
                                    domain: DomainDict,) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        if intent == 'favorite_things_a8':
            return {"favorite_things_q8": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"favorite_things_q8": None}


class Validate_asking_directions_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_asking_directions_form"

    def validate_asking_directions_q1(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `day_describe` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")

        intent = tracker.get_intent_of_latest_message()
        if intent != 'place':
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"asking_directions_q1": None}
        else:
            return {"asking_directions_q1": slot_value}
            
    def validate_asking_directions_q2(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `day_describe` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")

        intent = tracker.get_intent_of_latest_message()
        if intent == 'affirm':
            return {"asking_directions_q2": slot_value}
        elif intent == 'deny':
            return {"asking_directions_q2": slot_value, "asking_directions_q3": slot_value}
    
    def validate_asking_directions_q3(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `day_describe` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")

        intent = tracker.get_intent_of_latest_message()
        if intent == 'waytobusstop':
            return {"asking_directions_q3": slot_value}
        else:
            return {"asking_directions_q3": None}


class Validate_share_about_day_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_share_about_day_form"

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
        intent = tracker.get_intent_of_latest_message()
        if intent != 'fav_part':
            dispatcher.utter_message(text=f"That's a wrong format....")
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
        
        intent = tracker.get_intent_of_latest_message()
        if (intent == 'ask_back_howwasday') | (intent == 'affirm'):
            return {"ask_back_howwasyourday": slot_value}
        else:
            dispatcher.utter_message(text=f"That's a wrong format....")
            return {"ask_back_howwasyourday": None}

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
        
        intent = tracker.get_intent_of_latest_message()
        if intent != 'ask_back_favpart':
            dispatcher.utter_message(text=f"That's a wrong format....")
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
        
        intent = tracker.get_intent_of_latest_message()
        if intent != 'affirm':
            dispatcher.utter_message(text=f"That's a wrong format....")
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
        dispatcher.utter_message(text="transfer success!")
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