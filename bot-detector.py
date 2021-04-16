import amino
client = amino.Client()
client.login(email='temawe7102@aiclbd.com',password='abhiashish')
comlist= client.sub_clients(size=100)
for name, id in zip(comlist.name,comlist.comId):
    print("Comm Name  : ",name,"\nComm Id :",id,"\n--------------")
