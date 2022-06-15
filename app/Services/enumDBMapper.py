from ..globalEnums import IndustryDBMapper

def industry_name_to_id_db_mapper(idustry_name):
    for industry in IndustryDBMapper:
            if industry.name.lower() == idustry_name.lower(): 
                return industry.value 

def industry_id_to_name_db_mapper(idustry_id):
    for industry in IndustryDBMapper:
            if industry.value == idustry_id: 
                return industry.name 