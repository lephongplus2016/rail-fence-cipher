import os
import argparse
from attack_with_englishdic import Decrypt_withEngDic
from rail_fence import encryptRailFence, decryptRailFence

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
	# data = readfile("plaintext.txt")
	# cipher = encryptRailFence(data,49)
	# writefile("cipher.txt", cipher)
	# data = readfile("cipher.txt")
	# decode = decryptRailFence(data, 49)
	# writefile("decode.txt",decode)

	# attack by english dictionary


	# decrypt_withEngDic_Instance.get_english_score('PASSENGERS ARRIVED AT YEN NGHIA STATION')

	parser = argparse.ArgumentParser()
 
	parser.add_argument("-t", "--testcase", help = "enter testcase file")
	
	args = parser.parse_args()
	if args.testcase == None:
		print("Enter testcase file")
	else:
		data = readfile(args.testcase)
		print("Enter rail-fence key from 2 to",(len(data) - 1))
		RailFenceKey = int(input())
		cipher = encryptRailFence(data,RailFenceKey)
		file_name_dest = "cipher_of_" + args.testcase
		writefile(file_name_dest, cipher)

		# hacking cipher
		cipher = readfile(file_name_dest)
		decrypt_withEngDic_Instance = Decrypt_withEngDic()

		print('Decode with Rail_fence Cipher with English Dictionary:')
		resultHacking = decrypt_withEngDic_Instance.decrypt_Rail_fence(cipher)
		print('We calculate the key:')
		print(resultHacking['key'])
		print('Plaintext:')
		print(resultHacking['plaintext'])

		# write file
		file_result = 'result_' + args.testcase 
		writefile(file_result, "We calculate the key of "+args.testcase+ ":\n" + str(resultHacking['key']) + "\nPlaintext:\n" + resultHacking['plaintext'] )
