# que = ["Colour of sky?","colour of apple?","color of banana?"]
# ans = ["blue","red","yellow"]
#
# print(len(que))
#
# i = 0
# while(i<len(que)):
#     print(que[i])
#     sol = input("Enter your answer")
#
#     if ans[i] == sol:
#         print("correct", ans[i])
#     else:
#         print("wrong ans")
#     i = i + 1
###############################


questions = [
    ['Question1', 'a', 'b', 'c', 'd', 1],
    ['Question2', 'p', 'q', 'r', 's', 2],
    ['Question3', 'l', 'm', 'n', 'o', 3],
    ['Question4', 'u', 'v', 'w', 'x', 4],
    ['Question5', 'm', 'n', 'o', 'p', 5],
]
# print(questions[0][0])  #Question1
m = 0
for i in range(0, len(questions)):
    # print(questions[i][0],questions[i][1])
    print(questions[i][0])
    a = int(input("enter your answer:"))
    if a == questions[i][5]:
        print("correct answer!\n")
        if i == 2:
            m = 30000
            print("You won 30000 Rupees!\n")
        elif i == 4:
            m = 50000
            print(f'You have won KBC with money {m}!')
    else:
        print("\nwrong answer!")
        print(f'Your take away money is {m}')
        # exit()        #exit and break both are working same here.
        break








