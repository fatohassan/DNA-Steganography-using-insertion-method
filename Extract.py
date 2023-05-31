# A function for extraction

def Extraction():
 original_str = input("Enter the DNA sequence you would like to convert: ")
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
