from ..globalEnums import WorkHoursEnum

def workHours_mapped_to_value(job_hours):
    for hours in WorkHoursEnum:
            if hours.name.lower() == job_hours.lower(): 
                return hours.value 