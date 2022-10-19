num = 10

'''
      환율
달러  1131.5
엔화  1.3258
유로  1333.08
위안  172.94

달러, 엔화, 유로, 위안을 입력하면
원화로 환산해 주는 프로그램을 작성하세요

[힌트] split() 사용
       원화 = 입력한 금액 X 환율
[입력예] 100 달러, 100 엔, 100 유로, 100위안
         (위와 같이 금액과 통화명 사이에 공백 있음)
[출력] OOOO 원입니다         
'''
dict_exchange_rate \
  = {"달러":1131.5,"엔":1.3258,"유로":1333.08,"위안":172.94}

# [입력예] 100 달러, 100 엔, 100 유로, 100위안
money = input("입력 예를 보고 환전할 금액을 입력하세요 : ")

cash, currency = money.split()
# print(float(cash) * dict_exchange_rate[currency],"원입니다")
won = float(cash) * dict_exchange_rate[currency]
print("%.2F 원입니다" % won)




