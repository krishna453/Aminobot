import amino
client = amino.Client()
client.login(email='botamino016@fake-box.com',password='123ironman')
comlist= client.sub_clients(size=100)
for name, id in zip(comlist.name,comlist.comId):
    print("Comm Name  : ",name,"\nComm Id :",id,"\n--------------")
© 2021 GitHub, Inc.
