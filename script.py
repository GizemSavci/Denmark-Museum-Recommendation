
import csv

extracted_museums = []

flag = print("""
##   ##########
##   ##########

##   ##########
##   ##########
""")

with open('Museer, landsdel-gizem.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        extracted_row = {
            'Landsdel': row['Landsdel'],
            'Museumskategori': row['Museumskategori'],
            'Museumsnavn': row['Museumsnavn']
        }
        extracted_museums.append(extracted_row)

# Print the extracted data
#for row in extracted_museums:
    #print(row)

#print(type(extracted_museums))
#type()

def greet():
    print("Welcome To Museum Crawler of Denmark 🇩🇰")
    print("We are here to help you get most out of cultural layer of Denmark")

regions = []

for i in extracted_museums:
    region = list(i.values())[0]
    regions.append(region)
        
unique_regions = list(set(regions))
#first_letter_region = 
#print(unique_regions)

def choose_region():
    regions_list = "\n".join(unique_regions)
    print(f"Before we start, a quick reminder of Museum Regions of Denmark:\n{regions_list}")
    selected_region = input("In which region do you want to see the museum:")
    
    museums_in_selected_region = []
    
    for museum in extracted_museums:
        if museum['Landsdel'] == selected_region:
            museums_in_selected_region.append(museum['Museumsnavn'])
    
    if museums_in_selected_region:
        print(f"Museums in {selected_region}:")
        for museum_name in museums_in_selected_region:
            print(museum_name)
    else:
        print(f"No museums found in the selected region: {selected_region}")


#def choose_region():
    #regions_list = "\n".join(unique_regions)
    #print(f"Before we start, a quick reminder of Museum Regions of Denmark:\n{regions_list}")
    #first_question = input("In which region do you want to see the museum:")
    #if first_question in regions:
        #print(extracted_museums['Museumsnavn'])





#choose_region()
def museum_crawler():
    greet()
    choose_region()


museum_crawler()