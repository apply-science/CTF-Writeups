import hashlib

username_trial = b"MORTON"
key_static_part1 = "picoCTF{1n_7h3_|<3y_of_"
key_static_part2 = "}"

key = ""
key = key + hashlib.sha256(username_trial).hexdigest()[1]
key = key + hashlib.sha256(username_trial).hexdigest()[2]
key = key + hashlib.sha256(username_trial).hexdigest()[3]
key = key + hashlib.sha256(username_trial).hexdigest()[4]
key = key + hashlib.sha256(username_trial).hexdigest()[5]
key = key + hashlib.sha256(username_trial).hexdigest()[6]
key = key + hashlib.sha256(username_trial).hexdigest()[7]
key = key + hashlib.sha256(username_trial).hexdigest()[8]

correct_key = key_static_part1 + key + key_static_part2

print(correct_key)
print(len(correct_key))
