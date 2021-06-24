purity = float(input())

#your code goes here
def purity_checker(_purity: float) -> bool:
    if (_purity >= 91.7):
        print('Accepted')
        return True
    # else
    return False

if __name__ != 'main':
    purity_checker(purity)
