#1. pass: Neglate expected identation error
# for i in range(1, 10):
#    pass

#2. break: for terminating the loop
# for i in range(1, 10):
# if(i == 4):
# break
# print(i)


#3. continue: To stop perticular iteration
# for i in range(1, 10):
#    if(i == 4):
#     continue
#     print(i)

#4. else: will execute when the loop executed sucessfully
for i in range(1, 10):
    if(i == 4):
        break
    print(i)
else:
    print('Else block executed.')