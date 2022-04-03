import math
import random
import numpy as np

if __name__ == '__main__':
    distance = 8.0
    bearing = 0
    distance_noise = 0.05
    bearing_noise  = 0.03
    number = 8
    for n in range(number):
        bearing += math.pi / number
        print(f'--------distance: {distance}, distance noise: {distance_noise}, bearing: {bearing}, bearing noise: {bearing_noise}--------')
        data_both = []
        data_dist = []
        data_bear = []
        rdm_data_distance = []
        rdm_data_bearing = []
        for i in range(1000000):
            distance_gauss = random.gauss(0, distance_noise)
            bearing_gauss  = random.gauss(0, bearing_noise)
            distance_with_noise = distance + distance_gauss
            bearing_with_noise = bearing + bearing_gauss
            data_dist.append(distance_with_noise * math.cos(bearing))
            data_bear.append(distance * math.cos(bearing_with_noise))
            data_both.append(distance_with_noise * math.cos(bearing_with_noise))
            rdm_data_distance.append(distance_with_noise)
            rdm_data_bearing.append(bearing_with_noise)
        print(f'experiment: distance noise: {np.std(rdm_data_distance)}, bearing noise: {np.std(rdm_data_bearing)}')
        exp_dist_std = np.std(data_dist)
        exp_bear_std = np.std(data_bear)
        exp_both_std = np.std(data_both)
        exp_both_sqrt = math.sqrt(exp_dist_std ** 2 + exp_bear_std ** 2)
        distance_with_noise = distance + distance_gauss
        bearing_with_noise = bearing + bearing_gauss
        cal_dist_std = distance_noise * math.cos(bearing_with_noise)
        cal_bear_std = distance_with_noise * bearing_noise * (math.sin(bearing))
        cal_both_std = math.sqrt(cal_dist_std**2 + cal_bear_std**2)
        diff_bear_std = cal_bear_std - exp_bear_std
        diff_dist_std = cal_dist_std - exp_dist_std
        diff_both_std = cal_both_std - exp_both_std

        print(f'exp_dist_std: {exp_dist_std}, cal_dist_std: {cal_dist_std}, diff: {cal_dist_std - exp_dist_std}')
        print(f'exp_bear_std: {exp_bear_std}, cal_bear_std: {cal_bear_std}, diff: {cal_bear_std - exp_bear_std}')
        print(f'exp_both_sqrt: {exp_both_sqrt}, diff: {exp_both_sqrt - exp_both_std}')
        print(f'exp_both_std: {exp_both_std}, cal_both_std: {cal_both_std}, diff: {cal_both_std - exp_both_std}')
        print('\n')
