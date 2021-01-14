import math
x = 0.45

inputs = []
for o in range(0,20):
  inputs.append(x)
  x = x + 0.45

outputs = [] #outputs is the b

for number in inputs:
  outputs.append(math.sqrt(number) * 2)

#calculating actual exact integral on coordinate plane
out = 0
for number in outputs:
  out = out + (number*(number/4)*.5*.45)
print("Using 1/2bh triangle formula output: " + str(round(out,3)))

#using the 0.5(x) formula
out = 0
for number in inputs:
  out = out + (number*.5*.45)
print("Using 0.5(x) output formula: " + str(round(out,3)))
#end

print("f(x)    b in mm   h in mm  V in mm^2")

converted = []
for number in outputs:
  converted.append(number * 8.8888889)

height = []

for number in converted:
  height.append(.25 * number)

volume = []
for x in range(0,20):
  volume.append(0.5*height[x]*converted[x] *4)

for r in range(0,20):
  print(str(round(inputs[r],3))  + '     ' + str(round(converted[r],3)) + '    ' + str(round(height[r],3)) + '    ' + str(round(volume[r],3)))

totalSum = 0
for number in volume:
  totalSum = totalSum + number
print(totalSum)