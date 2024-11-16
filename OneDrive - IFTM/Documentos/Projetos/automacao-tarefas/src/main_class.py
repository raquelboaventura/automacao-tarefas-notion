import os
from notion_client import Client

class MainClass():
    def __init__(self) -> None:
        self.token = os.getenv('AUTH')
        self.notion = Client(auth=self.token)
        self.database_id = os.getenv('DATABASE_TAREFAS_ID')
    
    def automacao_tarefas_notion(self):
        response = self.notion.databases.query(
            database_id=self.database_id,
            filter={
                "and": [
                    {
                        "property": "PropertyID1",
                        "text": {
                            "equals": "Value1"
                        }
                    },
                    {
                        "property": "PropertyID2",
                        "text": {
                            "equals": "Value2"
                        }
                    }
                ]
            }
        )
        return response