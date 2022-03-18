import numpy as np
import scipy.linalg as la
import scipy.special as sp
import matplotlib.pyplot as plt

def baffled_circular_piston_directivity(radius,frequency,theta):
    c = 343
    k = 2*np.pi*frequency/c
    return 2*sp.jv(1,k*radius*np.sin(theta)) / (k*radius*np.sin(theta))

def get_circle_elements(total_area,num_elements):
    
    radius = np.sqrt(total_area/np.pi)
    
    diameter = 2*radius

    square_positions, square_areas = get_square_elements(diameter**2,num_elements*4/np.pi)
    
    areas = np.zeros(1)
    positions = np.zeros([1,3])
    
    # Cut out points that aren't in the circle
    for i in range(len(square_areas)):
        
        if la.norm(square_positions[i,:]) <= radius:
            areas = np.append(areas,square_areas[i])
            positions = np.append(positions,[square_positions[i,:]],axis = 0)
        
    # Removing the zeros at the top of the arrays
    areas = areas[1:]
    positions = positions[1:]
        
    return positions, areas

def get_square_elements(total_area,num_elements):
    
    length = np.sqrt(total_area)
    
    elements_length = int(np.sqrt(num_elements))
    
    dy = length/elements_length
    dz = dy
    
    areas = np.zeros(1)
    positions = np.zeros([1,3])
    
    for i in range(elements_length):
        for j in range(elements_length):
            y = (dy*i - length/2) + dy/2
            z = (dz*j - length/2) + dz/2
            areas = np.append(areas,dy*dz)
            positions = np.append(positions,[[0,y,z]],axis = 0)
            
    # Removing the zeros at the top of the arrays
    areas = areas[1:]
    positions = positions[1:]

    return positions, areas

"""
Define an array of loudspeakers
"""

def define_loudspeaker_array(num_speakers,cone_diameter,cone_separation,
                             cone_strengths = [1],
                             cone_phases = [0],
                             num_points = 100,
                             show_plots = False):

    if np.size(cone_strengths) == 1:
        cone_strengths = np.ones(num_speakers) * cone_strengths
        
    if np.size(cone_phases) == 1:
        cone_phases = np.ones(num_speakers) * cone_phases

    total_length = cone_diameter*num_speakers + cone_separation*num_speakers

    cone_positions = np.array([])
    for i in range(num_speakers):
        cone_positions = np.append(cone_positions,i*cone_separation + cone_diameter/2)
        
    # Centering about the origin
    cone_positions = cone_positions - max(cone_positions)/2 - cone_diameter/4


    # Creating the array of mini-sources
    positions = np.linspace(min(cone_positions) - cone_diameter/2,max(cone_positions)+cone_diameter/2,num_points)
    strengths = np.zeros(len(positions))
    phases = np.zeros(len(positions))
    for i in range(0,len(positions)):

        for j in range(0,num_speakers):

            if np.abs(positions[i] - cone_positions[j]) <= cone_diameter:
                strengths[i] = cone_strengths[j]
                phases[i] = cone_phases[j]

    if show_plots:
        plt.figure()
        plt.plot(positions,strengths)
        plt.title("Speaker Cone Source Strengths")
        plt.xlabel("Position (m)")
        plt.ylabel("Cone Source Strength (m^3/s)")
        
        plt.figure()
        plt.plot(positions,phases)
        plt.title("Speaker Cone Source Phases")
        plt.xlabel("Position (m)")
        plt.ylabel("Cone Phase (rad/s)")

        plt.show()
        
    return positions, strengths, phases, cone_positions
