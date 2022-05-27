price_of_worker = 2
LIST_OF_MATIRIAL = ['нефть', 'бензин', 'сено', 'мясо']
LIST_OF_COST_OF_MATERIAL = [100, 200, 100, 300, 1]
DICT_OF_COST_OF_MATERIAL = dict()
for i in range(len(LIST_OF_MATIRIAL)):
    DICT_OF_COST_OF_MATERIAL[LIST_OF_MATIRIAL[i]] = LIST_OF_COST_OF_MATERIAL[i]
