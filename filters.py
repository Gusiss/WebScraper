from datetime import datetime

def filter_by_gender(cats, gender):
    return [cat for cat in cats if cat['gender'].lower() == gender.lower()]

def sort_by_date(cats, reverse=False):
    return sorted(cats, key=lambda x: x['date'] or datetime.min.date(), reverse=reverse)