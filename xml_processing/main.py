import os
import json
from lxml import etree

def extract_item_stacks(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    
    item_stacks = root.find('.//itemStacks')
    items_dict = {}
    
    for item in item_stacks:
        items_dict[item.tag] = int(item.text)
    
    return items_dict

def process_folder():
    combined_dict = {}

    for filename in os.listdir('../xml_data'):
        if filename.endswith('.xml'):
            file_path = os.path.join('../xml_data', filename)
            items_dict = extract_item_stacks(file_path)

            for item, count in items_dict.items():
                if item in combined_dict:
                    combined_dict[item] += count
                else:
                    combined_dict[item] = count

    return combined_dict

def main():
    combined_items = process_folder()

    with open('output.json', 'w') as f:
        json.dump(combined_items, f, indent=4)

if __name__ == "__main__":
    main()
