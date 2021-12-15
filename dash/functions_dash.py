#-----------------------------------------
#----------LIBRARIES FOR FUNCTIONS--------
#-----------------------------------------
from io import BytesIO
import base64
from typing import Counter
import matplotlib.pyplot as plt
from math import pi, hypot, sin, cos, atan2, degrees


# FUNCTION TO GENERATE POINTS ALONG AN ARC
def arc_points(start_x:float, start_y:float, end_x:float, end_y:float, time_step:float):
    """Returns a lists of x-coordinates and y-coordinates along an arc given 2 known points.
    Outputs: return arc_x (list of x-coordinates), arc_y (list of y-coordinates)
    Source: https://stackoverflow.com/questions/48603681/plot-arc-path-between-two-points
    """
    def norm_angle(a):
        """Normalize the angle to be between -pi and pi"""
        return (a+pi)%(2*pi) - pi
    
    theta_0 = -pi/2      # initial orientation                
    t_0 = 0              # starting time

    r_G = hypot(end_x - start_x, end_y - start_y)        # relative polar coordinates
    phi_G = atan2(end_y - start_y, end_x - start_x)
    phi = 2*norm_angle(phi_G - theta_0)      # angle and 
    r_C = r_G/(2*sin(phi_G - theta_0))       # radius (sometimes negative) of the arc
    L = r_C*phi                              # length of the arc
    if phi > pi:
        phi -= 2*pi
        L = -r_C*phi
    elif phi < -pi:
        phi += 2*pi
        L = -r_C*phi
    t_1 = L/time_step + t_0                        # time at which the robot finishes the arc
    omega = phi/((t_1 - t_0)+0.01)                # angular velocity -- CJG added 0.01 to prevent zero divisor          
    x_C = start_x - r_C*sin(theta_0)           # center of rotation
    y_C = start_y + r_C*cos(theta_0)

    arc_x = []
    arc_y = []
    for t in range(t_0, int(t_1)+1):
        x = x_C + r_C*sin(omega*(t - t_0) + theta_0)
        arc_x.append(x)
        y = y_C - r_C*cos(omega*(t - t_0) + theta_0)
        arc_y.append(y)
    
    return arc_x, arc_y



# FUNCTION TO EXPORT MATPLOTLIB PLOTTING FIGURE AS URI
def fig_to_uri(in_fig:str, close_all=True, **save_args):
    """Returns the URI for a matplotlib.pyplot figure. 
    The 'in_fig' argument is in the form e.g. " in_fig = plt.<Figure/subplot()>"
    Requires the following libraries: 
        from io import BytesIO
        import base64
        import matplotlib.pyplot as plt
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)




