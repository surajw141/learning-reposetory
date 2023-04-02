#lab on insuline case study
su = "ORIGIN 1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed\n    61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn\n//"

print("Data received from case study = ",su)
# remove newline characters and leading/trailing whitespaces
su = su.replace("\n", "")

# remove non-alphabetic characters and digits
su = su.replace(" ", "")
su = su.replace("ORIGIN", "")
su = su.replace("1", "")
su = su.replace("61", "")
su = su.replace("6", "")
su = su.replace("//", "")
print("Full range of insulin = ",su)

print("Total number of characters in insulin: ", len(su))
lsinsulin= su[0:24]
print("1)lsinsulin range is: ",lsinsulin)
print("Number of characters in lsinsulin: ", len(lsinsulin))

binsulin= su[24:54]
print("2)binsulin range is: ",binsulin)
print("Number of characters in binsulin: ", len(binsulin))

cinsulin= su[54:89]
print("3)cinsulin range is: ",cinsulin)
print("Number of characters in cinsulin: ", len(cinsulin))


ainsulin= su[89:110]
print("4)ainsulin range is: ",ainsulin)
print("Number of characters in ainsulin: ", len(ainsulin))