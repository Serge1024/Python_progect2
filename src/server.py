from business import Contract
from business import Answer

user_name = "Serge"
class Server():
    def __init__(self):
        self.data_base = dict()
    def put_contract(self, contract):
        import clicker
        clicker.game.my_business[self.data_base[contract.business_id_to][1]].get_offer(contract)
    def send_ans(self, ans):
        if (ans.business_id_to == 0):
            return
        import clicker
        index = self.data_base[ans.business_id_to][1]
        clicker.game.my_business[index].sclad[ans.name] += ans.count
        clicker.game.dollar_score += ans.money
global server
server = Server()
