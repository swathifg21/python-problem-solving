N = int(input("ENTER THE NUMBER OF TERMS: "))
A, B = 0, 1
print("FIBONACCI SERIES:")
print(A)
print(B)
for _ in range(2, N):
    C = A + B
    print(C)
    A, B = B, C
