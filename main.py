from elasticsearch import Elasticsearch
from src import helpers as proc


# get the process information and convert it into a data frame
def getInfo():
    processes = proc.listOfProcesses()
    return processes


# main
def main():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    result = getInfo()
    i = 1
    for x in result:
        es.index(index="processes", doc_type="cpu_info", id=i, document=x)
        i = i + 1


if __name__ == '__main__':
    main()
