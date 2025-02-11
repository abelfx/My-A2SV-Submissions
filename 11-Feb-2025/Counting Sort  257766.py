# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem


def countingSort(arr):
    
    dict = Counter(arr)
    
    result = [0] * (100)
    
    for keys, values in dict.items():
        result[keys] = values
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
