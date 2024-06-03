from typing import Dict
from lib.utils import ClassMetaData
from lxml import etree
import requests

class OntologyCrawler:
    classesMetaData: Dict[str, ClassMetaData] = dict()

    def __init__(self, url):
        self.url = url

    def start(self): 
        response = requests.get(self.url)
        xml_content = response.content
        xml_tree = etree.fromstring(xml_content)

        namespaces = {
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'owl': 'http://www.w3.org/2002/07/owl#'
        }

        classes = xml_tree.xpath('//owl:Class', namespaces = namespaces)

        for cls in classes:
            print(cls.xpath('@rdf:about', namespaces = namespaces))