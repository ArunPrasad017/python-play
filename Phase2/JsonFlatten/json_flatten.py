##flatten a nested json 

data = {
    "id": 1,
    "first_name": "Jonathan",
    "last_name": "Hsu",
    "employment_history": [
        {
            "company": "Black Belt Academy",
            "title": "Instructor",
            "something": {
                "hello": [1,2,3,{
                    "something":"goes"
                }]
            }
        }]}
# recursive method
out = {}
def flatten(d,key=''):
    if type(d) is dict:
        for a in d:
            flatten(d[a],key+a+'-')
    elif type(d) is list:
        i=0
        for a in d:
            flatten(a,key+str(i)+'-')
            i+=1
    else:
        out[key[:-1]]=d

flatten(data)
print(out)