import hashlib

# PB_current_hash = "573de6af99199bdc7ae9534891d512afbc2b1473f2f6a5784e0c078d67a60bf9"
PB_current_hash = "51e8e2f87d506a64fc2663bbd0c6a1d679ddd726e81746718eb46b758f0d8879"

str = "Alice sends James 5 ETH amount"

result = hashlib.sha256(str.encode())
CB_previous_hash = result.hexdigest()

print(CB_previous_hash)

if PB_current_hash==CB_previous_hash:
	print("Hash verified")
else:
	print("Hash not verified")
