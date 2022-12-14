sequenceName = str(input("Sequence Name: "))
sequenceLength = int(input("Number of objects you are renaming: "))

def SeqRenamer(txt, num):

    count = txt.count("#")

    poundFind = txt.find("#" * count)
    if poundFind < 0:
        print("Enter the sequence with all the pound signs together")
        return

    for i in range(1, num+1):
        x = txt.replace("#" * count, str(i).zfill(count))
        print(x)

SeqRenamer(sequenceName, sequenceLength)
