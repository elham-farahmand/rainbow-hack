import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name, mode='r', newline='') as fin:
        reader = csv.reader(fin, delimiter=',')
        with open(output_file_name, mode='w', newline="") as fout:
            writer = csv.writer(fout, delimiter=',')
            dic = dict()
            result = dict()
            for i in range(1000,10000):
                pass_hash = hashlib.sha256(str(i).encode()).hexdigest()
                dic[pass_hash] = i
            for row in reader:
                result[row[0]] = dic.get(row[1])
            for item in result.items():
                writer.writerow([item[0], item[1]])
        
    fin.close()
    fout.close()


            

            




