import time

f = open('input.txt', 'r')

nums = [0]*2
i = 0

for line in f:
    for token in line.split():
        nums[i] = token
        i = i + 1

print('nums0: ', nums[0])
print('nums1: ', nums[1])

if (int(nums[0]) > int(nums[1])):
    for i in range(len(nums)):
        nums[i] = str(bin(int(nums[i]))[2:])
    print(nums[0])
    print(nums[1])
    

    while(int(nums[0], 2) > int(nums[1], 2)):
        i = 0
        oldnums = nums[0]
        # time.sleep(1)

        while( (i <= len(nums[0]) - 2) ):

            print('nums0i: ', nums[0][i])
            print('nums0i+1: ', nums[0][i+1])
            if (nums[0][i] == '0'):
                print('break', i)
            elif (nums[0][i] == '1'):
                print('Swap away, kids!')

                numsDigits = [0]*(len(nums[0]))

                for j in range(len(numsDigits)):
                    numsDigits[j] = nums[0][j]

                numsDigits[i] = numsDigits[i+1]
                numsDigits[i+1] = '1'

                print('numsDigits: ', numsDigits)

                nums[0] = numsDigits[0]

                for j in range(1, len(numsDigits)):
                    nums[0] = nums[0] + numsDigits[j]

                # nums[0][i] = nums[0][i+1] 
                # nums[0][i+1] = '1' 
            print('nums0: ', nums[0])
            print(i)
            i = i + 1

            print('\n')

        if oldnums == nums[0]:
            print('Stop repeating')
            break

        nums[0] = int(nums[0], 2)
        nums[1] = int(nums[1], 2)

        diff = nums[1] - nums[0]

        for i in range(len(str(nums[0]))):
            if str(diff) == str(nums[0])[i]:
                nums[0] = nums[0] + diff
                break
            else:
                print(' ')

        nums[0] = str(bin(nums[0])[2:])
        nums[1] = str(bin(nums[1])[2:])
 
    if (int(nums[0], 2) != int(nums[1], 2)):
        print('No solution exists.')
    else:
        print('A solution exists, but I\'m going to bed now.')

    # nums[0] = int(nums[0], 2)
    # nums[1] = int(nums[1], 2)
    print('The transformed pair: ', int(nums[0], 2), int(nums[1], 2))
else:
    print('Shaka Zulu')
    
f.close()
# print(nums[0])
# print(int(str(nums[0]), 2))
# print(int(nums[0]))
# print(int(nums[1]))
