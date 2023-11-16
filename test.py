
n = 1

def is_numeric(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if (is_numeric(n)):
    print('é número')
       
else:
    print('é letra')