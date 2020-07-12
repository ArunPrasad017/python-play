def restoreIpAddresses(s):
    def snapshotIpAddresses(allIpAddress,s,path,):
        # if(segment == 4) or (index ==len(s)):
        #     allIpAddress = path[0]+"."+path[1]+"."+path[2]+"."+path[3]
        #     return
        # elif segment ==4 or index == len(s):
        #     return
            
        # for i in range(1,4):
        #     if index+i <=len(s):
        #         snap = s[index:index+i]
        #         value = int(snap)
        #         if value>255 or (i>=2 and s[index]=='0'):
        #             break;
        #         path[segment]+= value
        #         snapshotIpAddresses(allIpAddress,s,path,index+i,segment+1)
        #         path[segment]=-1


        # Initial base case - our goal and catching any overshoots
        if not s and len(path)==4:
            s='.'.join(path[::-1])
            allIpAddress.append(s)
            return
        #Our constraints
        elif len(path)==4:
            return
        else:
            # other constraints and our recursive function call
            for i in range(1,min(3,len(s))+1):
                if int(s[:i])>=0 and int(s[:i])<256:
                    if i>1 and s[0]=='0':
                        continue
                    else:
                        snapshotIpAddresses(allIpAddress,s[i:], [s[:i]]+path)
            return

        
    path = []
    allIpAddress = []
    snapshotIpAddresses(allIpAddress,s,path)
    return allIpAddress

string="25525511135"
print(restoreIpAddresses(string))