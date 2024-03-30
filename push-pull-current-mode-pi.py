# -*- coding: utf-8 -*-
"""
Push-pull converter current mode

@author: Alonso
"""

from math import pi, log10, sqrt
from control import tf, bode_plot, margin
L= 97.2e-6; C=7.5e-6; R=5; rl=0; rc=0
n=0.5; Rsense=0.5; Ai=3
k=n*Rsense*Ai
s = tf('s')
G = (R/k)*(1 + rc*C*s)/(1 + (R+rc)*C*s)
# PI compensator
kc=0.18; fz=1/(2*pi*R*C); 
wz=2*pi*fz
Comp= kc*(1 + s/wz)/(s/wz)
# Sensor
H=1/(1+1e-20*s) # add pole at very high frequency to avoid runtime error
# Loop gain
T=Comp*G*H
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(G, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="red" )
mag, phase, omega = bode_plot(Comp, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="green" )
mag, phase, omega = bode_plot(H, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="blue" )
mag, phase, omega = bode_plot(T, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="orange" ) 
gm, pm, wcg, wcp = margin(T)
print("Bandwidth frequency(kHz)= ", (wcp/(2*pi))/1000)
print("Phase margin(deg)= ", pm)
# Compensator components
C2=10e-9
R2=1/(2*pi*fz*C2); Ra=R2/kc; Rb=Ra
print("R2(kOhm)= ", R2/1000)
print("C2(nF)= ", C2/1e-9)
print("Ra=Rb(kOhm)= ", Ra/1000)



'''
i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=56
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
'''



