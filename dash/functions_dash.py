#-----------------------------------------
#----------LIBRARIES FOR FUNCTIONS--------
#-----------------------------------------
from io import BytesIO
import base64
import matplotlib.pyplot as plt




# FUNCTION TO EXPORT PLOTTING FIGURE AS URI
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