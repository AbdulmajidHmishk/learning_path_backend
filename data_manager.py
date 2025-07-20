import json 
import os 

class JsonDataManager:
    def read_data(self, filepath) :
        try :
            if not os.path.exists(filepath):
                print (f"Datei nicht gefunden : {filepath}")
                return []
            with open (filepath, 'r' , encoding='utf-8' ) as f:
                return json.load(f)
        except  json.JSONDecodeError:
            print (f"ungultiges JSON in Datei: {filepath}")
            return []
        except Exception as e: 
            print (f"fehler beim Lesen der Datei: {e}")
            return []
    def write_date(self, filepath,data):
        try:
            with open(filepath, 'w', encoding='utf-8') as f :
                 json.dump(filepath,f , indent=4 , ensure_ascii= False  )
        except Exception as e:
            print (f"Fehler beim Schreiben der Datei: {e} ")        