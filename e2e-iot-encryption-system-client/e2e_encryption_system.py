import quickstart
import time
import tea

last_line=None
key=None
while(True):

    quickstart.read_data_from_google_sheet()
    with open('encrypted_data.txt', 'r') as file:
        lines = file.readlines()
        last_line = lines[-1].strip().split(',')
        print('\nEncrypted data fetched from cloud: ', last_line)

    decrypted_arr = []
    for item in last_line:
        decrypted_arr.append(tea.decrypt(item))

    with open('decrypted_data.txt','w') as f:
        print('Decrypted data: ', decrypted_arr)
        f.write(",".join(str(item) for item in decrypted_arr))

    time.sleep(10)