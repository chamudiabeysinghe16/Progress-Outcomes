passes= int(input('Please enter your credit at pass'))
defer=int(input('Please enter your credit at defer'))
fail=int(input('Please enter your credit at fail'))
if(passes+defer+fail==120):
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
