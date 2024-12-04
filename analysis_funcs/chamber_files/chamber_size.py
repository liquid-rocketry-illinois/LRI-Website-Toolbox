import numpy as np
from mpmath import sec
from math import *
import matplotlib.pyplot as plt

def calc_size_chamber(F, r_of, p_0, p_e, L, T_0, Cp, gamma, ISP, M_e, esp):
    
    p_0 = p_0 * 6894.757 #psi to Pa
    p_e = p_e * 101325 #atm to Pa
    Cp = Cp * 1000

    Cv = Cp/gamma
    R = Cp-Cv  #Specific gas constant

    m_dot = F/(ISP/9.81)  #mass flow rate

    #Throat
    #pressure at throat (not used further)
    p_t = p_0*(1+ (gamma-1)/2 )**(-gamma/(gamma-1))
    #temperature at throat (not used further)
    T_t = T_0/(1+ (gamma-1)/2)
    #Area of throat equation
    A_t =m_dot/(p_0/sqrt(T_0)*sqrt(gamma/R*(2/(gamma+1))**((gamma+1)/(gamma-1))))
    #chamber volume
    V_c = L*A_t


    #converging section of chamber
    #Contraction_ratio = float(input("enter contraction ratio Ac/At"))
    Contraction_ratio = 5
    #Contraction_angle = float(input("enter contraction angle [radians] (recommended angle: 0.6981 radians)"))
    Contraction_angle = np.deg2rad(30)
    #Radius of throat
    R_t = sqrt(A_t/pi)
    arcR = 1.5*R_t

    #converging chamber section length
    L_n = (R_t*(sqrt(Contraction_ratio)-1) + arcR*(sec(Contraction_angle) -1))/tan(Contraction_angle)
    #chamber cross section area
    A_c = Contraction_ratio*A_t
    #chamber radius
    R_c = sqrt(A_c/pi)
    # Converging section volume
    Vconv = 1/3 * pi*(R_c**2 +R_c*R_t + R_t**2)*L_n
    #compression ratio
    eps_c = (pi*R_c**2)/A_t
    #chamber length, Just the straight bit
    L_c = (V_c-Vconv)/(pi*R_c**2)

    #Exit section of nozzle
    #Area of exit
    A_e = (A_t/M_e)* (( (1+ (gamma-1)/2 * M_e**2)/((gamma+1)/2) )**((gamma+1)/(2*(gamma-1))))
    #expansion ratio
    eps_e = A_e/A_t
    #Radius of exit
    R_e = sqrt(A_e/pi)

    #Diverging_angle = float(input("enter diverging angle [radians] (recommended angle: 0.2618 radians)"))
    Diverging_angle = np.deg2rad(10)

    #Diverging nozzle section length
    L_d = (R_t*(sqrt(Contraction_ratio)-1) + arcR*(sec(Diverging_angle) -1))/tan(Diverging_angle)

    # Generate contour from values
    # Straight part of chamber generation
    contour = [[0,0],[0,R_c],[L_c,R_c]]
    #curved part of chamber based on -atan funct
    a = 3*(R_c-R_t)/(2*pi)
    for i in range(100):
        contour.append([L_c+ i*L_n/100 ,R_c-a*atan(i*sqrt(3)/50 -sqrt(3))-a*pi/3])
    #expansion part of nozzle based on parabolic
    c = 0.547197551197
    d = 1.48205080757
    b = (R_e-R_t)/3.977642011092831
    f = L_d/13.25
    #arctan function to connect parabolic part to chamber
    for i in range(173):
        contour.append([f*i/100 +L_c+L_n ,R_t+ b*(atan(i/100 -sqrt(3))+pi/3)])
    #parabolic function for nozzle
    for i in range(int(173/.15)):
        contour.append([f*(i+173)/100 +L_c+L_n ,R_t+ b*(sqrt((i+173)/100 - d)+c)])

    x_coords = [point[0] for point in contour]
    y_coords = [point[1] for point in contour]

    return x_coords, y_coords
