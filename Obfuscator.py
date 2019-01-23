import math
import random

def xorcipher(text):
    xorkey = '3'
    l = len(text)
    for i in range(0,l):
        text[i] = text[i]^xorkey
    return text

def encryptRailFence(text, key): 

	 
	rail = [['\n' for i in range(len(text))] 
				for j in range(key)] 
	
	 
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)): 
		
		 
		if (row == 0) or (row == key - 1): 
			dir_down = not dir_down 
		
		 
		rail[row][col] = text[i] 
		col += 1
		
		 
		if dir_down: 
			row += 1
		else: 
			row -= 1
	 
	result = [] 
	for i in range(key): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	return("" . join(result))
et1='''
void encryptDecrypt(char inpString[])
{
    char xorKey = 'P';
    int len = strlen(inpString);

    for (int i = 0; i < len; i++)
    {
        inpString[i] = inpString[i] ^ xorKey;
        cout<<inpString[i];
    }
}
'''
et2='''void decryptRailFence(string cipher, int key)
{
    // create the matrix to cipher plain text
    // key = rows , length(text) = columns
    char rail[key][cipher.length()];

    // filling the rail matrix to distinguish filled
    // spaces from blank ones
    for (int i=0; i < key; i++)
        for (int j=0; j < cipher.length(); j++)
            rail[i][j] = '    ';

    // to find the direction
    bool dir_down;

    int row = 0, col = 0;

    // mark the places with '*'
    for (int i=0; i < cipher.length(); i++)
    {
        // check the direction of flow
        if (row == 0)
            dir_down = true;
        if (row == key-1)
            dir_down = false;

        // place the marker
        rail[row][col++] = '*';

        // find the next row using direction flag
        dir_down?row++ : row--;
    }

    // now we can construct the fill the rail matrix
    int index = 0;
    for (int i=0; i<key; i++)
        for (int j=0; j<cipher.length(); j++)
            if (rail[i][j] == '*' && index<cipher.length())
                rail[i][j] = cipher[index++];


    // now read the matrix in zig-zag manner to construct
    // the resultant text
    string result;

    row = 0, col = 0;
    for (int i=0; i< cipher.length(); i++)
    {
        // check the direction of flow
        if (row == 0)
            dir_down = true;
        if (row == key-1)
            dir_down = false;

        // place the marker
        if (rail[row][col] != '*')
            result.push_back(rail[row][col++]);

        // find the next row using direction flag
        dir_down?row++: row--;
    }
    cout<<result<<endl;
}
	'''
