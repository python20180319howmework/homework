import pickle
import sys
d={"name":"cai","age":23,"tel":"123456"}

f=open("hwtest","wb")
#将字典序列化写入文件
pickle.dump(d,f)
f.close()

#反序列化，将文件中的字典读出来
f=open("hwtest","rb")
data=pickle.load(f)
print(type(data))
print(data)
