def dict_intersect(dic1: dict, dic2: dict) -> dict:
    dic_resp = dict()
    keys_dic1 = dic1.keys()
    keys_dic2 = dic2.keys()
    for k in keys_dic1:
        if k in keys_dic2:
            if dic1[k] == dic2[k]:
                dic_resp.update({k: dic1[k]})
    return dic_resp


d1 = {"A": 1, "B": 2, "C": 3, "D": 5, "E": 4}
d2 = {"A": -3, "B": 2, "C": 6, "D": 5}

print(dict_intersect(d1, d2))
