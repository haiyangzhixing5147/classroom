import time
with  open('chengji.txt') as f:
    film=f.readlines()
ccc=[]
for i in film:
    k=film.index(i)
    kk=[]
    if k==0:
        film[k]=film[k].split()
    else:
        kk=film[k].split()
        kkk=[int(k_0) for k_0 in kk[1:]]
        a=kk[0].split()
        ccc=a+kkk
        film[k]=ccc
film[0].append('总分')
film[0].append('平均分')
num=0
film_all=[]
for ii in film[1:]:
    k=film.index(ii)
    i=0
    k_1 =0
    k_2=0
    num +=1
    for  jj in ii[1:]:
        k_1 += jj
        i +=1
    k_2=float('%.1f'%(k_1/i))
    film[k].append(k_1)
    film[k].append(k_2)
    film_all.append(film[k])
film_pingjun=[0,'平均分',]
i_=0
for ii in range (1,len(film_all[0])):
         i_ +=1
         i=0
         _k=0
         for kk in film_all:
             _k +=kk[i_]
             i +=1
         film_pingjun.append(float('%.1f'%(_k/i)))
film_all_0=sorted(film[1:],key=lambda x:x[1],reverse=True)
for i in film_all_0:
    for k in i[1:]:
        k_0=i.index(k)
        if k<60:
            i[k_0]='不及格'
jieguo=[['名次']]
jieguo[0]+=film[0]
jieguo.append(film_pingjun)
for i in film_all_0:
    k=film_all_0.index(i)+1
    k_=k+1
    jieguo.append([k])
    jieguo[k_] += i
f=open('chengji1.txt','w') 
for i in jieguo:
        print(i)
        i=[str(a) for a in i]
        i='  '.join(i)
        print(i)
        f.writelines(i+'\n')
f.close()
