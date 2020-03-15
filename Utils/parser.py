import csv
import xml.etree.ElementTree as ET

def parseXML(xmlfile):

    tree = ET.parse(xmlfile)
    root = tree.getroot()

    reviews = []

    for sentence in root.iter('sentence'):
        
        entity_opinion = {
            "sentence" : "",
            "EA_Pair" : []
        }

        for text in sentence.iter('text'):
            entity_opinion['sentence'] = text.text
        
        try:
            for category in sentence.iter('Opinion'):
                opinion = category.get('category')
                
                entity = opinion.split('#')[0]
                attribute = opinion.split('#')[1]

                entity_opinion["EA_Pair"].append((entity, attribute))

        except:
            print('No opinion')
    
        reviews.append(entity_opinion)
    
    return reviews

if __name__ == "__main__":
    reviews = parseXML(r'C:/Users/ujzr76l/Desktop/ABSA/ABSA-15_Laptops_Train_Data.xml')

    for review in reviews:
        if review['EA_Pair'] == []:
            pass
        else:
            print(review['sentence'])
            print(review['EA_Pair'])