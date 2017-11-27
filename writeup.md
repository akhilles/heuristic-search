# Heuristic Search Assignment

## a)
`front-end` folder

![front end](./frontend.png)


## b)
`search.py` has the abstract heuristic algorithm  
`SearchClasses.py` has the various instantiations of it

## c)


## d)

**Best admissible/consistent heuristic:**

**Manhattan:** Manhattan distance from the point to the goal

**Custom1:**

**Custom2:**

**Custom3:** Maximum of distance from goal in the x-axis and distance from goal in the y-axis

## e)

Benchmark data collected for each heuristic and the following weights [0,1,1.5,2.5]:
```
- Admissible, w: 0
average path cost:       111.84385927461732
average expanded nodes:  103047.46
average run time:        1.0151276588439941
average visited/optimum: 1.481836334744668
- Admissible, w: 1
average path cost:       111.84385927461732
average expanded nodes:  78096.7
average run time:        0.8967481184005738
average visited/optimum: 1.481836334744668
- Admissible, w: 1.5
average path cost:       115.50471856198911
average expanded nodes:  35331.06
average run time:        0.4995976734161377
average visited/optimum: 1.3325063384040943
- Admissible, w: 2.5
average path cost:       176.2280337783883
average expanded nodes:  1429.0
average run time:        0.07152163028717042
average visited/optimum: 1.0739431016619791
- Manhattan, w: 0
average path cost:       111.84385927461732
average expanded nodes:  103047.46
average run time:        1.0491833257675172
average visited/optimum: 1.481836334744668
- Manhattan, w: 1
average path cost:       139.80380944789016
average expanded nodes:  7422.84
average run time:        0.12337670803070068
average visited/optimum: 1.2126789475216173
- Manhattan, w: 1.5
average path cost:       183.72135122493907
average expanded nodes:  1081.66
average run time:        0.04007392406463623
average visited/optimum: 1.0638882634163012
- Manhattan, w: 2.5
average path cost:       186.26661384514657
average expanded nodes:  1047.16
average run time:        0.03606216430664062
average visited/optimum: 1.0623821824725703
- Custom1, w: 0
average path cost:       111.84385927461732
average expanded nodes:  103047.46
average run time:        0.950502758026123
average visited/optimum: 1.481836334744668
- Custom1, w: 1
average path cost:       114.05131669041234
average expanded nodes:  41443.94
average run time:        0.6460857582092285
average visited/optimum: 1.3750903480649506
- Custom1, w: 1.5
average path cost:       155.10482817641238
average expanded nodes:  4278.12
average run time:        0.085530686378479
average visited/optimum: 1.1136014256167401
- Custom1, w: 2.5
average path cost:       183.4517610314042
average expanded nodes:  1042.0
average run time:        0.05516284465789795
average visited/optimum: 1.0488947512356441
- Custom2, w: 0
average path cost:       111.84385927461732
average expanded nodes:  103047.46
average run time:        1.0684921503067017
average visited/optimum: 1.481836334744668
- Custom2, w: 1
average path cost:       115.52862116419536
average expanded nodes:  37782.74
average run time:        0.5155617475509644
average visited/optimum: 1.3789415862135757
- Custom2, w: 1.5
average path cost:       155.08399339882607
average expanded nodes:  1345.1
average run time:        0.0807570219039917
average visited/optimum: 1.0664133543542191
- Custom2, w: 2.5
average path cost:       169.07112252341875
average expanded nodes:  1011.66
average run time:        0.07502131938934326
average visited/optimum: 1.0259286752138546
- Custom3, w: 0
average path cost:       111.84385927461732
average expanded nodes:  103047.46
average run time:        1.042763123512268
average visited/optimum: 1.481836334744668
- Custom3, w: 1
average path cost:       125.29175608280576
average expanded nodes:  26403.3
average run time:        0.39967933654785154
average visited/optimum: 1.3113612389657283
- Custom3, w: 1.5
average path cost:       168.65461748553926
average expanded nodes:  1211.78
average run time:        0.04547203540802002
average visited/optimum: 1.0771243343236003
- Custom3, w: 2.5
average path cost:       173.18652440774997
average expanded nodes:  1080.38
average run time:        0.053687214851379395
average visited/optimum: 1.077040049702986
```

## f)


## g)


## h)


## i)