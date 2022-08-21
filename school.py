school = {"math": [], "science": [], "goghrafia": [], "computer": [], "art": []}
print('when you want end print "-1"!')
while True:
    grade = input("please insert your grade in math: ")
    if grade == "-1":
        print("\/\/" * 20)
        break
    if int(grade) > 20:
        print("you number is false")
    elif int(grade) < 0:
        print("you number is false")
    else:
        grade = float(grade)
        school["math"].append(grade)
while True:
    grade = input("please insert your grade in science: ")
    if grade == "-1":
        print("\/\/" * 20)
        break
    if int(grade) > 20:
        print("you number is false")
    elif int(grade) < 0:
        print("you number is false")
    grade = float(grade)
    school["science"].append(grade)
while True:
    grade = input("please insert your grade in goghrafia: ")
    if grade == "-1":
        print("\/\/" * 20)
        break
    if int(grade) > 20:
        print("you number is false")
    elif int(grade) < 0:
        print("you number is false")
    grade = float(grade)
    school["goghrafia"].append(grade)
while True:
    grade = input("please insert your grade in computer: ")
    if grade == "-1":
        print("\/\/" * 20)
        break
    if int(grade) > 20:
        print("you number is false")
    elif int(grade) < 0:
        print("you number is false")
    grade = float(grade)
    school["computer"].append(grade)
while True:
    grade = input("please insert your grade in art: ")
    if grade == "-1":
        print("\/\/" * 20)
        break
    if int(grade) > 20:
        print("you number is false")
    elif int(grade) < 0:
        print("you number is false")
    grade = float(grade)
    school["art"].append(grade)
while True:
    work = input("1.grades \n2.average \n3.bigger \n4.smaller \n5.find the numbers \n6.add \n")
    if work == "1":
        work2 = input("1.math \n2.science \n3.goghrafia \n4.computer \n5.art \n")
        if work2 == "1":
            print(school["math"])
        elif work2 == "2":
            print(school["science"])
        elif work2 == "3":
            print(school["goghrafia"])
        elif work2 == "4":
            print(school["computer"])
        elif work2 == "5":
            print(school["art"])
        else:
            print("some think is wrong")
    elif work == "2":
        work3 = input("1.math \n2.science \n3.goghrafia \n4.computer \n5.art \n")
        if work3 == "1":
            print(sum(school["math"]) / len(school["math"]))
        elif work3 == "2":
            print(sum(school["science"]) / len(school["science"]))
        elif work3 == "3":
            print(sum(school["goghrafia"]) / len(school["goghrafia"]))
        elif work3 == "4":
            print(sum(school["computer"]) / len(school["computer"]))
        elif work3 == "5":
            print(sum(school["art"]) / len(school["art"]))
    elif work == "3":
        work3 = input("1.math \n2.science \n3.goghrafia \n4.computer \n5.art \n")
        if work3 == "1":
            print(max(school["math"]))
        elif work3 == "2":
            print(max(school["science"]))
        elif work3 == "3":
            print(max(school["goghrafia"]))
        elif work3 == "4":
            print(max(school["computer"]))
        elif work3 == "5":
            print(max(school["art"]))
    elif work == "4":
        work3 = input("1.math \n2.science \n3.goghrafia \n4.computer \n5.art \n")
        if work3 == "1":
            print(min(school["math"]))
        elif work3 == "2":
            print(min(school["science"]))
        elif work3 == "3":
            print(min(school["goghrafia"]))
        elif work3 == "4":
            print(min(school["computer"]))
        elif work3 == "5":
            print(min(school["art"]))
    elif work == "5":
        work3 = input("1.math \n2.science \n3.goghrafia \n4.computer \n5.art \n")
        number = int(input("please insert the number: "))
        math1 = []
        if work3 == "1":
            for i in range(len(school["math"])):
                x = school["math"][i]
                if x > number:
                    math1.append(x)
            print(math1)
        science = []
        if work3 == "2":
            for i in range(len(school["science"])):
                x = school["science"][i]
                if x > number:
                    science.append(x)
            print(science)
        goghrafia = []
        if work3 == "3":
            for i in range(len(school["goghrafia"])):
                x = school["goghrafia"][i]
                if x > number:
                    goghrafia.append(x)
            print(goghrafia)
        computer = []
        if work3 == "4":
            for i in range(len(school["computer"])):
                x = school["computer"][i]
                if x > number:
                    computer.append(x)
            print(computer)
        art = []
        if work3 == "5":
            for i in range(len(school["art"])):
                x = school["art"][i]
                if x > number:
                    art.append(x)
            print(art)
    elif work == "6":
        while True:
            work3 = input("1.math \n2.science \n3.goghrafia \n4.computer \n5.art \n")
            if work3 == "1":
                while True:
                    grade = input("please insert your grade in math: ")
                    if int(grade) > 20:
                        print("you number is false")
                    elif int(grade) < 0:
                        print("you number is false")
                    else:
                        grade = float(grade)
                        school["math"].append(grade)
                        break
            if work3 == "2":
                while True:
                    grade = input("please insert your grade in science: ")
                    if int(grade) > 20:
                        print("you number is false")
                    elif int(grade) < 0:
                        print("you number is false")
                    else:
                        grade = float(grade)
                        school["science"].append(grade)
                        break
            if work3 == "3":
                while True:
                    grade = input("please insert your grade in goghrafia: ")
                    if int(grade) > 20:
                        print("you number is false")
                    elif int(grade) < 0:
                        print("you number is false")
                    else:
                        grade = float(grade)
                        school["goghrafia"].append(grade)
                        break
            if work3 == "4":
                while True:
                    grade = input("please insert your grade in computer: ")
                    if int(grade) > 20:
                        print("you number is false")
                    elif int(grade) < 0:
                        print("you number is false")
                    else:
                        grade = float(grade)
                        school["computer"].append(grade)
                        break
            if work3 == "5":
                while True:
                    grade = input("please insert your grade in art: ")
                    if int(grade) > 20:
                        print("you number is false")
                    elif int(grade) < 0:
                        print("you number is false")
                    else:
                        grade = float(grade)
                        school["art"].append(grade)
                        break
            run2 = input("do you want to add another number?(yes or no): ")
            if run2 == "no":
                break
    run = input("do you want do some think??(yes or no): ")
    if run == "no":
        break
        print("bay(;")
