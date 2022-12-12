progress = 0
trailer = 0
retriever = 0
exclude = 0   


def in_range(credit):   
 for i in range(len(between)):
   while not(credit in between):
     print('Out of range')
     credit=int(input('Please Re-enter your above credit'))

     break
     
    
between=[0,20,40,60,80,100,120]



def total_incorrect(totals):
   if(totals!=120):
     print('Total incorrect')





   
capture=0
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
     
      

       
       
       if (total==120):
        if (passes==120) :
         progress+=1  
         print ('Progress')
   
        elif (passes==100 and (defer==20 or defer==0)):
         trailer+=1
         print ('Progress(module trailer)')
   
        elif (passes==80 or passes==60) and (defer==20 or defer==40):
         retriever+=1  
         print('Do not Progress – module retriever')
   
        elif (passes==40 and defer!=0):
         retriever+=1  
         print('Do not Progress – module retriever')
   
        elif (passes==40 and fail==80) :
         exclude+=1  
         print('Exclude')
   
        elif ((passes==20) and (fail==80 or fail==100)):
         exclude+=1 
         print('Exclude')
   
        elif (passes==20):
         retriever+=1  
         print('Do not Progress – module retriever')

   
        elif ((passes==0) and (fail==80 or fail==100 or fail==120)):
         exclude+=1
         print('Exclude')
   
        elif (passes==0):
         retriever+=1  
         print('Do not Progress – module retriever')
   
        else:
         print('Invalid')
  
        capture=input('Would you like to enter another set of data? Enter y for yes or q to quit')

        if (capture == 'y' or capture == 'Y'):
         continue
        else:
         (capture == 'q' or capture == 'Q')
         print('Exits loop')
      
       done= True
      

   except ValueError:
      print('Integer required')
      




cr1 = 'Progress'
cr2 = 'Progress: Module Trailer'
cr3 = 'Do Not Progress: Module Trailer'
cr4 = 'Exclude'

def histogram():
 print('Horizontal Histogram')
 print(cr1,':', '*' * progress)
 print(cr2,':', '*' * trailer)
 print(cr3,':', '*' * retriever)
 print(cr4,':', '*' * exclude)
         
      
  
 print(sum([progress, trailer, retriever, exclude]), 'outcomes in total')
        
histogram()

     
       


