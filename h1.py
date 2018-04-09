import pickle

d = {'name':'wuhan','age':'21','tel':'17631263523'}

f = open('htest','wb')
pickle.dump(d,f)
f.close()
f = open('htest','rb')
data = pickle.load(f)
print(type(data))
print(data)



