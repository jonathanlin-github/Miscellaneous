import math
x = 0.45

inputs = []
for o in range(0,20):
  inputs.append(x)
  x = x + .45

outputs = []

for number in inputs:
  outputs.append(math.sqrt(number) * 2)

converted = []
for number in outputs:
  converted.append(round(number,3) * 8.8888889)

height = []

for number in converted:
  height.append(.25 * number)

for r in range(0,20):
  print(str(round(inputs[r],3)) + '   ' + str(round(outputs[r],3)) + '     ' + str(round(converted[r],3)) + '    ' + str(round(height[r],3)))

