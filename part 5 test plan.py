progress = 0
trailer = 0
retriever = 0
exclude = 0   
count=0

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
         
  

passes=[120,100,100,80,60,40,20,20,20,0]
defer=[0,20,0,20,40,40,40,20,0,0]
fail=[0,0,20,20,20,40,60,80,100,120]

for i in range(10):
 if(passes[i]==120):
     progress=progress+1
     print('Progress')
 elif (passes[i]==100) and (defer[i]==20 or defer[i]==0):
     trailer=trailer+1
     print('Progress: Module Trailer')
 elif (20<=passes[i]<=80) and (20<defer[i]<=40 or 20<=fail[i]<=60):
     retriever=retriever+1
     print('Do Not Progress: Module Trailer')
 else:
     exclude=exclude+1
     print('Exclude')


histogram()
print(sum([progress, trailer, retriever, exclude]), 'outcomes in total')
        


    



















       




