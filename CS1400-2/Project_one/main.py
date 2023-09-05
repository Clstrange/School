def main():
    reaver_count = int(input("How many Reavers: "))
    if reaver_count < 3:
        print("Not enough crew")

    unit_count = int(input("How many units: "))
    if unit_count < reaver_count * 3:
        print("Not enough units")

    crew = reaver_count - 2 #removing yondu and peter from crew
    unit_count -= (crew * 3) #Black Lotus

    yondu = int(unit_count * 0.13)
    unit_count -= yondu

    peter = int(unit_count * 0.11)
    unit_count -= peter

    crew = unit_count // reaver_count
    unit_count -= crew * reaver_count

    yondu += crew
    peter += crew

    rbf_fund = unit_count
    print("Yondu's share: " + str(yondu))
    print("Peter's share: " + str(peter))
    print("Crew: " + str(crew))
    print("RBF: " + str(rbf_fund))

if __name__ == "__main__":
    main()