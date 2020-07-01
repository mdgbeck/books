import time, sys
indent = 0 # how many spaces to indent.
indent_increasing = True # whether the indentation is increasing or not.

try:
    while True: # the main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.01) # pause for 1/10 of a second
        if indent_increasing:
            # increase the number of spaces
            indent += 1
            if indent == 50:
                # Change directions
                indent_increasing = False
        else:
            # decrease the number of spaces
            indent = indent -1
            if indent == 0:
                # Change directions
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
            
