num_list=input().split()
M=int(num_list[0])
N=int(num_list[1])
if M%2==0 or N%2==0:
    print(int(M*N/2))
else:
    print(int((M*N-1)/2))