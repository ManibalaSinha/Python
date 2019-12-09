#raise statement allows the programmer to force a specified exception to occur
try:
    raise NameError('HiThere') #NameError: HiThere
except NameError:
    print('An exception flew by!')
    raise