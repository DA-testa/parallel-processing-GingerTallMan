# python3

def parallel_processing(n, m, data):
    threads = []
    time = []
    output = []
    for i in range (n):
        threads.append(i)
        time.append(0)
    count = 0
    timer = 0
    for i in range (m):
        output.append (threads[count])
        output.append (time[count])
        while(True):
            time[count] = time[count] + 1
            data[i] = data[i] - 1
            if data[i] == 0:
                break
        
        count+=1
        if count == len(threads):
            count = 0
            timer+=1

    return output

def main():
    first_in = input()
    split_in = first_in.split()
    n = int(split_in[0])
    m = int(split_in[1])

    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)

    for i in range (0,len(result),2):
        print (result[i],result[i+1])


if __name__ == "__main__":
    main()
