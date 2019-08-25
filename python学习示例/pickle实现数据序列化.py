import pickle
data1={'Jack':[32,'male','Market'],
       'Suan':[28,'female','Adverting'],
       'Black':[50,'male','Accounting'],}
List1=[1,2,3]
List1.insert(0,List1)
output=open('data.pkl','wb')
pickle.dump(data1,output,0)
pickle.dump(List1,output,-1)
output.close()

pk1_file=open('data.pkl','rb')
data1=pickle.load(pk1_file)
print(data1)
data2=pickle.load(pk1_file)
print(data2)
pk1_file.close()
