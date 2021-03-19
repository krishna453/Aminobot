import amino
import random

fakeemails=['email1','email2','email3']             #you can add more emails and passwords
passwords=['password1','password2','password 3']    # in the same format here , just put a comma


message=["""

 Invite message 1 here~~~~

""",
"""

Invite message 2 here~~~


""",

"""


Invite MEssage 3 here~~~


"""]
global sw
sw=0
l=len(fakeemails)
def switch_acc():
    global sw
    sw+=1
    if sw>(l-1):
        sw=sw%l
    print("Error Occurred , Switching to ",fakeemails[sw])
    try:
        client.login(email=fakeemails[sw], password=passwords[sw])
    except:
        switch_acc()

    try:
        client.join_community(comid)
    except amino.lib.util.exceptions.YouAreBanned:
        switch_acc()
    except:
        switch_acc()

client = amino.Client()
try:
    client.login(fakeemails[0],passwords[0])
except:
    switch_acc()
comlist= client.sub_clients(size=100)
i=0
for i in range(100):
    try:
        print(i+1,comlist.name[i])
    except IndexError:
        break
c = int(input("Select Community : "))
print("Selected Community : ",comlist.name[c-1])
comid=comlist.comId[c-1]
subclient = amino.SubClient(comId=comid, profile=client.profile)  
level=int(input("Enter Level Limit below which the users are to be invited"))
print("Starting Advertising in ",comlist.name[c-1])


i=0
j=0
count=0
breakflag=0
 
 
while True:
    try:
        client.join_community(comid)
    except:
        switch_acc()
    users =subclient.get_online_users(start=j,size=100) 
    for i in range(95):
        try:
            ulvl= subclient.get_user_info(users.profile.userId[i]).level
            if ulvl<int(level) or ulvl==int(level):
                r=random.randint(0, 2)
                subclient.start_chat(users.profile.userId[i], message[r])
                count+=1
                print(count+". Invited "+users.profile.nickname[i])
        except IndexError:
            breakflag=1
            break
            
        except amino.lib.util.exceptions.ChatInvitesDisabled:
            pass
        except amino.lib.util.exceptions.VerificationRequired :
            switch_acc()
        except amino.lib.util.exceptions.YouAreBanned:
            switch_acc()
        except:
            switch_acc()
    if breakflag==1:
        break
    j+=100
print("Total Invites : ",count)
