sub1 = int(input("Enter your first subject marks\n"))
sub2 = int(input("Enter your second subject marks\n"))
sub3 = int(input("Enter your third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
      print("You are fail becouse you have less than 33%  in one the subject")

elif(sub1+sub2+sub3)/3 <40:
     print("you are fail due to total percentage less then 40")
     
else:
   print("congatulation! you passed the exam")    
          