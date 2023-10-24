
with open("sample.ini") as file:
        log = file.read()

def variables(log):
     for line in log.split('\n'):
        print(line)
        
        lineHalf = line.split("=")
        print(lineHalf[0])
       
    
variables(log)