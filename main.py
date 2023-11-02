line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().upper() # Where do you want to put the treasure?

split_input = [*position]

if split_input[0]=='A':
  if split_input[1]=='1':
    line1[0] = 'X'
  elif split_input[1]=='2':
    line2[0] = 'X'
  elif split_input[1]=='3':
    line3[0] = 'X'  
elif split_input[0]=='B':
  if split_input[1]=='1':
    line1[1] = 'X'
  elif split_input[1]=='2':
    line2[1] = 'X'
  elif split_input[1]=='3':
    line3[1] = 'X'  
elif split_input[0]=='C':
  if split_input[1]=='1':
    line1[2] = 'X'
  elif split_input[1]=='2':
    line2[2] = 'X'
  elif split_input[1]=='3':
    line3[2] = 'X'  
  
print(f"{line1}\n{line2}\n{line3}")