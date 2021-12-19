import math

liquid, width, height = 0, len(input()) - 2, 0
while (a := input()):
    if (a[1] == "#"):
        break
    if (a[1] == "~"):
        liquid += 1
    height += 1

new_liquid = math.ceil(width * liquid / height)

print("#" * (height + 2))
for i in range(width):
    print("#" + ("." if i < (width - new_liquid) else "~") * (height) + "#")
print("#" * (height + 2))

new_liquid = int(width * liquid / height)

max_vol = max((height - liquid) * width, liquid * width)
gas = round((height - liquid) * width / max_vol * 20)
liq = round(liquid * width / max_vol * 20)

print("{:<20} {:{base}}/{}".format("." * gas, (height - liquid) * width, height * width, base=len(str(max_vol))))
print("{:<20} {:{base}}/{}".format("~" * liq, liquid * width, height * width, base=len(str(max_vol))))
