# for i in range(10):
#     # print(i)

A=list(range(1,10,1))
# print(A);
# print(A[2]);
B=0
# while (B<2):
#     # print (B)
#     B=B+1
#     if (B==2):
#         # print("stop di B = 2");

# match B:
#     case 1:
#         result = "one"
#     case 2:
#         result = "two"
#     case 3:
#         result = "three"
#     case _:
#         result = "unknown"

# print(result)

def Evaluasi_kedewasaan(umur:int):
    if umur >= 19:
        print("Anda adalah orang dewasa")  # Runs if condition is True
    elif umur == 17 or umur == 18 :
        print("Anda masih remaja")  # Runs if condition is umur == 17 or umur == 18
    else: 
        print("Anda masih anak anak")  # Runs if condition is False


Evaluasi_kedewasaan(1)