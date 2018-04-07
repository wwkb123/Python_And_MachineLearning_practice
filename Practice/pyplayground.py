
# coding: utf-8

# In[1]:


1+2


# In[1]:


2**3


# In[2]:


4**0.5


# In[3]:


0.1+0.2


# In[4]:


0.1+0.2-0.3


# In[5]:


0.1+0.1


# In[6]:


0.1+0.3


# In[7]:


0.1+0.2


# In[8]:


0.2+0.1


# In[9]:


0.2


# In[5]:


asd = 1.213123
xxx = "xxx"
print ('the string is {0:1.2f}'.format(asd))


# In[12]:


print("asasd {0}".format("123"))


# In[9]:


my_list = [0,2,4,7,99]


# In[10]:


my_list.sort()


# In[11]:


my_list


# In[1]:


pwd


# In[2]:


f = open('test.txt')


# In[3]:


f


# In[6]:


f.readlines()


# In[20]:


f.seek(0)


# In[48]:


f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '!':
            count = count + 1

print ("! is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '@':
            count = count + 1

print ("@ is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '#':
            count = count + 1

print ("# is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '$':
            count = count + 1

print ("$ is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '%':
            count = count + 1

print ("% is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '^':
            count = count + 1

print ("^ is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '&':
            count = count + 1

print ("& is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '*':
            count = count + 1

print ("* is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '(':
            count = count + 1

print ("( is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == ')':
            count = count + 1

print (") is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '-':
            count = count + 1

print ("- is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '+':
            count = count + 1

print ("+ is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '=':
            count = count + 1

print ("= is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '_':
            count = count + 1

print ("_ is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '{':
            count = count + 1

print ("{ is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '}':
            count = count + 1

print ("} is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == '[':
            count = count + 1

print ("[ is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == ']':
            count = count + 1

print ("] is",count)

f.seek(0)
count = 0
for line in f.readlines():
    for word in line:
        if word == ']':
            count = count + 1

print ("] is",count)



f.seek(0)
list = f.readlines()
x = 'a'
asd = 0
while asd < 25:
    for line in list:
        count = line.count(x)
        if count!=0:
            print(x, count)
    x = chr(ord(x)+1)
    asd = asd + 1    

for line in list:
    for word in line:
        if ord(word) >= ord('a') and ord(word) <=ord('z'):
            print(word)


# In[46]:


print(ord('A'))


# In[17]:


st = "aHdVasDccAAAzCCCdAAAAasSgwE"
front = 0
rear = 8
while rear<len(st):
    if not (st[front].isupper()) and not (st[rear].isupper()):
        if st[front+1].isupper() and st[rear-1].isupper():
            if st[front+2].isupper() and st[rear-2].isupper():
                if st[front+3].isupper() and st[rear-3].isupper():
                    print(st[front+4])
    front = front+ 1
    rear = rear + 1


# In[20]:


f = open("test.txt")
list = f.readlines()
for st in list:
    front = 0
    rear = 8
    while rear<len(st):
        if not (st[front].isupper()) and not (st[rear].isupper()):
            if st[front+1].isupper() and st[rear-1].isupper():
                if st[front+2].isupper() and st[rear-2].isupper():
                    if st[front+3].isupper() and st[rear-3].isupper():
                        if not (st[front+4].isupper()):
                            print(st[front+4])
        front = front+ 1
        rear = rear + 1


# In[1]:


st = 'Print only the words that start with s in this sentence'
list = st.split()


# In[2]:


list


# In[3]:


for word in list:
    if word[0]=='s':
        print(word)


# In[4]:


for x in range(0,11):
    if x%2==0:
        print(x)


# In[26]:


lt = [x for x in range(1,51) if x%3==0]
        


# In[27]:


lt


# In[19]:


st = 'Print every word in this sentence that has an even number of letters'
list = st.split()
for word in list:
    if len(word)%2==0:
        print (word," is even!")


# In[20]:


for x in range(1,101):
    if x%3==0 and x%5!=0:
        print("Fizz")
    elif x%3!=0 and x%5==0:
        print("Buzz")
    elif x%3==0 and x%5==0:
        print("FizzBuzz")
    else:
        print(x)


# In[21]:


st = 'Create a list of the first letters of every word in this string'
list = st.split()


# In[22]:


lt = [x[0] for x in list]


# In[23]:


lt


# In[1]:


def vol(radius):
    return 4/3*3.14*radius**3


# In[2]:


vol(2)


# In[3]:


def ran_check(num,low,high):
    return num in range(low,high)


# In[5]:


ran_check(1,1def up_low(s):,3)


# In[8]:


def up_low(s):
    low = 0
    up = 0
    for word in s:
        if word.isupper():
            up+=1
        elif word.islower():
            low+=1
    print("No. of Upper case characters : ",up)
    print("No. of Lower case characters : ",low)


# In[9]:


st = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(st)


# In[10]:


def unique_list(l):
    s = set(l)
    return list(s)


# In[11]:


lt = [1,1,1,1,2,2,3,3,3,3,4,5]
unique_list(lt)


# In[14]:


def multiply(numbers):
    result = 1
    for number in numbers:
        result*=number
    return result


# In[15]:


multiply([1,2,3,-4])


# In[16]:


def palindrome(s):
    copy = s[::-1]
    return copy==s


# In[17]:


palindrome('helleh')


# In[19]:


palindrome('healblaeh')


# In[35]:


import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    str1.lower()
    lt = [word for word in str1 if word in alphabet]
    s = set(lt)
    return s==set(alphabet)


# In[37]:


ispangram("The quick brown fox jumps over the lazy dog")


# In[51]:


class Dog(object):
    fur = True
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(self.name,"!")
    def hasFur(self):
        print(Dog.fur)
    
    def __str__(self):
        return "name is {x}".format(x=self.name)
        


# In[52]:


d1 = Dog(name="pika")


# In[53]:


d1


# In[54]:


d1.name


# In[55]:


d1.bark()


# In[56]:


d1.hasFur()


# In[57]:


print(d1)


# In[64]:


class Line(object):
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        return ((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1])**2)**0.5
        
    def slope(self):
        return (self.coor1[1]-self.coor2[1])/(self.coor1[0]-self.coor2[0])
    


# In[65]:


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)



# In[66]:


li.distance()


# In[67]:


li.slope()


# In[68]:


class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return 3.14*self.radius**2*self.height
        
    def surface_area(self):
        return 2*3.14*self.radius**2+2*3.14*self.radius*self.height


# In[69]:


c = Cylinder(2,3)


# In[70]:


c.volume()


# In[71]:


c.surface_area()


# In[44]:


import urllib.request
lt=[]
x = '63579'
st = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+x
req = urllib.request.Request(st)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    lt = the_page.split()
for count in range(0,500):
    
    x = lt[-1].decode("utf-8")
    st = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+x
    req = urllib.request.Request(st)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    
    print(the_page," count:",count)
    lt = the_page.split()


# In[28]:





# In[26]:


lt = the_page.split()


# In[14]:


lt


# In[22]:


lt[-1].decode("utf-8")


# In[1]:


import pickle


# In[4]:


entry=['p','e','a','k']
with open('entry.pickle', 'wb') as f:
    
    pickle.dump(entry, f)


# In[5]:


f


# In[6]:


with open('entry.pickle', 'rb') as f:
    entry = pickle.load(f)


# In[7]:


entry


# In[8]:


f


# In[11]:


import urllib.request
import pickle
lt=[]
st = 'http://www.pythonchallenge.com/pc/def/banner.p'
req = urllib.request.Request(st)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
data = pickle.loads(the_page)


# In[16]:


for line in data:
    print("".join([k * v for k, v in line]))


# In[31]:


st = 'http://www.pythonchallenge.com/pc/def/channel.jpg'
req = urllib.request.Request(st)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
data = pickle.loads(the_page)


# In[34]:


list1="channel"
list2="<-- zip"
zipped = list(zip(list1,list2))
print (zipped)
unzipped = list(zip(zipped))
print (unzipped)


# In[64]:


import zipfile
zf = zipfile.ZipFile('channel.zip','r')

list1 = "Next nothing is 94191".split()
x = list1[-1]
comments=[]
name = x+".txt"
comments.append(zf.getinfo(name).comment.decode("utf-8"))
f = open("channel\\"+name)
list1 = f.readline().split()
for count in range(0,950):
    f.seek(0)
    print(f.readline())
    zf.getinfo("90506.txt").comment
    x = list1[-1]
    name = x+".txt"
    comments.append(zf.getinfo(name).comment.decode("utf-8"))
    f = open("channel\\"+name)
    list1 = f.readline().split()


# In[66]:


print("".join(comments))


# In[63]:




