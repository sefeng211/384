import csv
from collections import defaultdict
import sys
FOOD_TYPE = ['Breakfast', 'Lunch', 'Dinner']
def csv_to_dict(in_file):
    """
    Converts the .csv format file into a dictionary of dictionary object. Each row represents a unique key
    value pair, with the first entry being the key. The other entries are values of the inner dictionary
    with their keys manually entered.
    """
    with open(in_file, mode="r") as infile:
        reader = csv.reader(infile)
        #with open(out_file, mode="w") as outfile:
        #writer = csv.writer(outfile)
        food_dict = {}
        next(reader)
        for row in reader:
            food = row[0]
            nutr_dict = {}
            nutr_dict["water"] = float(row[1]) if row[1].strip() != "" else 0.0
            nutr_dict["energy"] = float(row[2]) if row[2].strip() != "" else 0.0
            nutr_dict["protein"] = float(row[3]) if row[3].strip() != "" else 0.0
            nutr_dict["fat"] = float(row[4]) if row[4].strip() != "" else 0.0
            nutr_dict["carbohydrate"] = float(row[5]) if row[5].strip() != "" else 0.0
            nutr_dict["fiber"] = float(row[6]) if row[6].strip() != "" else 0.0
            nutr_dict["sugar"] = float(row[7]) if row[7].strip() != "" else 0.0
            nutr_dict["calcium"] = float(row[8]) if row[8].strip() != "" else 0.0
            nutr_dict["iron"] = float(row[9]) if row[9].strip() != "" else 0.0
            nutr_dict["magnesium"] = float(row[10]) if row[10].strip() != "" else 0.0
            nutr_dict["phosphorus"] = float(row[11]) if row[11].strip() != "" else 0.0
            nutr_dict["potassium"] = float(row[12]) if row[12].strip() != "" else 0.0
            nutr_dict["sodium"] = float(row[13]) if row[13].strip() != "" else 0.0
            nutr_dict["zinc"] = float(row[14]) if row[14].strip() != "" else 0.0
            nutr_dict["copper"] = float(row[15]) if row[15].strip() != "" else 0.0
            nutr_dict["vitamin C"] = float(row[16]) if row[16].strip() != "" else 0.0
            nutr_dict["vitamin B6"] = float(row[17]) if row[17].strip() != "" else 0.0
            nutr_dict["vitamin B12"] = float(row[18]) if row[18].strip() != "" else 0.0
            nutr_dict["vitamin E"] = float(row[19]) if row[19].strip() != "" else 0.0
            nutr_dict["vitamin D"] = float(row[20]) if row[20].strip() != "" else 0.0
            nutr_dict["cholesterol"] = float(row[21]) if row[21].strip() != "" else 0.0
            nutr_dict["price"] = float(row[22]) if row[22].strip() != "" else 0.0
            food_dict[food] = nutr_dict

    return food_dict

def csv_to_dict_v2(in_file):
    """
    Converts the .csv format file into a dictionary of dictionary object. Each row represents a unique key
    value pair, with the first entry being the key. The other entries are values of the inner dictionary
    with their keys manually entered.
    """
    with open(in_file, mode="r") as infile:
        reader = csv.reader(infile)
        #with open(out_file, mode="w") as outfile:
        #writer = csv.writer(outfile)
        dic = defaultdict(list)
        next(reader)
        for row in reader:
            food_dict = {}
            food = row[0]
            nutr_dict = {}
            nutr_dict["water"] = float(row[1]) if row[1].strip() != "" else 0.0
            nutr_dict["energy"] = float(row[2]) if row[2].strip() != "" else 0.0
            nutr_dict["protein"] = float(row[3]) if row[3].strip() != "" else 0.0
            nutr_dict["fat"] = float(row[4]) if row[4].strip() != "" else 0.0
            nutr_dict["carbohydrate"] = float(row[5]) if row[5].strip() != "" else 0.0
            nutr_dict["fiber"] = float(row[6]) if row[6].strip() != "" else 0.0
            nutr_dict["sugar"] = float(row[7]) if row[7].strip() != "" else 0.0
            nutr_dict["calcium"] = float(row[8]) if row[8].strip() != "" else 0.0
            nutr_dict["iron"] = float(row[9]) if row[9].strip() != "" else 0.0
            nutr_dict["magnesium"] = float(row[10]) if row[10].strip() != "" else 0.0
            nutr_dict["phosphorus"] = float(row[11]) if row[11].strip() != "" else 0.0
            nutr_dict["potassium"] = float(row[12]) if row[12].strip() != "" else 0.0
            nutr_dict["sodium"] = float(row[13]) if row[13].strip() != "" else 0.0
            nutr_dict["zinc"] = float(row[14]) if row[14].strip() != "" else 0.0
            nutr_dict["copper"] = float(row[15]) if row[15].strip() != "" else 0.0
            nutr_dict["vitamin C"] = float(row[16]) if row[16].strip() != "" else 0.0
            nutr_dict["vitamin B6"] = float(row[17]) if row[17].strip() != "" else 0.0
            nutr_dict["vitamin B12"] = float(row[18]) if row[18].strip() != "" else 0.0
            nutr_dict["vitamin E"] = float(row[19]) if row[19].strip() != "" else 0.0
            nutr_dict["vitamin D"] = float(row[20]) if row[20].strip() != "" else 0.0
            nutr_dict["cholesterol"] = float(row[21]) if row[21].strip() != "" else 0.0
            nutr_dict["price"] = float(row[22]) if row[22].strip() != "" else 0.0
            collection = str(row[23])
            if collection not in FOOD_TYPE:
                print("The data file is not valid")
                sys.exit(1)
            food_dict[food] = nutr_dict
            dic[collection].append(food_dict)
    return dic

if __name__ == '__main__':
    csv_to_dict_v2('food_nutrition_small_type_v2.csv')