str='''# include <bits/stdc++.h> 
using namespace std; 
  
// Returns max possible value of i*arr[i] 
int maxSum(int arr[], int n) 
{ 
    // Find array sum and i*arr[i] with no rotation ;
    int arrSum = 0;  // Stores sum of arr[i] 
    int currVal = 0;  // Stores sum of i*arr[i] 
    for (int i=0; i<n; i++) 
    { 
        arrSum = arrSum + arr[i]; 
        currVal = currVal+(i*arr[i]); 
    } 
  
    // Initialize result as 0 rotation sum 
    int maxVal = currVal; 
  
    // Try all rotations one by one and find 
    // the maximum rotation sum. 
    for (int j=1; j<n; j++) 
    { 
        currVal = currVal + arrSum-n*arr[n-j]; 
        if (currVal > maxVal) 
            maxVal = currVal; 
    } 
  
    // Return result 
    return maxVal; 
} 
  
int main() 
{
//out << "";
    int arr[10];
    arr[0]=10;
    arr[1]=1;
    arr[2]=2;
    arr[3]=3;
    arr[4]=4;
    arr[5]=5;
    arr[6]=6;
    arr[7]=7;
    arr[8]=8;
    arr[9]=9;
    
    cout<<"bharat";
    int n = sizeof(arr)/sizeof(arr[0]); 
    cout <<"Max sum is "<<maxSum(arr, n); 
    return 0; 
}  
'''
dc1='''int getMax(int arr[], int n)
{
    int mx = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] > mx)
            mx = arr[i];
            }
    return mx;
}
void countSort(int arr[], int n, int exp)
{
    int output[n];
    int i, count[10] = {0};
    for (i = 0; i < n; i++)
    {
        count[ (arr[i]/exp)%10 ]++;
        }
    for (i = 1; i < 10; i++)
    {
        count[i] += count[i - 1];
        }

    for (i = n - 1; i >= 0; i--)
    {
        output[count[ (arr[i]/exp)%10 ] - 1] = arr[i];
        count[ (arr[i]/exp)%10 ]--;
    }

    for (i = 0; i < n; i++)
    {
        arr[i] = output[i];
        }
}

void ewqr(int arr[], int n)
{
  int m = getMax(arr, n);

    for (int exp = 1; m/exp > 0; exp *= 10)
    {
        countSort(arr, n, exp);
        }
}'''
dc2='''int jhgdasjh()
{
//out<<"dc2"<<endl;
    int arr[700];
    int key = 50;
    int low = 0;
    int high = key - 1;
    int mid;

    while ((arr[high] != arr[low]) && (key >= arr[low]) && (key <= arr[high])) {
        mid = low + ((key - arr[low]) * (high - low) / (arr[high] - arr[low]));

        if (arr[mid] < key)
            low = mid + 1;
        else if (key < arr[mid])
            high = mid - 1;
        else
            return mid;
    }

    if (key == arr[low])
        return low ;
    else
        return -1;
}'''
dc3='''void dskfajdgfj(int n)
{
//out<<"dc3"<<endl;
    bool prime[n+1];
    memset(prime, true, sizeof(prime));

    for (int p=2; p*p<=n; p++)
    {

        if (prime[p] == true)
        {

            for (int i=p*2; i<=n; i += p)
            {
                prime[i] = false;
            }
        }
    }
}'''
dc4='''int kjahskjf(int limit)
{
//out<<"dc4"<<endl;
    if (limit > 2)
        cout << " ";
    if (limit > 3)
        cout << " ";

    bool sieve[limit];
    for (int i = 0; i < limit; i++)
    {
        sieve[i] = false;
        }

    for (int x = 1; x * x < limit; x++) {
        for (int y = 1; y * y < limit; y++) {

            int n = (4 * x * x) + (y * y);
            if (n <= limit && (n % 12 == 1 || n % 12 == 5))
                sieve[n] ^= true;

            n = (3 * x * x) + (y * y);
            if (n <= limit && n % 12 == 7)
                sieve[n] ^= true;

            n = (3 * x * x) - (y * y);
            if (x > y && n <= limit && n % 12 == 11)
                sieve[n] ^= true;
        }
    }
}'''
dc5='''
void xhjdgshjkdgs()
{
   /*jkdfghdhfkghjkgdfhgkjd
   kdjfghkjdfhgkj4dfjhdfgkjkjghkj
   */
}'''
dc6='''
int sjdhfgjhs()
{
//out<<"dc6"<<endl;
    int arr[5];
    arr[0]=5;
    arr[1]=0;
    arr[2]=9;
    arr[3]=8;
    arr[4]=3;
    int x = 4;
    int n = 3 ;
    if (x >= arr[n-1])
        return n-1;
    if (x < arr[0])
        return -1;
    for (int i=1; i<n; i++)
    {
    if (arr[i] > x)
        return (i-1);
        }
    return -1;
}'''

def fun1():
      s="_"
      t=random.randint(7,26)
      list1=['l','1','I']
      for i in range(1,t):
            k=random.randint(0,2)
            s=s+list1[k]
      return s

def fun2():
      s="_"
      t=random.randint(7,25)
      list1=['0','O']
      for i in range(1,t):
            k=random.randint(0,1)
            s=s+list1[k]
      return s

def fun3():
      s="x"
      t=random.randint(7,50)
      list1=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
      for i in range(1,t):
            k=random.randint(0,14)
            s=s+list1[k]
      return s
def fun4():
      s="x"
      t=random.randint(7,80)
      for i in range(1,t):
            s=s+"_"
      return s
#variable renaming
    
