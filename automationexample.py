'''
<p>John is a school teacher, he has to check some answer sheets but his
schedule for today is quite busy also he has plans for seeing El Cl&aacute
;sico(between Madrid vs Barca) so can you help him by <i>writing a computer
program which can do this mundane task of giving marks.</i></p> <p><b>Input:
</b><br>14 lines will be given as input to console(stdin) It will contain Name
of Student, 10 Questions with the answer given by Student and placeholder for
Score.</p> <b>Important note:</b> <p> 1) while dealing with float<br>
Name: Aarav<br> 118 / 18 != 6.56 False<br> LHS = 6.55555555556 first round LHS
to two decimal place<br> now LHS = 6.56 since 6.56 == 6.56 is True therefore
118 / 18 != 6.56 False is a correct answer so <b>award +1 point for this answer.
</b></p> <p>2) treat '=' as '==' it means your program should do equality check
when it encounters equations like this 15*8 = 75 False</p> <p>3) Each question
have this pattern<br> <i>Operand_A Arithmetic_Operator Operand_B Comparision_Operator Operand_C Student_Ans
</i><br> 10 + 75 < 95 True </p> <i>Arithmetic_Operator = ['*', '/', '-', '+']<br>
Comparision_Operator = ['>', '>=', '<', '<=', '!=', '=']</i><br> <p><b>Output:</b>
Just Print the Score obtained by Student </p> <p><strong>Sample Input&nbsp;&nbsp;
*points(will not be present in input)</strong></p> <p>Name: Aadish</p> <p>120 * 68 &gt; 8162 True&nbsp;
0<br />115 / 70 = 5.64 False 1<br />93 * 55 &lt;= 5111 True 0<br />140 / 24 = 3.83 False 1<br />103 + 44 != 147 False 1<br />107 + 84 != 192 True 1<br />116 / 37 &gt;= -0.86 True 1<br />168 - 5 &gt;= 166 False 1<br />95 - 62 = 36 False 1<br />131 / 45 = -0.09 False 1</p> <p>Score:</p> <p><strong>Sample Output</strong></p> <p>&nbsp;8</p>
'''
def arthoperator(op1,arthop,op2):
    if arthop == '*':
        return float(op1)*float(op2)
    if arthop == '/':
        return float(op1)/float(op2)
    if arthop == '-':
        return float(op1)-float(op2)
    if arthop == '+':
        return float(op1)+float(op2)

def compare(op1,comp,op2):
    if comp == ">=":
        return float(format(float(op1),'.2f')) >= float(format(float(op2),'.2f'))
    if comp == ">":
        return float(format(float(op1),'.2f')) > float(format(float(op2),'.2f')) 
    if comp == "<=":
        return float(format(float(op1),'.2f')) <= float(format(float(op2),'.2f'))
    if comp == "<":
        return float(format(float(op1),'.2f'))<float(format(float(op2),'.2f'))
    if comp == "!=":
        return float(format(float(op1),'.2f'))!=float(format(float(op2),'.2f'))
    if comp == "=":
        return float(format(float(op1),'.2f'))==float(format(float(op2),'.2f'))
def answer(ans):
    if ans == "True":
        return True
    if ans == "False":
        return False
name = input()
space = input()
l = [None]*10
point = 0
for i in range(0, 10):
  l[i]= input()
for i in range(0,10):
  l[i] = [x for x in l[i].split(" ")]
for i in range(0,10):
  op1 = l[i][0]
  arthop = l[i][1]
  op2 = l[i][2]
  comp = l[i][3]
  op3 = l[i][4]
  ans = l[i][5]
  subans = arthoperator(op1,arthop,op2)
  print(compare(subans,comp,op3))
  if compare(subans,comp,op3) == answer(ans):
      point = point +1
print(point) 

