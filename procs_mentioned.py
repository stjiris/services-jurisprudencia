from elasticsearch import Elasticsearch
from os import environ
import re

ELASTICSEARCH_URL = environ.get("ELASTICSEARCH_URL", "http://localhost:9200/")
ELASTICSEARCH_USER = environ.get("ELASTICSEARCH_USER","")
ELASTICSEARCH_PASS = environ.get("ELASTICSEARCH_PASS","")

client = Elasticsearch(ELASTICSEARCH_URL, basic_auth=(ELASTICSEARCH_USER,ELASTICSEARCH_PASS))

def process(text):
    return list(set(x.group() for x in re.finditer("\d+(-\w+)?/(\w+.)(\s)?(\w+.?)+(-\w+)?", text)))

def searchProcs(proc, UUID):
    must = [{'term': {'Processo': proc}}, {'wildcard': {'UUID': f"{UUID}*"}}]
    text = client.search(index="jurisprudencia.7.0", query={'bool': {'must': must} } )["hits"]["hits"][0]["_source"]["Texto"]
    procs_referidos = process(text)
    return procs_referidos # str[]