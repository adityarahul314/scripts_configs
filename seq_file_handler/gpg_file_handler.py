import gnupg
import os
from pprint import pprint 

rootdir = os.getcwd()
gpg_dir = rootdir + '/gpg_bin/gpg.exe'
gpg = gnupg.GPG(gnupghome='gpg_bin',gpgbinary=gpg_dir)
gpg.encoding = 'utf-8'
#gpg_import_key = gpg.import_keys('ceasback_public.gpg')
with open ('ceasback_public.gpg','r') as key_file:
		key_data = key_file.read()
gpg_import_key = gpg.import_keys(key_data)
#deleting key with fingerprint
#gpg.delete_keys("6CB5240F076CF375A8CA3912700CC4EB15501500")
gpg_public_key_list = gpg.list_keys()
#print key in pprint format
#pprint(gpg_public_key_list)
data_dinput = open('original.png','rb')
encrypted_data = gpg.encrypt_file(data_dinput,'CeasBack',always_trust=True,output='encrypted.png')
print(str(encrypted_data))