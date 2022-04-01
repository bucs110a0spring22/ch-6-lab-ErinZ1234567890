import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        #print(n)
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    #print(n)                  # the last print is 1
    return count

def drawGraph(uB):
  """
  Draws Graph of seq3np1 values and displays max value so far in top left. window grows along with graph.
  """
  
  maxSoFar = 0 #keeps track of max value of seq3np1 so far
  graphing = turtle.Turtle() #draws the graph of seq3np1 vals
  graphing.goto(0, 0)
  writer = turtle.Turtle() #writes max val of seq3np1 within bounds
  window = turtle.Screen()
  window.setworldcoordinates(0,0,10,10)
  graphing.down()
  writer.up()
  
  for i in range(1, uB+1):
    result = seq3np1(i)
    print("result {}".format(result))
    
    if (result > maxSoFar):
      maxSoFar = result
      writer.clear()
      writer.goto(0,maxSoFar)
      writer.write("Maximum so far: {}, {} ".format(i, result))
      
    window.setworldcoordinates(0, 0, i+10, maxSoFar+10)
    graphing.goto(i, result)
  print("end)")
  #window.exitonclick()

def main():
  window = turtle.Screen()
  print("test")
  upBound = (int)(input("Please input an upper bound: ")) 
  
  if(upBound > 0):
    drawGraph(upBound)
    for start in range(1, upBound+1):
      seq3np1(start)
      print("start: {}".format(start))
      print("seq3np1: {}".format(seq3np1(start)))
  else:
    print("please restart the program and input a positive number for the upper bound.")
    
  window.exitonclick()
main()
