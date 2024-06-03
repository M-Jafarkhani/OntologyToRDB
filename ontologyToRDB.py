import json
from lib.ontologyCrawler import OntologyCrawler


def main():
    with open('../config.json', 'r') as config_file:
        config = json.load(config_file)
        ontology_url = config["OntologyUrl"]
        crawler = OntologyCrawler(ontology_url)

if __name__ == "__main__":
    main()

