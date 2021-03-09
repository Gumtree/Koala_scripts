# Script control setup area
# script info
__script__.title = 'Koala Control'
__script__.version = '0.1'

# Use below example to create parameters.
# The type can be string, int, float, bool, file.

title = Par('label', 'Koala control wizard')
title.font_size = 24

tab1 = Tab('Alignment')
tab2 = Tab('Experiment')

gdif = Group('Diffractometer Control')
#gdif.tier = 1

gsphi = Group('Sample Phi angle')
gsphi.tier = 2
gsphi.numColumns = 4
gsphi.equalWidth = True

aod = Act('open_diff()', 'Open Diffractometer')
aod.colspan = 2
aod.height = 40
acd = Act('close_diff()', 'Close Diffractometer')
acd.colspan = 2
acd.height = 40
sp1 = Par('space')
sp1.colspan = 4

psphi = Par('float', 0.)
psphi.title = 'Target angle'
psphi.colspan = 2
asphi = Act('move_samphi()', 'Drive sample Phi')
asphi.colspan = 2
asphi.height = 40
sp2 = Par('space')
sp2.colspan = 4

psphi_c = Par('float', 0.)
psphi_c.title = 'Current angle'
psphi_c.enabled = False
psphi_c.colspan = 2
psphi_c.enable = False
pleft = Act('sphi_left()', '<<')
pleft.colspan = 1
pright = Act('sphi_right()', '>>')
pright.colspan = 1

#sp1 = Par('space')
#sp1.colspan = 2

gsphi.add(aod, acd, sp1, psphi, asphi, sp2, 
          psphi_c, pleft, pright)

greset = Group('Motor Reset')
greset.tier = 2
greset.numColumns = 2
greset.equalWidth = True
freset = Act('full_reset()', 'Full Motor Reset')
freset.colspan = 1
freset.height = 40
qreset = Act('quick_reset()', 'Quick Motor Reset')
qreset.colspan = 1
qreset.height = 40

greset.add(freset, qreset)
greset.folded = False

gdif.add(gsphi, greset)

gcry = Group('Cryostat')
gcry.tier = 1
gcry.numColumns = 4
tset = Par('float', 300)
tset.title = 'Set point'
tunits = Par('string', 'K', options = ['K', 'C'])
tunits.title = ''
acry = Act('drive_temp()', 'Set the temperature')
acry.colspan = 1
acry.height = 40
gcry.add(tset, tunits, acry)

gsample = Group('Sample Offsets')
gsample.tier = 1

gsho = Group('Sample Height Offset [negative]')
gsho.tier = 2
gsho.numColumns = 4
hoff = Par('float', 0)
hoff.title = 'Current Offset (mm) '
hoff.enabled = False
hoff.colspan = 2
#hunits = Par('label', 'mm')
#hunits.width = 30
ahoff = Act('check_offset()', 'Check Offset')
ahoff.colspan = 2
ahoff.height = 40
gsho.add(hoff, ahoff)

gsxo = Group('Sample X Offset')
gsxo.tier = 2
gsxo.numColumns = 4

tsxo = Par('float', 0)
tsxo.title = 'Target offset'
tsxo.colspan = 2

asxo = Act('drive_sx()', 'Move')
asxo.height = 40
asxo.colspan = 2

sp1 = Par('space')
sp1.colspan = 4

csxo = Par('float', 0)
csxo.title = 'Current offset'
csxo.enabled = False
csxo.colspan = 2

sxleft = Act('sx_left()', '<<')
sxleft.colspan = 1
sxright = Act('sx_right()', '>>')
sxright.colspan = 1

gsxo.add(tsxo, asxo, sp1, csxo, sxleft, sxright)


gsyo = Group('Sample Y Offset')
gsyo.tier = 2
gsyo.numColumns = 4

tsyo = Par('float', 0)
tsyo.title = 'Target offset'
tsyo.colspan = 2

asyo = Act('drive_sy()', 'Move')
asyo.colspan = 2
asyo.height = 40

sp2 = Par('space')
sp2.colspan = 4

csyo = Par('float', 0)
csyo.title = 'Current offset'
csyo.enabled = False
csyo.colspan = 2

syleft = Act('sy_left()', '<<')
syleft.colspan = 1
syright = Act('sy_right()', '>>')
syright.colspan = 1

gsyo.add(tsyo, asyo, sp2, csyo, syleft, syright)


gsample.add(gsho, gsxo, gsyo)

tab1.add(gdif, gcry, gsample)
#tab2.add()

#tg = Group('test')
#pt = Par('string', 'test par')
#tg.add(pt)

def open_diff():
    print 'diffractometer open'

def close_diff():
    print 'diffractometer closed'

def move_samphi():
    print ('drive sample Phi to {}'.format(psphi.value))
    
def sphi_left():
    print 'jog left'

def sphi_right():
    print 'jog right'
    
def full_reset():
    print("full motor reset")    

def quick_reset():
    print("quick motor reset")    

def check_offset():
    print("check sample height offset")
    
def drive_temp():
    print("drive temperature to {} {}".format(tset.value, 
                                              tunits.value))
    
def drive_sx():
    print("drive sx offset")

def drive_sy():
    print("drive sy offset")

def sx_left():
    print("nudge sx offset left")

def sx_right():
    print("nudge sx offset right")

def sy_left():
    print("nudge sy offset left")

def sy_right():
    print("nudge sy offset right")

# Use below example to create a new Plot
# Plot4 = Plot(title = 'new plot')

# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
    # Use the provided resources, please don't remove.
    global Plot1
    global Plot2
    global Plot3
    
    # check if a list of file names has been given
    if (fns is None or len(fns) == 0) :
        print 'no input datasets'
    else :
        for fn in fns:
            # load dataset with each file name
            ds = df[fn]
            print ds.shape
    print arg1_name.value
    
def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
