import os
import argparse
from attack_with_englishdic import Decrypt_withEngDic
from rail_fence import encryptRailFence, decryptRailFence
import time

def readfile(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data

def writefile(file_name,content):
	with open(file_name, "w") as myfile:
		myfile.write(content)


if __name__ == "__main__":

# chi tieng anh va khong co ki tu khac
#  ke ca dau xuong dong

	parser = argparse.ArgumentParser()
 
	parser.add_argument("-t", "--testcase", help = "enter testcase file")
	
	args = parser.parse_args()
	if args.testcase == None:
		print("Enter testcase file")
	else:
		# encrypt rail fence
		data = readfile("testcase/"+args.testcase)
		print("Enter rail-fence key from 2 to",(len(data) - 1))
		RailFenceKey = int(input())
		cipher = encryptRailFence(data,RailFenceKey)
		file_name_dest = "cipher_of_" + args.testcase
		writefile("cipher_rail_fence/" + file_name_dest, cipher)

		# hacking cipher
		cipher = readfile("cipher_rail_fence/" +file_name_dest)
		decrypt_withEngDic_Instance = Decrypt_withEngDic()

		print('Decode with Rail_fence Cipher with English Dictionary:')
		start_time = time.time()
		resultHacking = decrypt_withEngDic_Instance.decrypt_Rail_fence(cipher)
		end_time = time.time()
		print('We calculate the key:')
		print(resultHacking['key'])
		elapsed_time = end_time - start_time
		print ("Elapsed_time: {0}".format(elapsed_time) + "[sec]")

		print('Plaintext:')
		print(resultHacking['plaintext'])

		# write file
		file_result = 'result_' + args.testcase 
		writefile("result_hacking_rail_fence/"+file_result, "We calculate the key of "+args.testcase+ ":\n" + str(resultHacking['key']) + "\nElapsed_time: {0}".format(elapsed_time) + "[sec]" +"\nPlaintext:\n" + resultHacking['plaintext'] )
