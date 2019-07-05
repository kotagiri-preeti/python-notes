batch=[40,39,35,30,25,20]
cut=25
for i in batch:
    assert i>25,"rejected"
    print(str(i)+"is ok")
