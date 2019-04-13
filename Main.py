def prinntfunc(n,*input):
    for i in range(n):
        strr = "["
        for j in range(n):
            strr+= str(input[i][j])
            strr+= " "
        print(strr+"]")
    print (".............")

print ("Solving Ax = b")
n = input("Enter size of matrix c or r (same size)")
A = list()
c =list()
r = list()
det = 1.0
for i in range(n):
    A.append(list())

print ("enter c elements")
for i in range(n):
    c.append(input())

print ("enter r elements")
for i in range(n):
    r.append(input())
z = 0
for i in A:
    v = 0
    for j in range(n):
        if j <= z:
            i.append(c[z-j])
        else:
            i.append(r[1+v])
            v += 1
    z += 1


# print ("now enter values of b")
# b = list()
# for i in range(n):
#     b.append(input())

j =0
for i in A:
        # i.append(b[j])
        # j+=1
        print i

j=0
i=0
while j < n:
    i = j+1
    while i < n:
        if (A[i])[j] != 0:
            A[i] , A[j] = A[j] , A[i]
            det*=-1
            prinntfunc(n,*A)
            break
        i+=1
    i=j+1
    while i < n:
        if (A[i])[j] != 0:
            reduce = float(float((A[i])[j])/(float((A[j])[j])))
            m=0
            while m < n:
                A[i][m] -= reduce*(A[j])[m]
                m+=1
            prinntfunc(n,*A)
        i+=1
    j+=1
# j=n-1
# while j>=0:
#     if (A[j])[j] != 1 and (A[j])[j] != 0:
#         m=j+1
#         while m < n:
#             A[j][m] =float (float (A[j][m]) /float (A[j][j]))
#             m+=1
#         A[j][j] = 1
#         prinntfunc(n, *A)
#     j-=1
print ("A")
prinntfunc(n, *A)
s = 0
for i in range(n):
    if i == s:
        det *= (float)(A[s][s])
        s += 1

print ("det =",det)
# j=n-2
# while j>=0:
#     k=j
#     while k>=0:
#         if (A[k])[j+1] != 0 and (A[j+1][j+1]) != 0:
#             m=j+1
#             reduce = float (A[k][j+1]) /float (A[j+1][j+1])
#             while m < n:
#                 A[k][m] -=float ( reduce* float (A[j+1][m]))
#                 m+=1
#             prinntfunc(n,*A)
#         k-=1
#     j-=1

# for i in A:
#     for j in i:
#         j = round(j,3)
# print ("A afzoodeh final")
# for i in A:
#     print(i)
#
# answerNum = 1
# answer = list()
# if A[n-1][n-1] == 0:
#     if A[n-1][n] != 0:
#         answerNum = 0
#     else:
#         answerNum = 2
# if answerNum == 0:
#     print ("doesn't have answer!")
# elif answerNum == 1:
#     j=0
#     while j<n:
#         answer.append(A[j][n])
#         j+=1
# else:
#     j=0
#     while j<n:
#         i=j+1
#         answer.append("")
#         if A[j][j] == 0:
#             answer[j]+= "x" + str(j+1)
#             j+=1
#             continue
#         while i<n:
#             answer[j] +="(" +str(-A[j][i])+"x"+str(i+1) + ")+"
#             i+=1
#         answer[j] += str(A[j][n])
#         j+=1
# print ("answer(X) : ")
# for i in range(n):
#     print ("["+str(round(answer[i],3))+"]")
#
#
