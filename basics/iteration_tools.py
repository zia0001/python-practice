with open('basics\\loops_problems.py','r') as f:
  content =f.read()
  print(content)



  #------------
   mylist = [1,2,3,4,5]
>>> I = iter(mylist)
>>> I
<list_iterator object at 0x0000024636D693F0>
>>> I.__next__()
1   
>>> I.__next__()
2   
>>> I.__next__()
3 I.__next__()
4   
>>> I.__next__()
5   