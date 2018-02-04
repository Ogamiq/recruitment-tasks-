hacks = ['ccbc','baaca','babacaba','aabacabaaaca','abc','baad']
powers = [20,31,55,81,6,0]

def hack_calculator(hack):
    length = len(hack)
    a_counter = 0
    b_counter = 0
    c_counter = 0
    baa_counter = 0
    ba_counter = 0

    for i in range(length):
        if(hack[i] == 'a'):
            a_counter += 1
        elif(hack[i] == 'b'):
            b_counter += 1
            if(i + 2 < length and hack[i + 1]=='a' and hack[i + 2]=='a'):
                baa_counter += 1
            elif(i + 1 < length and hack[i + 1]=='a'):
                ba_counter += 1
        elif(hack[i] == 'c'):
            c_counter += 1
        else:
            return 0

    return sum(range(a_counter+1))+2*sum(range(b_counter+1))+3*sum(range(c_counter+1))+20*baa_counter+10*ba_counter

#test
for hack in hacks:
    print(hack_calculator(hack))