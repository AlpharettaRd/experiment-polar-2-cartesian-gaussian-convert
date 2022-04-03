# experiment-polar-2-cartesian-gaussian-convert


This project is trying to find the formula of converting polar system gaussian noise to cartersian system by experimenting. It only calcuates the x axis.

--------distance: 8.0, distance noise: 0.05, bearing: 0.39269908169872414, bearing noise: 0.03--------
experiment: distance noise: 0.049951161907419696, bearing noise: 0.02995007185116088
exp_dist_std: 0.04614885611142251, cal_dist_std: 0.04614615483095946, diff: -2.7012804630494047e-06
exp_bear_std: 0.09176824312867421, cal_bear_std: 0.09231160672103753, diff: 0.0005433635923633162
exp_both_sqrt: 0.10271868071249864, diff: -6.006899042829139e-06
exp_both_std: 0.10272468761154147, cal_both_std: 0.10320319927745643, diff: 0.00047851166591496297


--------distance: 8.0, distance noise: 0.05, bearing: 0.7853981633974483, bearing noise: 0.03--------
experiment: distance noise: 0.05000441542273804, bearing noise: 0.03000330730258628
exp_dist_std: 0.035358461234687236, cal_dist_std: 0.036702046133569734, diff: 0.001343584898882498
exp_bear_std: 0.16968490676548864, cal_bear_std: 0.16986691692391873, diff: 0.00018201015843008483
exp_both_sqrt: 0.17332970998907676, diff: -1.140693255549663e-05
exp_both_std: 0.17334111692163226, cal_both_std: 0.17378667859081773, diff: 0.000445561669185468


--------distance: 8.0, distance noise: 0.05, bearing: 1.1780972450961724, bearing noise: 0.03--------
experiment: distance noise: 0.05006622953725339, bearing noise: 0.029983260979143982
exp_dist_std: 0.019159516564894577, cal_dist_std: 0.01783916603066728, diff: -0.0013203505342272957
exp_bear_std: 0.22151606631213713, cal_bear_std: 0.22220823528315412, diff: 0.000692168971016982
exp_both_sqrt: 0.22234310133081173, diff: -2.8008473155205493e-06
exp_both_std: 0.22234590217812725, cal_both_std: 0.22292316091497377, diff: 0.0005772587368465254


--------distance: 8.0, distance noise: 0.05, bearing: 1.5707963267948966, bearing noise: 0.03--------
experiment: distance noise: 0.04999840507542039, bearing noise: 0.0300099733692372
exp_dist_std: 3.0615193369043186e-18, cal_dist_std: 0.0017783338444877107, diff: 0.0017783338444877076
exp_bear_std: 0.23997163550286982, cal_bear_std: 0.24119277342299889, diff: 0.0012211379201290673
exp_both_sqrt: 0.23997163550286982, diff: -7.235789624193689e-06
exp_both_std: 0.239978871292494, cal_both_std: 0.24119932923360407, diff: 0.0012204579411100591


--------distance: 8.0, distance noise: 0.05, bearing: 1.9634954084936207, bearing noise: 0.03--------
experiment: distance noise: 0.050004855580788314, bearing noise: 0.029987588112864436
exp_dist_std: 0.019136029768576687, cal_dist_std: -0.0211658110927996, diff: -0.04030184086137629
exp_bear_std: 0.22154400668438756, cal_bear_std: 0.22128599944433283, diff: -0.00025800724005473064
exp_both_sqrt: 0.22236891539303738, diff: 2.641606890832482e-05
exp_both_std: 0.22234249932412906, cal_both_std: 0.22229594037969597, diff: -4.655894443308939e-05


--------distance: 8.0, distance noise: 0.05, bearing: 2.356194490192345, bearing noise: 0.03--------
experiment: distance noise: 0.04996258704505016, bearing noise: 0.029994628655961683
exp_dist_std: 0.035328884105178114, cal_dist_std: -0.036145343212796055, diff: -0.07147422731797418
exp_bear_std: 0.169639296273154, cal_bear_std: 0.1723512093384177, diff: 0.0027119130652636936
exp_both_sqrt: 0.17327902611732335, diff: -2.6663759371131635e-05
exp_both_std: 0.17330568987669448, cal_both_std: 0.17610061100514643, diff: 0.0027949211284519493


