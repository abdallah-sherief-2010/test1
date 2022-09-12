deg = input("Degree = ")

full = input("Full Mark = ")

###########################

def percentage (d,f):
    degree = int(d)
    fullMark = int(f)

    if degree == 0 and fullMark == 0:
        print("Write numbers in Degree and Full Mark to calculate precentage")

    elif fullMark == 0:
        print("Full Mark Must be greate than zero")

    elif degree > fullMark:
        print("Degreen can't be greater then Full Mark")

    else:
        per = ( degree / fullMark ) * 100
        print(f"Stutent Percntage = {per} %")
 ##############################
                    
percentage(deg, full)
