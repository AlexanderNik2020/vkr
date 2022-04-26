from rdflib import Graph
import pandas as pd

'''
dataframe = pd.read_excel('data.xls', index_col=0, header=None)

print(dataframe)

'''

# Create a Graph, pare in Internet data
g = Graph().parse("ontology/vkr-main/database-formatted.ttl")

print(g.serialize(format='ttl'))


