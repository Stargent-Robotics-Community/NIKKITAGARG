print("Enter number of lines:")
lines = int(input())
for i in range(lines):
    for j in range(i+1):
        print(j+1, end=' ')
    print()