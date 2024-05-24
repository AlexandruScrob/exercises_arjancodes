def solution(U: int, weight: list[int]):
    total_cars = len(weight)
    num_cars = 0
    skip_next_cars = 0
    for index, car in enumerate(weight):

        if skip_next_cars > 0:
            skip_next_cars -= 1
            continue

        if index < total_cars - 1:
            if all(car + car_2 > U for car_2 in weight[index + 1 :]):
                num_cars += 1
                continue
            if car + weight[index + 1] > U:
                for car_2 in weight[index + 1 :]:
                    if car + car_2 <= U:
                        break
                    else:
                        skip_next_cars += 1
                        num_cars += 1

    return num_cars


weight1 = [5, 3, 8, 1, 8, 7, 7, 6]
u1 = 9

weight2 = [7, 6, 5, 2, 7, 4, 5, 4]
u2 = 7

weight3 = [3, 4, 3, 1]
u3 = 7


if __name__ == "__main__":
    print(solution(u3, weight3))
