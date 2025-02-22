def get_cats_info(path):
    cat_list = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                lines = line.strip().split(',')
                cat_dict = {
                    'id':lines[0],
                    'name':lines[1],
                    'age':lines[2]
                }
                cat_list.append(cat_dict)

    except FileNotFoundError:
        return 'File doesn\'t exist!'
    except Exception as e:
        return f'Exception has occured: {e}'
    
    return cat_list