def find_maw(A):
    max = A[0]
    for item in A:
        if item > mat:
            max = item
    return max

array = [20, 34, 12, 93, 84, 39 ,64 ,55, 24] 
print("A =",array)
print("max(A) = ", find_maw(array))       
