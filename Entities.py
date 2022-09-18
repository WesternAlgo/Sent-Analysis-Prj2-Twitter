words='DATE'
entitiesList = []
#read the text file
with open('NamedEntities.txt') as f:
    line1=f.readlines()
    
#get the unique values from the text file
def get_unique_values(words):
    list_of_unique_values=[]
    unique_numbers = set(words)
    for word in unique_numbers:
        list_of_unique_values.append(word)
    return list_of_unique_values

entities2=get_unique_values(line1)
#remove \n
entities3= list(map(lambda x:x.strip(),entities2))

#print(*entities3, sep='\n')

retrieved_elements = list(filter(lambda x: 'DATE' in x, entities3))
retrieved_elements1 = list(filter(lambda x: 'PERSON' in x, entities3))
retrieved_elements2 = list(filter(lambda x: 'ORG' in x, entities3))

print(*retrieved_elements,sep='\n')
print(*retrieved_elements1,sep='\n')
print(*retrieved_elements2,sep='\n')