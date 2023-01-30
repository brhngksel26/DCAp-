

def clear_all_item_by_dict(dict:dict)-> dict:
    for key in dict:
        dict[key] = [ls.strip() for ls in dict[key]]

    return dict