# Hiding secret message inside a DNA sequence

# set variable with input text

def case(a):
 if a == 1:
     Embedding()
 elif a == 2:
     Extraction()
 elif a == 3:
     quit()
 else:
     print("\nEnter valid Choice!")

# A function for embedding

def Embedding():

 # step 1: convert secret text message to binary digits
 secret_msg = input("Type your secret message: ")
 binary_msg = ''.join(format(x, '08b') for x in bytearray(secret_msg,'utf-8'))
 binary_list = [binary_msg[i: i+2] for i in range(0, len(binary_msg), 2)]

 # step 2: convert DNA sequence to binary sequence
 # "binary values to nucleotide sequence"
 # remember:
 # 00 = "A" (adenine)
 # 01 = "G" (guanine)
 # 10 = "C" (cytosine)
 # 11 = "T" (thymine)

 Ref_dna = input("Type DNA sequence: ")

 #check binary secret message must be less than binary DNA sequence

 DNA_encoding = {
 "A": "00",
 "C": "01",
 "G": "10",
 "T": "11"
 }

 DNA_list = []
 for num in Ref_dna:
     for key in list(DNA_encoding.keys()):
         if num == key:
             DNA_list.append(DNA_encoding.get(key))
 DNA_str = "".join(DNA_list)

 # step 3: split every three digits on it's own of the binary DNA sequence

 split_list = []
 for i in range(0, len(DNA_str) - 2):
     if i % 3 == 0:
         split_list.append(DNA_str[i: i+3])

 # step 4: add binary secret message one by one in the beginning of the binary splitted sequence

 if len(binary_msg) <= len(split_list):
     insert_list = []
     for j in range(0, len(binary_msg)):
         insert_list.append(str(binary_msg[j]) + str(split_list[j]))
     stegoString = str.join("", insert_list)

 # Step 5: convert binary stego-DNA sequence into a stego-DNA sequence

 binary_list = [stegoString[i: i+2] for i in range(0,len(stegoString), 2)]
 DNA_encoding1 = {
 "00": "A",
 "01": "C",
 "10": "G",
 "11": "T"
 }
 DNA_lis = []
 for num in binary_list:
     for key in list(DNA_encoding1.keys()):
         if num == key:
             DNA_lis.append(DNA_encoding1.get(key))
 DNA_st = "".join(DNA_lis)

 # print the process step by step

 print("\nThe secret message: " + "\n" + secret_msg + "\n")
 print("The message after binary conversion: " + "\n" + binary_msg + "\n")
 print("The DNA sequence: " + "\n" + Ref_dna + "\n")
 print("The DNA sequence after binary conversion : " + "\n" + DNA_str + "\n")
 print("The binary DNA sequence after splitting into segments: " + "\n" + str(split_list) + "\n")
 print("The binary splitted stego-DNA after applying insertion method: " + "\n" + str(insert_list) + "\n")
 print("The binary stego-DNA: " + "\n" + stegoString + "\n")
 print("The stego-DNA: " + "\n" + DNA_st + "\n")

def Extraction():
 original_str = input("Type the DNA sequence you would like to convert: ")
 DNA_encoding = {
 "A": "00",
 "C": "01",
 "G": "10",
 "T": "11"
 }
 #step 1: convert stego-DNA sequence into binary bits
 DNA_list = []
 for num in original_str:
     for key in list(DNA_encoding.keys()):
         if num == key:
             DNA_list.append(DNA_encoding.get(key))
 DNA_str = "".join(DNA_list)
 # step 2: split every four digits on it's own of the binary stego-DNA sequence

 split_list2 = []
 for i in range(0, len(DNA_str) - 2):
     if i % 4 == 0:
         split_list2.append(DNA_str[i: i + 4])

 # step 3: extract the secret message bits

 insert_list = []
 for j in range(0, len(DNA_str)):
     if j % 4 == 0:
         insert_list.append(DNA_str[j: j + 1])
 secret = str.join("", insert_list)

 # step 4: convert binary secret message to a secret text message

 input_string = int(str(secret), 2)
 Total_bytes = (input_string.bit_length() + 7) // 8
 input_array = input_string.to_bytes(Total_bytes, "big")
 ASCII_value = input_array.decode()

 # print input text, binary code and DNA sequence
 print("\nThe stego-DNA is :" + "\n" + original_str + "\n")
 print("The binary converted stego-DNA is :" + "\n" + DNA_str + "\n")
 print("The stego-DNA after splitting into segments is :" + "\n" + str(split_list2) + "\n")
 print("The binary bits of secret message : " + "\n" + str(insert_list) + "\n")
 print("The binary secret message :" + "\n" + secret + "\n")
 print("The secret message is :" + "\n" + ASCII_value + "\n")


while(1):
 print("\nSelect an option: \n1)Embed\n2)Extract\n3)exit")
 val = int(input("\nChoice:"))
 case(val)
