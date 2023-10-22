
This exercise wasa taken from _Python for Scienitifc Computing and Artifical Intelligenc.


[Modelling the Three Body Problem in Classical Mechanics using Python](https://towardsdatascience.com/modelling-the-three-body-problem-in-classical-mechanics-using-python-9dc270ad7767)
Uses the ordinary differential solver from scipy.

```commandline
#Package initial parameters
init_params=sci.array([r1,r2,v1,v2]) #create array of initial params
init_params=init_params.flatten() #flatten array to make it 1D
time_span=sci.linspace(0,8,500) #8 orbital periods and 500 points
#Run the ODE solver
import scipy.integrate
two_body_sol=sci.integrate.odeint(TwoBodyEquations,init_params,time_span,args=(G,m1,m2))
```

[Use Python to Create Three-Body Orbits](https://towardsdatascience.com/use-python-to-create-three-body-orbits-329ffb5b2627)

Animations. Some interesting configurations.

http://three-body.ipb.ac.rs/sheen_sol.php?id=3

A remarkable periodic solution of the three-body problem in the case of equal masses
by Alain Chenciner and Richard Montgomery
Annals of Mathematics, 152 (2000), 881–901
https://arxiv.org/pdf/math/0011268.pdf