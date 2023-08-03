r_rook=int(input())
c_rook=int(input())
r_queen=int(input())
c_queen=int(input())

#Finding the next positions for Rook
positions_rook=[]
for i in range(1,9):
 positions_rook.append((r_rook,i)) #same row
 positions_rook.append((i,c_rook)) #same column
for rc in positions_rook:
 if(rc==(r_rook,c_rook) or rc==(r_queen,c_queen)):
  positions_rook.remove(rc)

#Finding the next positions for Queen
positions_queen=[]
for i in range(1,9):
 positions_queen.append((r_queen,i)) #same row
 positions_queen.append((i,c_queen)) #same column

#For diagonals_Queen
c=c_queen
r=r_queen
while(c!=1 and r!=8):
 positions_queen.append((r+1,c-1))
 r=r+1
 c=c-1
c=c_queen
r=r_queen
while(c!=1 and r!=1):
 positions_queen.append((r-1,c-1))
 r=r-1
 c=c-1
c=c_queen
r=r_queen
iwhile(c!=8 and r!=8):
 positions_queen.append((r+1,c+1))
 r=r+1
 c=c+1
c=c_queen
r=r_queen
while(c!=8 and r!=1):
 positions_queen.append((r-1,c+1))
 r=r-1
 c=c+1

for rc in positions_queen:
 if(rc==(r_rook,c_rook) or rc==(r_queen,c_queen)):
  positions_queen.remove(rc)

final_list=[]
for i in positions_rook:
 if(i in positions_queen):
  final_list.append(i)

x=sorted(final_list)
for i in x:
 print(i)