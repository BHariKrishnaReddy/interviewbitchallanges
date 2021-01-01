#You are given an input file called input.

#    The first line of the file contains a positive integer **T**, denoting number of test cases
#    Each of the next **T** lines contains a positive integer **N**

#For each N, you are supposed to echo the Nth fibonacci number on a new line.

#The first fibonacci number F1 = 1
#The first fibonacci number F2 = 1
#The nth fibonacci number Fn = Fn-1 + Fn-2 (n > 2)



eof=1 #denotes if end of file has been reached or not, 0 denotes end of file
while [ $eof -eq 1 ]
do
eof=$((eof-1)) #we will be reading the whole file inside the loop
read num_test_cases #first line of input denotes test cases
while [ $num_test_cases -gt 0 ] #loop while num_test_cases is greater than 0
do
read n #read the number N
a=1
b=1
c=$((a + b))
if [ $n -eq 1 ] #if n is 1, echo 1
then
echo 1
elif [ $n -eq 2 ] #if n is 2, echo 1
then
echo 1
elif [ $n -eq 3 ] #if n is 3, echo 2 (c is 2)
then
echo $c
else
n=$((n - 3)) #as n = 1, 2 and 3 is handled, we don’t need to loop over them
while [ $n -gt 0 ]
do
a=$((b))
b=$((c))
c=$((a + b))
n=$((n - 1))
done
echo $c #final answer is c
fi #end of id statements
num_test_cases=$((num_test_cases - 1)) #decrement number of test cases
done
done < input #read from file “input”