--------distance: 8.0, distance noise: 0.05, bearing: 2.748893571891069, bearing noise: 0.03--------
experiment: distance noise: 0.04997191212624706, bearing noise: 0.029991416896885188
exp_dist_std: 0.04616802681389224, cal_dist_std: -0.044907381123325124, diff: -0.09107540793721736
exp_bear_std: 0.09189715840206866, cal_bear_std: 0.09134109750023862, diff: -0.0005560609018300383
exp_both_sqrt: 0.10284247382411205, diff: 9.131641995090145e-05
exp_both_std: 0.10275115740416114, cal_both_std: 0.10178344154086988, diff: -0.0009677158632912658


--------distance: 8.0, distance noise: 0.05, bearing: 3.141592653589793, bearing noise: 0.03--------
experiment: distance noise: 0.050041729520331514, bearing noise: 0.030010414158912185
exp_dist_std: 0.050041729520331514, cal_dist_std: -0.04997733048680747, diff: -0.10001906000713898
exp_bear_std: 0.0050946070415422385, cal_bear_std: 2.963400919839082e-17, diff: -0.005094607041542209
exp_both_sqrt: 0.05030039477274259, diff: 2.7462337246590696e-05
exp_both_std: 0.050272932435496, cal_both_std: 0.04997733048680747, diff: -0.00029560194868853

The conclusion is 
1. This experiment does work for simulating noise. 
   For this exmaple,
       --------distance: 8.0, distance noise: 0.05, bearing: 0.39269908169872414, bearing noise: 0.03--------
       experiment: distance noise: 0.049951161907419696, bearing noise: 0.02995007185116088
       exp_dist_std: 0.04614885611142251, cal_dist_std: 0.04614615483095946, diff: -2.7012804630494047e-06
       exp_bear_std: 0.09176824312867421, cal_bear_std: 0.09231160672103753, diff: 0.0005433635923633162
       exp_both_sqrt: 0.10271868071249864, diff: -6.006899042829139e-06
       exp_both_std: 0.10272468761154147, cal_both_std: 0.10320319927745643, diff: 0.00047851166591496297
   
   The real distance noise is 0.05, then exmperiment result is 0.049951161907419696. 
   The bearing result is similar, the real noise is 0.03, and the experimant result is 0.02995007185116088. 
   The experiment result is close enough to the real value.
   
2. exp_both_std ≈ sqrt(exp_dist_std ** 2 + exp_bear_std ** 2)
   For this exmaple,
       --------distance: 8.0, distance noise: 0.05, bearing: 0.39269908169872414, bearing noise: 0.03--------
       experiment: distance noise: 0.049951161907419696, bearing noise: 0.02995007185116088
       exp_dist_std: 0.04614885611142251, cal_dist_std: 0.04614615483095946, diff: -2.7012804630494047e-06
       exp_bear_std: 0.09176824312867421, cal_bear_std: 0.09231160672103753, diff: 0.0005433635923633162
       exp_both_sqrt: 0.10271868071249864, diff: -6.006899042829139e-06
       exp_both_std: 0.10272468761154147, cal_both_std: 0.10320319927745643, diff: 0.00047851166591496297
    exp_dist_std: 0.04614885611142251 (the exmperiment result of the distance with noise, the bearing has no noise.)
    exp_bear_std: 0.09176824312867421 (the exmperiment result of the bearing with noise, the distance has no noise.)
    exp_both_std: 0.10272468761154147 (the exmperiment result of both distance and bearing have noise.)
    Definitely, 
        exp_both_std != exp_dist_std + exp_bear_std, 
    Actually, exp_both_std is close to exp_both_sqrt.
       exp_both_sqrt = sqrt(exp_dist_std ** 2 + exp_bear_std ** 2)
    
3. The result of formulas are close to the experiment.
   exp_dist_std ≈ cal_dist_std
   exp_bear_std ≈ cal_bear_std
   exp_both_std ≈ cal_both_std
   
   cal_dist_std = distance_noise * math.cos(bearing)
   cal_bear_std = distance * bearing_noise * (math.sin(bearing))
   cal_both_std = math.sqrt(cal_dist_std**2 + cal_bear_std**2)

   
    
    
