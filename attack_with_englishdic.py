import re 
import random
from h import TanCongCesar
from rail_fence import encryptRailFence, decryptRailFence

LIMITS = 50

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

english_words = load_words()

class Decrypt_withEngDic:
    def isEnglishWord(self, word):
        return word.lower() in english_words
    
    def get_english_score(self, words):
        # remove special charaters
        words_with_nospecial = re.sub('[^a-zA-Z0-9\n]', ' ', words)
        # print(words_with_nospecial)
        score = 0
        for word in words_with_nospecial.split():
            score += self.isEnglishWord(word)

        return score
    

    def attack_Rail_fence(self, ciphertext):
        keyRail_fence_max =  len(ciphertext) - 1
        candidates = []
        for key_candidate in range(2, keyRail_fence_max):
            plaintext_candidate = decryptRailFence(ciphertext, key_candidate)
            candidate_score = self.get_english_score(plaintext_candidate)
            result = {
                'key': key_candidate,
                'score': candidate_score,
                'plaintext': plaintext_candidate
            }

            candidates.append(result) 

        candidates.sort(key=lambda c: c['score'], reverse=True)
        # for x in candidates:
        #     print(x)
        return candidates[0]

    def attack_Product(self, ciphertext):
        keyRail_fence_max =  len(ciphertext) - 1
        candidates = []

        for key_rail_fence_candidate in range(2, keyRail_fence_max):
            decrypt_rail_fence_cipher = decryptRailFence(ciphertext, key_rail_fence_candidate)
            for key_cesar_candidate in range(1,25):
                plaintext_candidate = TanCongCesar(decrypt_rail_fence_cipher, key_cesar_candidate)
                candidate_score = self.get_english_score(plaintext_candidate)
                result = {
                    'key_cesar': key_cesar_candidate,
                    'key_rail_fence': key_rail_fence_candidate,
                    'score': candidate_score,
                    'plaintext': plaintext_candidate
                }

                candidates.append(result) 

        candidates.sort(key=lambda c: c['score'], reverse=True)
        # for x in candidates:
        #     print(x)
        return candidates[0]
