cont = []
finish = input()
water, gas = 0, 0
width, height = len(finish) - 2, 0
while (curr := input()) != finish:
    height += 1
    for i in curr[1:-1]:
        if i == '~':
            water += 1
        else:
            gas += 1
height, width = width, height
water_height = water // width + (water % width != 0)
print('#' * (width + 2))
for i in range(height):
    if i < height - water_height:
        print('#' + '.' * width + '#')
    else:
        print('#' + '~' * width + '#')
print('#' * (width + 2))
gas_bar, water_bar = 0, 0
if gas > water:
    gas_bar = 20
    water_bar = round(20 * water / gas)
else:
    water_bar = 20
    gas_bar = round(20 * gas / water)
gas_bar *= '.'
water_bar *= '~'
allign = max(len(str(gas)), len(str(water)))
print(f"{gas_bar:<20} {gas:>{allign}}/{gas+water}")
print(f"{water_bar:<20} {water:>{allign}}/{gas+water}")
