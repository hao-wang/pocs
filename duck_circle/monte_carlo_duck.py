import random 

def is_on_same_side(idx, coordinates):
    origin_x, origin_y = coordinates[idx]
    # line determined by two points: (x0=0.5, y0=0.5), (x1=ori_x, y1=ori_y) 
    k = (0.5-origin_y)/(0.5-origin_x+0.00001)
    b = (0.5*origin_y - origin_x*0.5)/(0.5-origin_x+0.00001)

    cnt = 0
    total_above = 0
    for i, coord in enumerate(coordinates):
        if i != idx:
            cnt += 1
            if coord[1] >= k*coord[0]+b:
                total_above += 1
            else:
                total_above -= 1

        if abs(total_above) < cnt:
            return 0

    return 1


def is_in_same_half(coordinates):
    for idx, coord in enumerate(coordinates):
        if is_on_same_side(idx, coordinates):
            return 1

    return 0

def is_in_same_half2(coordinates):
    pass


def generate_duck(number, n_trial=100):
    same = 0
    for i in range(n_trial):
        coordinates = []
        while (len(coordinates) < number):
            x = random.randint(0, 1000)*1./1000
            y = random.randint(0, 1000)*1./1000
            if (x-.5)*(x-.5) + (y-.5)*(y-.5) <= 1:
                coordinates.append((x, y))

        same += is_in_same_half(coordinates)

    print("{0} ducks on the same side {2} times out of {1}, ratio = {3:.2f}".format(
        number, n_trial, same, same*1./n_trial))


if __name__ == "__main__":
    for n_duck in [3, 4, 5, 6]:
        for n_trial in [5000, 10000, 20000]:
            generate_duck(n_duck, n_trial)

        print("-"*30)

