import os
import argparse
from attack_with_englishdic import Decrypt_withEngDic
from rail_fence import encryptRailFence, decryptRailFence
from h import MahoaCesar, TanCongCesar
import time

def readfile(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data

def writefile(file_name,content):
	with open(file_name, "w") as myfile:
		myfile.write(content)

def encryptMessageByRailFence(fileTestcase):
	data = readfile("testcase/"+fileTestcase)
	print("Enter rail-fence key from 2 to",(len(data) - 1))
	RailFenceKey = int(input())
	cipher = encryptRailFence(data,RailFenceKey)
	file_name_dest = "cipher_of_" + fileTestcase
	writefile("cipher_rail_fence/" + file_name_dest, cipher)
	return file_name_dest

if __name__ == "__main__":

# chi tieng anh va khong co ki tu khac
#  ke ca dau xuong dong

	parser = argparse.ArgumentParser()

	parser.add_argument("-m", "--method", help = "enter encrypt method")
 
	parser.add_argument("-t", "--testcase", help = "enter testcase file")
	
	args = parser.parse_args()
	if args.method == "railfence":
		# encrypt rail fence
		file_name_dest = encryptMessageByRailFence(args.testcase)

		# hacking cipher
		cipher = readfile("cipher_rail_fence/" +file_name_dest)
		decrypt_withEngDic_Instance = Decrypt_withEngDic()

		print('Attack Rail_fence Cipher with English Dictionary:')
		start_time = time.time()
		resultHacking = decrypt_withEngDic_Instance.attack_Rail_fence(cipher)
		end_time = time.time()
		print('We calculate the key:')
		print(resultHacking['key'])
		elapsed_time = end_time - start_time
		print ("Elapsed_time: {0}".format(elapsed_time) + "[sec]")
		print('Score:')
		print(resultHacking['score'])
		print('Plaintext:')
		print(resultHacking['plaintext'])

		
		# print('Score 400:')
		# print(decrypt_withEngDic_Instance.get_english_score("is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. "))


		# write file
		file_result = 'result_' + args.testcase 
		writefile("result_hacking_rail_fence/"+file_result, "We calculate the key of "+args.testcase+ ":\n" + str(resultHacking['key']) + "\nElapsed_time: {0}".format(elapsed_time) + "[sec]"+'\nScore:\n' + str(resultHacking['score'])  +"\nPlaintext:\n" + resultHacking['plaintext'] )

	elif args.method == "product":
		# encrypt
		data = readfile("testcase/"+args.testcase)
		print("Enter cesar key from 1 to 25")
		CesarKey = int(input())
		cipherCesar = MahoaCesar(data, CesarKey)
		print("Enter rail-fence key from 2 to",(len(data) - 1))
		RailFenceKey = int(input())
		cipherProduct = encryptRailFence(cipherCesar, RailFenceKey)  
		print("Product cipher: ")
		print(cipherProduct)

		# decrypt
		decryptRailFence = decryptRailFence(cipherProduct, RailFenceKey)
		decryptCesar = TanCongCesar(decryptRailFence, CesarKey)
		print("Decode product cipher: ")
		print(decryptCesar)	
		# hacking
		print("Attack product cipher with English Dictionary:")
		decrypt_withEngDic_Instance = Decrypt_withEngDic()
		print(decrypt_withEngDic_Instance.attack_Product(cipherProduct))


	else:
		raise ValueError("Invalid method.")
