# actions/actions.py

import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# 모킹된 재고 데이터
# INVENTORY = {
#     ("에어팟", "강남점"): 3,
#     ("마우스", "잠실점"): 0,
#     ("키보드", "강남점"): 30,
#     ("맥북", "홍대점"): 14
# }

class ActionCheckStock(Action):
    def name(self) -> Text:
        return "action_check_stock"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        df = pd.read_csv("docs/inventory.csv")

        row = inventory_df[
            (inventory_df["product_name"] == product) &
            (inventory_df["store_location"] == store)
        ]

        product = tracker.get_slot("product_name")
        store   = tracker.get_slot("store_location")

        if not store:
            dispatcher.utter_message(text="어느 매장 재고를 확인할까요?")
            return []

        key     = (product, store)
        count = int(row["count"].iloc[0])

        if count is None:
            # dispatcher.utter_message(text=f"{store}에 {product} 정보가 없습니다.")
            return [SlotSet("count", None)]
        elif count == 0:
            # dispatcher.utter_message(text=f"{store}에 {product}은(는) 품절입니다.")
            return [SlotSet("count", 0)]
        else:
            # dispatcher.utter_message(text=f"{store}에 {product}은(는) {count}개 남아 있어요.")
            return [SlotSet("count", count)]
