#made by Fedorchenko Roman КН-45-5

def sort_by_name(students_dict):
    #create a list of tuples (key, value) and sort it by first_name
    sorted_items = sorted(students_dict.items(), key=lambda x: x[1]["first_name"])
    # Return a new dictionary sorted by first names
    return dict(sorted_items)