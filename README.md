# experiment-polar-2-cartesian-gaussian-convert


This project is trying to find the formula of converting polar system gaussian noise to cartersian system by experimenting. It only calcuates the x axis.


The conclusion is 
1. This experiment does work for simulating noise. 
   For this exmaple,
    --------distance: 10.0, distance noise: 0.05, bearing: 0, bearing noise: 0.03--------
    experiment: distance noise: 0.04996792184157838, bearing noise: 0.02994630552105194
    exp_dist_std: 0.04996792184157838, cal_dist_std: 0.05, diff: 3.207815842162093e-05
    exp_bear_std: 0.006323185582140158, cal_bear_std: 0.006363961030678928, diff: 4.0775448538769334e-05
    exp_both_sqrt: 0.05036641628180698, diff: 6.223794290907692e-05
    exp_both_std: 0.05034113496010209, cal_both_std: 0.05040337290301117, diff: 6.223794290907692e-05
   
   The real distance noise is 0.05, then exmperiment result is 0.04996792184157838. 
   The bearing result is similar, the real noise is 0.03, and the experimant result is 0.02994630552105194. 
   The experiment result is close enough to the real value.
   
2. exp_both_std ≈ sqrt(exp_dist_std ** 2 + exp_bear_std ** 2)
   For this exmaple,
    --------distance: 10.0, distance noise: 0.05, bearing: 0, bearing noise: 0.03--------
    experiment: distance noise: 0.04996792184157838, bearing noise: 0.02994630552105194
    exp_dist_std: 0.04996792184157838, cal_dist_std: 0.05, diff: 3.207815842162093e-05
    exp_bear_std: 0.006323185582140158, cal_bear_std: 0.006363961030678928, diff: 4.0775448538769334e-05
    exp_both_sqrt: 0.05036641628180698, diff: 6.223794290907692e-05
    exp_both_std: 0.05034113496010209, cal_both_std: 0.05040337290301117, diff: 6.223794290907692e-05
    
    exp_dist_std: 0.04996792184157838 (the exmperiment result of the distance with noise, the bearing has no noise.)
    exp_bear_std: 0.006323185582140158 (the exmperiment result of the bearing with noise, the distance has no noise.)
    exp_both_std: 0.05036641628180698 (the exmperiment result of both distance and bearing have noise.)
    Definitely, 
        exp_both_std != exp_dist_std + exp_bear_std, 
    Actually, exp_both_std is close to exp_both_sqrt.
       exp_both_sqrt = sqrt(exp_dist_std ** 2 + exp_bear_std ** 2)
    
3. The result of formulas are close to the experiment.
   exp_dist_std ≈ cal_dist_std
   exp_bear_std ≈ cal_bear_std
   exp_both_std ≈ cal_both_std
   
   cal_dist_std = distance_noise * math.cos(bearing)
   cal_bear_std = distance * math.sqrt((math.sin(bearing) ** 2)  * (bearing_noise ** 2) + ((math.cos(bearing) ** 2) * (bearing_noise ** 4) / 2.0))
   cal_both_std = math.sqrt(cal_dist_std**2 + cal_bear_std**2)

   
    
    