def funct(str3333):
          f=0
          x=['abcd']
          last_found=-1
          while True:
                last_found = str3333.find("int", last_found + 1)
                if last_found == -1:  
                      break  # All occurrences have been found
                else:
                      f=str3333.find(";",last_found+1)
                      s=str3333[last_found+3:f]
                      s=s.replace(' ','')
                      y=s.split(",")
                      x=x+y
          ren=["abcd"]
          for x11 in x:
                t=random.randint(0,3)
                if(t==0):
                      rename1=fun1()
                      ren.append(rename1)
                elif(t==1):
                      rename1=fun2()
                      ren.append(rename1)
                elif(t==2):
                      rename1=fun3()
                      ren.append(rename1)
                else:
                      rename1=fun3()
                      ren.append(rename1)
          for ttt in range(0,len(x)):
              xxx=x[ttt]
              xx=xxx.find("=")
              if(xx!=-1):
                xxx=xxx[0:xx]
                x[ttt]=xxx
          for ttt in range(0,len(x)):
              xxx=x[ttt]
              xx=xxx.find("[")
              if(xx!=-1):
                xxx=xxx[0:xx]
                x[ttt]=xxx        
          
          
              
          list4=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',1,2,3,4,5,6,7,8,9,0];
          t=-1
          for x11 in x:
              last_found=-1
              t=t+1
              while True:
                  last_found=str3333.find(x11,last_found+1)
                  sak=last_found+len(x11)-1
                  abc=str3333.rfind(";",0,last_found)
                  bcd=str3333.rfind('"',0,last_found)
                  if last_found==-1:
                      break
                  elif(list4.count(str3333[sak+1])==0):
                      if(abc>bcd):
                        if(list4.count(str3333[last_found-1])==0):   
                            str3333=str3333[:last_found]+ren[t]+str3333[last_found+len(x11):]
          #char rename
          f=0
          x=['abcd']
          last_found=-1
          while True:
                last_found = str3333.find("char", last_found + 1)
                if last_found == -1:  
                      break  # All occurrences have been found
                else:
                      f=str3333.find(";",last_found+1)
                      s=str3333[last_found+4:f]
                      s=s.replace(' ','')
                      y=s.split(",")
                      x=x+y
          ren=["abcd"]
          for x11 in x:
                t=random.randint(0,3)
                if(t==0):
                      rename1=fun1()
                      ren.append(rename1)
                elif(t==1):
                      rename1=fun2()
                      ren.append(rename1)
                elif(t==2):
                      rename1=fun3()
                      ren.append(rename1)
                else:
                      rename1=fun4()
                      ren.append(rename1)
          
          list4=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',1,2,3,4,5,6,7,8,9,0];
          t=-1
          for x11 in x:
              last_found=-1
              t=t+1
              while True:
                  last_found=str3333.find(x11,last_found+1)
                  sak=last_found+len(x11)-1
                  abc=str3333.rfind(";",0,last_found)
                  bcd=str3333.rfind('"',0,last_found)
                  if last_found==-1:
                      break
                  elif(list4.count(str3333[sak+1])==0):
                      if(abc>bcd):
                        if(list4.count(str3333[last_found-1])==0):   
                            str3333=str3333[:last_found]+ren[t]+str3333[last_found+1:]
          
          #float rename
          f=0
          x=['abcd']
          last_found=-1
          while True:
                last_found = str3333.find("float", last_found + 1)
                if last_found == -1:  
                      break  # All occurrences have been found
                else:
                      f=str3333.find(";",last_found+1)
                      s=str3333[last_found+5:f]
                      s=s.replace(' ','')
                      y=s.split(",")
                      x=x+y
          ren=["abcd"]
          for x11 in x:
                t=random.randint(0,3)
                if(t==0):
                      rename1=fun1()
                      ren.append(rename1)
                elif(t==1):
                      rename1=fun2()
                      ren.append(rename1)
                elif(t==2):
                      rename1=fun3()
                      ren.append(rename1)
                else:
                      rename1=fun4()
                      ren.append(rename1)
          
          list4=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',1,2,3,4,5,6,7,8,9,0];
          t=-1
          for x11 in x:
              last_found=-1
              t=t+1
              while True:
                  last_found=str3333.find(x11,last_found+1)
                  sak=last_found+len(x11)-1
                  abc=str3333.rfind(";",0,last_found)
                  bcd=str3333.rfind('"',0,last_found)
                  if last_found==-1:
                      break
                  elif(list4.count(str3333[sak+1])==0):
                      if(abc>bcd):
                        if(list4.count(str3333[last_found-1])==0):   
                            str3333=str3333[:last_found]+ren[t]+str3333[last_found+1:]
          
          #double
          f=0
          x=['abcd']
          last_found=-1
          while True:
                last_found = str3333.find("double", last_found + 1)
                if last_found == -1:  
                      break  # All occurrences have been found
                else:
                      f=str3333.find(";",last_found+1)
                      s=str3333[last_found+6:f]
                      s=s.replace(' ','')
                      y=s.split(",")
                      x=x+y
          ren=["abcd"]
          for x11 in x:
                t=random.randint(0,2)
                if(t==0):
                      rename1=fun1()
                      ren.append(rename1)
                elif(t==1):
                      rename1=fun2()
                      ren.append(rename1)
                elif(t==2):
                      rename1=fun3()
                      ren.append(rename1)
                else:
                      rename1=fun4()
                      ren.append(rename1)
          
          list4=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',1,2,3,4,5,6,7,8,9,0];
          t=-1
          for x11 in x:
              last_found=-1
              t=t+1
              while True:
                  last_found=str3333.find(x11,last_found+1)
                  sak=last_found+len(x11)-1
                  abc=str3333.rfind(";",0,last_found)
                  bcd=str3333.rfind('"',0,last_found)
                  if last_found==-1:
                      break
                  elif(list4.count(str3333[sak+1])==0):
                      if(abc>bcd):
                        if(list4.count(str3333[last_found-1])==0):   
                            str3333=str3333[:last_found]+ren[t]+str3333[last_found+1:]
          return (str3333)
