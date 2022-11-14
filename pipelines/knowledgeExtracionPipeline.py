from typing import Dict
import requests


class KnowledgeExtractionPipeline:
    
    def __init__(self) -> None:
        '''Ininitialize Models'''
        self.__spacyKnowledgeExtractor:None
        self.__rebelKnowledgeExtractor:None
        self.__linker:None
        self.__tripleGenerator:None
        

    def extract(model, text:str) -> Dict:
        pass

    def testExtract(self, text:str) -> Dict:
        '''test with falcon API'''
        json_data = {'text': text,}
        headers = {'Content-Type': 'application/json',}
        response = requests.post('https://labs.tib.eu/falcon/falcon2/api?mode=long', json=json_data, headers=headers)
        return response.json()