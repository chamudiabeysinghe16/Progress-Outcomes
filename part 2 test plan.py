def in_range(credit):   
 for i in range(len(between)):
   if not(credit in between):
     print('Out of range')
     credit=int(input('Please Re-enter your above credit'))
     break
     
    
between=[0,20,40,60,80,100,120]



def total_incorrect(totals):
   if(totals!=120):
     print('Total incorrect')
   

   
done=False
while not done:
   try:
      
      
      passes= int(input('Please enter your credit at pass'))
      in_range(passes)
      defer=int(input('Please enter your credit at defer'))
      in_range(defer)
      fail=int(input('Please enter your credit at fail'))
      in_range(fail)
      
      
      total=passes+defer+fail
      total_incorrect(total)
     
      
     
      done= True
      

   except ValueError:
      print('Integer required')
      

   

if (total==120):
 if (passes==120) :
   print ('Progress')
 elif (passes==100 and (defer==20 or defer==0)):
   print ('Progress(module trailer)')
 elif (passes==80 or passes==60):
   print('Do not Progress – module retriever')
 elif (passes==40 and defer!=0):
   print('Do not Progress – module retriever')
 elif (passes==40 and fail==80) :
   print('Exclude')
 elif ((passes==20) and (fail==80 or fail==100)):
   print('Exclude')
 elif (passes==20):
   print('Do not Progress – module retriever')
 elif ((passes==0) and (fail==80 or fail==100 or fail==120)):
   print('Exclude')
 elif (passes==0):
   print('Do not Progress – module retriever')   
else:
   print('Invalid')
