## Assignment 3 ME369P
## Name:
## EID:
##
import math as m


'''
Kwargs can be:
    initial_step        : float
    max_step            : float
    relative_tolerance  : float
'''
#Do not modify the function input parameters
def ODE45( func, duration, initial_states, **kwargs):

    return time, states


def mySystem( t, y ):
    # This is given, do not modify
    y_prime_1 = y[1]
    y_prime_2 = 0.3*y[1] - 0.1*y[0] + 4*m.cos(t)
    y_prime = ( y_prime_1, y_prime_2)
    return y_prime

def PlotStates(time, states):
    ## Bonus Function
    return

def main():
    time, states = ODE45( mySystem, [0, 30], [4, 0])

if __name__ == '__main__':
    main()
