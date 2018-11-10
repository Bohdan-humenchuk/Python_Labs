def logg(commar):
    line=""
    for el in commar:
        line+=str(el)+" "
    line+="\n"
    with open("logg.txt", 'a') as log:    
        log.write(str(line))
