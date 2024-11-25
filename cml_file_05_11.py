my_file = open("D:/jst.txt", "a")
my_file.write("\n7th Batch")
my_file.close()

my_file = open("D:/jst.txt", "r")
##for i in range (1,6):
  #  print(my_file.readline())
print(my_file.read())
my_file.close()