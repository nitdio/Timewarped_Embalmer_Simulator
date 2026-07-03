import random
import copy
import matplotlib.pyplot as plt

minion_list_temp=[["Kill","Reborn",2],["SP","Reborn",2],["SP","Reborn",2],["SP","Reborn",2],["SP","Reborn",2],["SP","Reborn",2],["SP","Reborn",2]]
total_token_dict={}
total_kill_dict={}

print(minion_list_temp)
for i in range(100000):
    print(i)

    minion_list=copy.deepcopy(minion_list_temp)

    kill_count = 0
    for j in range(300000):


        if j%2==0: #attack first
            if minion_list[0][0] == "Kill":
                kill_count+=1
            if minion_list[0][1]=="Reborn": #if attacking minion has reborn
                if all(
                    item == 0
                    for i, sublist in enumerate(minion_list)
                    if i != 0
                    for item in sublist
                    if isinstance(item, (int, float))
                ):
                    minion_list[0][1] = "No Reborn"
                else:
                    for k in range(len(minion_list)):
                        if k==0:  #if checking attacking minion
                            continue

                        if minion_list[k][0]=="SP": #if the checking minion has give reborn ability
                            if minion_list[k][2]>0: #check if the reborn ability can still be use
                                minion_list[k][2]-=1 # minus one usage
                                if minion_list[0][0]=="SP": #if attacking minion has give reborn ability
                                    minion_list[0][2] = 2 #reset it

                                break





            else:
                minion_list.pop(0)

                if minion_list == []:
                    break
        elif j%2==1: #attack first
            random_index=random.randrange(0,len(minion_list))
            if minion_list[random_index][0] == "Kill":
                kill_count+=1
            if minion_list[random_index][1]=="Reborn": #if attacked minion has reborn
                if  all(
    item == 0
    for i, sublist in enumerate(minion_list)
    if i != k
    for item in sublist
    if isinstance(item, (int, float))
):
                    minion_list[random_index][1] = "No Reborn"
                else:
                    for k in range(len(minion_list)):
                        if k==random_index:  #if checking attacking minion
                            continue

                        if minion_list[k][0]=="SP": #if the checking minion has give reborn ability

                            if minion_list[k][2]>0: #check if the reborn ability can still be use
                                minion_list[k][2]-=1 # minus one usage
                                if minion_list[random_index][0]=="SP": #if attacked minion has give reborn ability
                                    minion_list[random_index][2] = 2 #reset it

                                break #stop cehcking so reborn check will not change (reborn check = true  will cause it not to reborn)






            else:
                minion_list.pop(random_index)

                if minion_list == []:
                    break

        print(minion_list)
    if j+1 in total_token_dict:
        total_token_dict[j+1] += 1
    else:
        total_token_dict[j+1] = 1
    if kill_count in total_kill_dict:
        total_kill_dict[kill_count] += 1
    else:
        total_kill_dict[kill_count] = 1
    print(total_token_dict)
    print(total_kill_dict)

plt.figure(figsize=(8, 5))
plt.bar(total_token_dict.keys(), total_token_dict.values())
plt.title("Total Tokens")
plt.xlabel("Total tokens")
plt.ylabel("No_simulations")

plt.figure(figsize=(8, 5))
plt.bar(total_kill_dict.keys(), total_kill_dict.values())
plt.title("Total kills")
plt.xlabel("Total Kills")
plt.ylabel("No_simulations")
#
plt.show()