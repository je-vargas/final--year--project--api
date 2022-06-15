from ..globalEnums import IndustryDBMapper, CategoryDBMapper

def industry_name_to_id_db_mapper(idustry_name):
    for industry in IndustryDBMapper:
            if industry.name.lower() == idustry_name.lower(): 
                return industry.value 

def industry_id_to_name_db_mapper(idustry_id):
    for industry in IndustryDBMapper:
            if industry.value == idustry_id: 
                return industry.name 

def category_name_to_id_db_mapper(category_name):
    for category in CategoryDBMapper:
            if category.name.lower() == category_name.lower(): 
                return category.value 

def category_id_to_name_db_mapper(category_id):
    for category in CategoryDBMapper:
            if category.value == category_id: 
                return category.name 