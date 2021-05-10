# RSA
## Name and Email:

  Dianne Lopez: diannel@csu.fullerton.edu

## Programming language:

  python

## How to execute:

  To execute, type the following command:

    python signer.py <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>

  Each parameter is defined as follows:

    KEY FILE NAME: The name of the file containing private key (if signing) or public key (when
    verifying the digital signature).

    SIGNATURE FILE NAME: The file to which to save the digital signature (if signing) or from 
    which to load the digital signature (when verifying).
    
    INPUT FILE NAME: The file for which to generate or verify the digital signature.
    
    MODE: Can be one of the following:
      
      - sign
      
      - verify

  An example command would be:

    bash$ python signer.py privKey.pem music.sig music.mp3 sign

### The extra credit was not implemented.

### There are no additional notes.
