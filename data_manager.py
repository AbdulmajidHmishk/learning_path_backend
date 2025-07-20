import json 
import os 

class JsonDataManager:
    def read_data(self, file_path):
        if not os.path.exists(file_path):
            print(f"Datei nicht gefunden: {file_path}")
            return []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"JSON Fehler: {e}")
            return []
    
    def write_data(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)