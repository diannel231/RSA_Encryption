import os, random, struct
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode

##################################################
# Loads the RSA key object from the location
# @param keyPath - the path of the key
# @return - the RSA key object with the loaded key
##################################################
def loadKey(keyPath):

	# The RSA key
	key = None

	# Open the key file
	with open(keyPath, 'r') as keyFile:

		# Read the key file
		keyFileContent = keyFile.read()

		# Decode the key
		decodedKey = b64decode(keyFileContent)

		# Load the key
		key = RSA.importKey(decodedKey)

	# Return the key
	return key


##################################################
# Signs the string using an RSA private key
# @param sigKey - the signature key
# @param string - the string
##################################################
def digSig(sigKey, string):

	# Encrypt string with private key
	dataSig = sigKey.sign(string, '')

	# Return the signature
	return dataSig

##########################################################
# Returns the file signature
# @param fileName - the name of the file
# @param privKey - the private key to sign the file with
# @return fileSig - the file signature
##########################################################
def getFileSig(fileName, privKey):

	# Open file and read its contents
	with open(fileName, 'r') as contents:
		data = contents.read()

	# Compute SHA-512 hash of contents
	dataHash = SHA512.new(data).hexdigest()

	# Sign computed hash
	fileSig = digSig(privKey, dataHash)

	# Return file signature
	return fileSig

###########################################################
# Verifies the signature of the file
# @param fileName - the name of the file
# @param pubKey - the public key to use for verification
# @param signature - the signature of the file to verify
##########################################################
def verifyFileSig(fileName, pubKey, signature):

	# Open and read contents of input file
	with open(fileName, 'r') as contents:
		data = contents.read()

	# Compute SHA-512 hash of contents
	dataHash = SHA512.new(data).hexdigest()

	# Verify file
	if pubKey.verify(dataHash, signature) == True:
		return True
	else:
		return False

############################################
# Saves the digital signature to a file
# @param fileName - the name of the file
# @param signature - the signature to save
############################################
def saveSig(fileName, signature):

	# Get first value of signature
	digSig = str(signature[0])

	# Save the value to a file
	with open(fileName, 'w') as file:
		file.write(digSig)


###########################################
# Loads the signature and converts it into
# a tuple
# @param fileName - the file containing the
# signature
# @return - the signature
###########################################
def loadSig(fileName):

	# Get signature from signature file
	with open(fileName, 'r') as file:
		signature = file.read()

	# Convert signature into an integer and then put it into a single elem tuple
	tuple = (int(signature),)

	# Return the signature
	return tuple

#################################################
# Verifies the signature
# @param theHash - the hash
# @param sig - the signature to check against
# @param veriKey - the verification key
# @return - True if the signature matched and
# false otherwise
#################################################
def verifySig(theHash, sig, veriKey):

	# Verify hash
	if veriKey.verify(theHash, sig) == True:
		return True
	else:
		return False

# The main function
def main():

	# Make sure that all the arguments have been provided
	if len(sys.argv) < 5:
		print "USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME>"
		exit(-1)

	# The key file
	keyFileName = sys.argv[1]

	# Signature file name
	sigFileName = sys.argv[2]

	# The input file name
	inputFileName = sys.argv[3]

	# The mode i.e., sign or verify
	mode = sys.argv[4]

	# TODO: Load the key using the loadKey() function provided.
	key = loadKey(keyFileName)

	# We are signing
	if mode == "sign":

		# Get file signature
		fileSig = getFileSig(inputFileName, key)

		# Save signature to the file
		saveSig(sigFileName, fileSig)

		print "Signature saved to file ", sigFileName

	# We are verifying the signature
	elif mode == "verify":

		# Load signature from file
		signature = loadSig(sigFileName)

		# Verify the signature
		if verifyFileSig(inputFileName, key, signature) == True:
			print "Signatures match!"
		else:
			print "Signatures DO NOT MATCH!"

	else:
		print "Invalid mode ", mode

### Call the main function ####
if __name__ == "__main__":
	main()