# pattern

'''str2=str.split(' ')
d= (1) + (8*len(str2));

# find two solutions
sol1 = (-1- (math.sqrt(d)))/(2)
sol2 = (-1+ (math.sqrt(d)))/(2)
if(sol1>0):
    sol=sol1
else:
    sol=sol2
sol=int(sol)+1
k=0
for i in range(0, sol): 
      
        
        for j in range(0, i+1): 
          
            
            if(k<len(str2)):
                 print(str2[k],end="")
                 k=k+1;
       
        
        print("\r")

str=str.replace("\n"," ")
str=str.replace(";","; ")
str2=str.split(" ")
j=-1
for i in range(10,):
    for k in range(1,i):
        if(j==len(str2)):
            break;
        else:
            j=j+1
            print(str2[j])
    if(j==len(str2)):
        break;'''
# loops with dead code 
sak=str.find(";")
last_found=-1
while True:
      last_found=str.find("for",last_found+1)
      if(last_found==-1):
            break
      f_for=str.find("{",last_found+1)
      j=f_for
      l=1
      while l!=0:
            f1_for=str.find("{",f_for+1)
            s1_for=str.find("}",f_for+1)
            if(f1_for==-1):
                  l=l-1
                  f_for=s1_for
            elif(f1_for<s1_for):
                  l=l+1
                  f_for=f1_for
            else:
                  l=l-1
                  f_for=s1_for
      dc=random.randint(2,6)
      if(dc==2):
            str=str[:j+1]+"jhgdasjh();"+str[j+1:]
      elif(dc==3):
           str=str[:j+1]+"dskfajdgfj(45);"+str[j+1:]
      elif(dc==4):
           str=str[:j+1]+"kjahskjf(35);"+str[j+1:]
      elif(dc==5):
           str=str[:j+1]+"xhjdgshjkdgs();"+str[j+1:]
      elif(dc==6):
           str=str[:j+1]+"sjdhfgjhs();"+str[j+1:]
str=str[0:sak+1]+"\n"+dc2+str[sak+1:]
str=str[0:sak+1]+"\n"+dc5+str[sak+1:]
str=str[0:sak+1]+"\n"+dc3+str[sak+1:]
str=str[0:sak+1]+"\n"+dc6+str[sak+1:]
str=str[0:sak+1]+"\n"+dc4+str[sak+1:]

