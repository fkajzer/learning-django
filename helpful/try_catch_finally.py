try:
    f = open('simple.txt', 'w')
    f.write("Test write to file")
except:
    print ("ERROR, COULD NOT FIND FILE")
finally:
    print("I ALWAYS WORK NO MATTER WHAT")
    f.close()
