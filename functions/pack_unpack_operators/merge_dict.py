# https://stepik.org/lesson/2284240/step/6?unit=2318722

def merge_dicts(*dict1, ignored_keys=None):
    res = {}
    for i in dict1:
        res.update(i)
        
    if ignored_keys != None:
        for i in ignored_keys:
            del res[i]
            
    return res 

goods = merge_dicts(goods1, goods2, goods3, goods4, ignored_keys=('id', 'date', 'cat_id'))