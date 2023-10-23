
This exercise wasa taken from _Python for Scientifc Computing and Artifical Intelligenc.

# Sources

## Three-Body Gallery

Great website!
http://three-body.ipb.ac.rs/

## ODE Solver
[Modelling the Three Body Problem in Classical Mechanics using Python](https://towardsdatascience.com/modelling-the-three-body-problem-in-classical-mechanics-using-python-9dc270ad7767)
Uses the ordinary differential solver from scipy.

<details>
<summary> Click for code snippet</summary>

```
def ThreeBodyEquations(w,t,G,m1,m2,m3):
    r1=w[:3]
    r2=w[3:6]
    r3=w[6:9]
    v1=w[9:12]
    v2=w[12:15]
    v3=w[15:18]
    r12=sci.linalg.norm(r2-r1)
    r13=sci.linalg.norm(r3-r1)
    r23=sci.linalg.norm(r3-r2)
    
    dv1bydt=K1*m2*(r2-r1)/r12**3+K1*m3*(r3-r1)/r13**3
    dv2bydt=K1*m1*(r1-r2)/r12**3+K1*m3*(r3-r2)/r23**3
    dv3bydt=K1*m1*(r1-r3)/r13**3+K1*m2*(r2-r3)/r23**3
    dr1bydt=K2*v1
    dr2bydt=K2*v2
    dr3bydt=K2*v3
    r12_derivs=sci.concatenate((dr1bydt,dr2bydt))
    r_derivs=sci.concatenate((r12_derivs,dr3bydt))
    v12_derivs=sci.concatenate((dv1bydt,dv2bydt))
    v_derivs=sci.concatenate((v12_derivs,dv3bydt))
    derivs=sci.concatenate((r_derivs,v_derivs))
    return derivs

#Run the ODE solver
import scipy.integrate
three_body_sol=sci.integrate.odeint(ThreeBodyEquations,init_params,time_span,
                                    args=(G,m1,m2,m3))

```

</details>

## Python Solution
[Use Python to Create Three-Body Orbits](https://towardsdatascience.com/use-python-to-create-three-body-orbits-329ffb5b2627)

Animations. Some interesting configurations.

## Rediscovery of figure eight path
A remarkable periodic solution of the three-body problem in the case of equal masses
by Alain Chenciner and Richard Montgomery
Annals of Mathematics, 152 (2000), 881–901
https://arxiv.org/pdf/math/0011268.pdf

## Discovery of new configs

https://arxiv.org/pdf/1303.0181.pdf

##### Press Release 

[Physicists Discover a Whopping 13 New Solutions to Three-Body Problem](https://www.science.org/content/article/physicists-discover-whopping-13-new-solutions-three-body-problem)

