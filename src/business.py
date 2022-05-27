from base_constants import LIST_OF_MATIRIAL
from base_constants import DICT_OF_COST_OF_MATERIAL


class Business:
    def __init__(self, name, price, recipt, to_person, main_product, cost_of_work):
        self.cost_of_work = cost_of_work
        self.rub_score = 0
        self.name = name
        self.price = price
        self.recipt = recipt
        self.to_person = to_person
        self.main_product = main_product
        self.sclad = dict()
        for material in LIST_OF_MATIRIAL:
            self.sclad[material] = 0
        self.work_resurce = 1
        self.business_id = 0
        self.offer = list()
        if (to_person):
            self.offer.append(Contract(0, self.business_id,
                self.main_product, self.work_resurce * 10,
                self.work_resurce * 10 * DICT_OF_COST_OF_MATERIAL[self.main_product]))

    def add_rub(self, count_of_rub):
        self.rub_score += count_of_rub

    def add_worker(self):
        self.work_resurce += 1

    def normal(self):
        flag = True
        for material in LIST_OF_MATIRIAL:
            flag = flag and (self.sclad[material] >= self.recipt.ingredient[material])
        return flag and (self.rub_score >= self.cost_of_work)

    def work(self):
        count_of_make_iteration = 0
        for inc in range(self.work_resurce):
            if (self.normal()):
                count_of_make_iteration += 1
                for material in LIST_OF_MATIRIAL:
                    self.sclad[material] -= self.recipt.ingredient[material]
                    self.sclad[material] += self.recipt.result[material]
                self.rub_score -= self.cost_of_work
        self.work_resurce = count_of_make_iteration

    def get_offer(self, contract):
        self.offer.append(contract)

    def say_yes(self):
        if (not len(self.offer)):
            return 0, 0
        if (self.sclad[self.offer[0].name] >= self.offer[0].count):
            self.sclad[self.offer[0].name] -= self.offer[0].count
            ans = self.offer[0]
            self.offer.pop(0)
            if(self.to_person and self.work_resurce > 0):
                self.offer.append(Contract(0, self.business_id,
                    self.main_product, self.work_resurce * 10, 
                    self.work_resurce * 10 * DICT_OF_COST_OF_MATERIAL[self.main_product]))
            return ans.cost, Answer(ans.business_id_from, 0, ans.name, ans.count)
        return 0, 0
    def say_no(self):
        if (not len(self.offer)):
            ans = self.offer[0]
            self.offer.pop(0)
            return Answer(ans.business_id_from, ans.cost, ans.name, 0)


class Recipt:
    def __init__(self, ingredient, result):
        self.ingredient = ingredient
        self.result = result

class Contract:
    def __init__(self, business_id_from, business_id_to, name, count, cost):
        self.business_id_from = business_id_from
        self.business_id_to = business_id_to
        self.name = name
        self.count = count
        self.cost = cost
class Answer:
    def __init__(self, business_id_to, money, name, count):
        self.business_id_to = business_id_to
        self.money = money
        self.name = name
        self.count = count

def from_offer_to_string(offer):

    answer += '0*' +str(offer.business_id_to) + "*"+str(offer.business_id_from)
    answer += "*" + offer.name + "*" + str(offer.count) + "*" + str(offer.cost)
    return answer

def from_ans_to_string(ans):
    answer += "1*" + str(ans.business_id_to) + "*" + str(ans.money)
    answer += "*" + ans.name + "*" + str(ans.count)
    return answer

def from_string_to_obgect(string):
    my_list = string.split("*")
    if (my_list[0] == '0'):
        return Contract(my_list[2], my_list[1],  my_list[3], my_list[4], my_list[5])
    else:
        return Answer(my_list[1], my_list[2],  my_list[3], my_list[4])
