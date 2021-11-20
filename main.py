# import os
import argparse
from attack_with_englishdic import Decrypt_withEngDic
from rail_fence import encryptRailFence, decryptRailFence
from cesar import MahoaCesar, TanCongCesar
import time

def readfile(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data

# remove old content first
def overwritefile(file_name,content):
	with open(file_name, "w") as myfile:
		myfile.write(content)

def writefile(file_name,content):
	with open(file_name, "a") as myfile:
		myfile.write(content)		

def encryptFileMessageByRailFence(fileTestcase):
	data = readfile("testcase/"+fileTestcase)
	print("Enter rail-fence key from 2 to",(len(data) - 1))
	RailFenceKey = int(input())
	cipher = encryptRailFence(data,RailFenceKey)
	print("-----------------------------------")
	print("Plaintext:")
	print(data)
	print("-----------------------------------")
	print("Rail fence cipher with key = " + str(RailFenceKey) +":")
	print(cipher)
	print("-----------------------------------")
	# write cipher result to file text
	file_name_dest = "cipher_of_" + fileTestcase
	overwritefile("cipher_rail_fence/" + file_name_dest, cipher)
	#  write final result
	file_result = 'result_' + fileTestcase 
	content = "-----------------------------------"  + "\nPlaintext:\n" + data + "\n-----------------------------------" + "\nRail fence cipher with key = " + str(RailFenceKey) + ":\n"+ cipher + "\n-----------------------------------\n"
	overwritefile("result_hacking_rail_fence/" + file_result, content)

	return file_name_dest

def encryptFileMessageByProduct(fileTestcase):
	data = readfile("testcase/"+fileTestcase)
	print("Enter cesar key from 1 to 25")
	CesarKey = int(input())
	cipherCesar = MahoaCesar(data, CesarKey)
	print("Enter rail-fence key from 2 to",(len(data) - 1))
	RailFenceKey = int(input())
	cipherProduct = encryptRailFence(cipherCesar, RailFenceKey)  
	print("-----------------------------------")
	print("Plaintext:")
	print(data)
	print("-----------------------------------")
	print("Cesar cipher, cesar key = "+ str(CesarKey)+ ":")
	print(cipherCesar)
	print("-----------------------------------")
	print("Rail fence encryption of the generated cesar ciphertext, Rail fence key = " + str(RailFenceKey) + " (Product cipher):")
	print(cipherProduct)
	print("-----------------------------------")
	# write cipher result to file text
	file_name_dest = "cipher_of_" + fileTestcase
	overwritefile("cipher_product/" + file_name_dest, cipherProduct)
	#  write final result
	file_result = 'result_' + fileTestcase 
	content = "-----------------------------------"  + "\nPlaintext:\n" + data + "\n-----------------------------------" + "\nCesar cipher, cesar key = "+ str(CesarKey)+ ":\n"+ cipherCesar + "\n-----------------------------------" +"\nRail fence encryption of the generated cesar ciphertext, Rail fence key = " + str(RailFenceKey) + " (Product cipher):\n" + cipherProduct + "\n-----------------------------------\n"
	overwritefile("result_hacking_product/" + file_result, content)
	return file_name_dest

def printHackingResult(resultHacking, elapsed_time):
	if 'key' in resultHacking:
		print('Attack Rail_fence Cipher with English Dictionary:')
		print('We calculate the key:')
		print(resultHacking['key'])
		print ("Elapsed_time: {0}".format(elapsed_time) + "[sec]")
		print('Score:')
		print(resultHacking['score'])
		print('Plaintext:')
		print(resultHacking['plaintext'])
	else:
		print('Attack Product Cipher with English Dictionary:')
		print('We calculate the key:')
		print('Cesar key: ' + str(resultHacking['key_cesar']))
		print('Rail fence key: ' + str(resultHacking['key_rail_fence']))
		print ("Elapsed_time: {0}".format(elapsed_time) + "[sec]")
		print('Score:')
		print(resultHacking['score'])
		print('Plaintext:')
		print(resultHacking['plaintext'])
	print("-----------------------------------")

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument("-m", "--method", help = "enter encrypt method")
 
	parser.add_argument("-t", "--testcase", help = "enter testcase file")
	
	args = parser.parse_args()
	if args.method == "railfence":
		# encrypt rail fence
		file_name_dest = encryptFileMessageByRailFence(args.testcase)

		# hacking cipher
		cipher = readfile("cipher_rail_fence/" +file_name_dest)
		decrypt_withEngDic_Instance = Decrypt_withEngDic()
		# Print result
		start_time = time.time()
		resultHacking = decrypt_withEngDic_Instance.attack_Rail_fence(cipher)
		end_time = time.time()
		elapsed_time = end_time - start_time
		printHackingResult(resultHacking, elapsed_time)

		# write file
		file_result = 'result_' + args.testcase 
		writefile("result_hacking_rail_fence/"+file_result, "We calculate the key of "+args.testcase+ ":\n" + str(resultHacking['key']) + "\nElapsed_time: {0}".format(elapsed_time) + "[sec]"+'\nScore:\n' + str(resultHacking['score'])  +"\nPlaintext:\n" + resultHacking['plaintext'] )

	elif args.method == "product":
		# encrypt
		file_name_dest = encryptFileMessageByProduct(args.testcase)

		# hacking
		cipherProduct = readfile("cipher_product/" +file_name_dest)
		decrypt_withEngDic_Instance = Decrypt_withEngDic()
		start_time = time.time()
		resultHacking = decrypt_withEngDic_Instance.attack_Product(cipherProduct)
		end_time = time.time()
		elapsed_time = end_time - start_time
		printHackingResult(resultHacking,elapsed_time )
		# write file
		file_result = 'result_' + args.testcase 
		writefile("result_hacking_product/"+file_result, "We calculate the key of "+args.testcase+ ":\n" +"Cesar key: "+ str(resultHacking['key_cesar']) +"\nRail fence key: " + str(resultHacking['key_rail_fence']) + "\nElapsed_time: {0}".format(elapsed_time) + "[sec]"+"\nScore:\n" + str(resultHacking['score'])  +"\nPlaintext:\n" + resultHacking['plaintext'] )

	else:
		raise ValueError("Invalid method.")
