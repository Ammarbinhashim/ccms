from os import read


def appenduser(filename,elelist):
    from csv import writer
    with open(filename,"a+",newline="") as writeobj:
        csv_writer = writer(writeobj)
        csv_writer.writerow(elelist)
