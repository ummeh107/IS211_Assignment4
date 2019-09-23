import time

def sequential_search(a_list, item):
    start = time.time()
    # print(start)
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    # print(end)            
    return end-start


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return end-start

def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()                
    return end-start


def binary_search_recursive(a_list, item):
    start = time.time()
    if len(a_list) == 0:
        return time.time()-start
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return time.time()-start             
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)



import random


def main():    
    for item in [500,1000,10000]:
        seq_src = 0.0
        ord_seq_src = 0.0
        bin_src_itr = 0.0
        bin_src_rcsv = 0.0    
        for i in range(0,100):            
            a_list=[]
            for s in range(1,item):
                a_list.append(random.randint(1,100))
            seq_src += sequential_search(a_list,-1)
            sorted_list = sorted(a_list)
            ord_seq_src += ordered_sequential_search(sorted_list, -1)
            bin_src_itr += binary_search_iterative(sorted_list, -1)
            bin_src_rcsv += binary_search_recursive(sorted_list, -1)
        print("For "+str(item)+" Size :")            
        print("Sequential Search took %10.8f seconds to run, on average" % (seq_src/100))
        print("Order Sequential Search took %10.8f seconds to run, on average" % (ord_seq_src/100)) 
        print("Binary Search Iterative took %10.8f seconds to run, on average" % (bin_src_itr/100)) 
        print("Binary Search Recursive took %10.8f seconds to run, on average" % (bin_src_rcsv/100))  


if __name__ == "__main__":
    main()   


