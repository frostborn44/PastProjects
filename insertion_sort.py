import time

def insertion_sort(in_list):
    
    for index in range(1, len(in_list)):
        current_value = in_list[index] # save the value as it may get overwritten, as its space is used as buffer for shifts in the sorted list
        sorted_index = index-1
        
        while sorted_index >= 0 and in_list[sorted_index] > current_value:
            in_list[sorted_index+1] = in_list[sorted_index]
            sorted_index -= 1
        
        in_list[sorted_index+1] = current_value
    

def main() :
    in_list = list(range(20000,0,-1))

    start = time.time()
    count = insertion_sort(in_list)
    end = time.time()
    
    print("Time:", end - start)
    

if __name__ == '__main__' :
    main()
    #import cProfile
    #cProfile.run('main()')
