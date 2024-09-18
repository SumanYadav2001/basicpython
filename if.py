#wap to check the user eligible for job
#if gender is female and age is greater  than 17
#if gender is male then then they can apply for private job
userage=int(input("enter the user age"))
usergender=(input("enter you gender"))
if(userage> 17 and usergender == "female"):
    print("you are eligible for goverment job")
elif(userage>17 and  usergender =="male"):
    print("you are eligible for private job")
else:
    print("you are not eligible for any job")
    