# string encryption
ind_1=0
last_found=-1
str135=''
str246=str
aa=[]
bb=[]
cc=[]
dd=[]
ee=[]
while True:
      last_found=str.find("cout",last_found+1)
      if(last_found ==-1):
            break
      j=str.find(";",last_found+1)
      aa.append(str[last_found:j+1])
      str1=str[last_found:j+1]
      cc.append(str1.count("<<"))
      t1=-1
      while True:
            t1=str1.find('<<',t1+1)
            if(t1==-1):
                  break
            if(str1[t1+2]=='"'):
                t2=str1[t1+3:str1.find('"',t1+3)]
                dd.append("decryptRailFence("+"\""+encryptRailFence(t2,2)+"\",2);")
            else:
                if(str1.find('<<',t1+2)!=-1):
                    yy=str1.find('<<',t1+2)
                else:
                    yy=str1.find(';',t1)
                dd.append("cout<<"+str1[t1+2:yy]+";")

for index_st in range(0,len(cc)):
        lll=cc[index_st]
        str135=''
        for index_s in range(0,lll):
            str135=str135+(dd[ind_1+index_s])
        ind_1=ind_1+lll
        ee.append(str135)

for index_t in range(0,len(aa)):
        str=str.replace(aa[index_t],ee[index_t])
str=str[0:str.find(";")+1]+et2+str[str.find(";")+1:]


#variable in functions
str123=str
beech=[]
nobeech=[]
prev_end=0
start=-1
coun_t=0
index=-1
end=-1
while True:
    close=str123.find("}",index+1)
    opens=str123.find("{",index+1)
    if(close!=-1 & opens!=-1):
         if(close<opens):
              coun_t=coun_t-1
              if(coun_t==0):
                 end=close
              index=close
         else:
              if(coun_t==0):
                 start=opens
              coun_t=coun_t+1
              index=opens
         if (start<end):
             str4=funct(str123[start:end+1])
             str5=str123[prev_end:start]
             prev_end=end+1
             beech.append(str5)
             nobeech.append(str4)
    elif(opens==-1& close==-1):
        str5=str123[prev_end:start]
        str4=funct(str123[start:end+1])
        beech.append(str5)
        nobeech.append(str4)
        break
    elif(opens==-1):
         coun_t=coun_t-1
         if(coun_t==0):
             end=close
         index=close
str=''         
for i in range(0,len(beech)):
    str=str+beech[i]+'\n'+nobeech[i]
            
        
    
#using define
used2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def fundefine ():
      s="x"
      while True:
          t=random.randint(3,39)
          if(used2[t-1]==0):
              used2[t-1]=1
              s=s+("_"*t)
              return s                 
key_word=["for","int","float","double","char","string","while","switch","do","if","else","return","bool"]
key_word1=["for","int","float","double","char","string","while","switch","do","if","else","return","bool"]
for iter in range (10,35):
    ran_gen=random.randint(1,12)
    finder=str.find("# include")
    sss=fundefine()
    str=str[0:finder]+"# define "+sss+" "+key_word1[ran_gen]+'\n'+str[finder:]
    key_word1[ran_gen]=sss
for iter2 in range(0,13):
    if(key_word1[iter2]!=key_word[iter2]):
       finder=str.find("# include")
       str222=str[finder:]
       str222=str222.replace(key_word[iter2],key_word1[iter2])
       str=str[0:finder]+str222 
# digraphs and trigraphs
'''a = ["#","\\","^","[","]","|","{","}","~"]
b = ["??=","??/","??'","??(","??)","??!","??<","??>","??-"]
t=-1
for a1 in a:
      last_found=-1
      t=t+1
      while True:
            last_found=str.find(a1,last_found+1)
            abc=str.rfind(";",0,last_found)
            bcd=str.rfind('"',0,last_found)
            if(last_found==-1):
                  break
            if(bcd==-1):
                  str=str[:last_found]+b[t]+str[last_found+1:]
            elif(bcd<abc):
                 str=str[:last_found]+b[t]+str[last_found+1:]'''

print(str)
