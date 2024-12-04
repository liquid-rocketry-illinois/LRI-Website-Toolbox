string1 = r'''
The first euqation we use is Newtons Law of Cooling $q = h_{gas}(T_{aw} - T_{hw})$ 
$q = {heat flux}$
$h_{gas} = {coefficent of heat transfer}$
$T_{aw} = {temperature of the adiabadic wall}$
$T_{hw} = {temperature of the hot wall}$
$T_{aw}$ is dependent on the free stream temperature $T_{st}$ as seen below:
'''

def get_regen_string(str):
    if str == 'string1':
        return string1