import time
#words = input('Please input the words you want to say!:')
words = "Eva"
print("")
for item in words.split():
    letterlist = [] # stores all characters that will be printed out
    for y in range(14, -14, -1): # from y = 14 to y = -14
        list_X = [] # stores characters of x-axis
        letters = ''
        for x in range(-30, 30): # from x = -30 to x = 30
            expression = ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3  # the expression of a heart
            if expression <= 0:
                letters += item[(x-y) % len(item)]
            else:
                letters += ' '
        list_X.append(letters)
        letterlist += list_X
    print('\n'.join(letterlist))
    time.sleep(1.5)

"""

            aEvaEva                       aEvaEva           
       vaEvaEvaEvaEvaEvaE           EvaEvaEvaEvaEvaEva      
    aEvaEvaEvaEvaEvaEvaEvaEva   EvaEvaEvaEvaEvaEvaEvaEvaE   
   aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEva  
  aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv 
 aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaE
 EvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv
 vaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEva
 aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaE
 EvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv
  aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv 
   vaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv  
    EvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv   
     aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv    
       aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaE      
         aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEva        
           aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEv          
             aEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaEvaE            
                EvaEvaEvaEvaEvaEvaEvaEvaEvaEv               
                   vaEvaEvaEvaEvaEvaEvaEva                  
                      aEvaEvaEvaEvaEvaE                     
                         EvaEvaEvaEv                        
                             aEv                            
                              v                             
"""
