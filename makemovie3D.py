import numpy
from scipy import io
import cPickle
import subprocess
import os
import sys
from enthought.mayavi import mlab
try:
    from progressbar import Bar,ProgressBar,Percentage
    showbar=True
except:
    showbar=False

def usage():
    print "Usage:"
    print "If compressed numpy objects :\n\t"+sys.argv[0]+" -n datafile.npz [-x [dt]]"
    print "If numpy objects :\n\t"+sys.argv[0]+" -y datafile-Y.npy [-x [dt]]"
    print "                      datafile-t.npy must be present"
    print "Optional argument : -x"  
    print "                   dt, time in ms between images"
    
def loadsignal():
    datafile = sys.argv[2]
    if sys.argv[1]=='-n':
        ofile=open(datafile)
        npztmp=numpy.load(ofile)
        t=npztmp['t']
        Y=npztmp['Y']
        ofile.close()
        dataext='.npz'
    elif sys.argv[1]=='-y':
        Y=numpy.load(datafile,mmap_mode='r')
        datafile_t = datafile.replace('-Y.npy','-t.npy')
        if datafile_t == datafile:
            usage()
            sys.exit(2)
        t=numpy.load(datafile_t,mmap_mode='r')
        dataext='.npy'
    else:
        usage()
        sys.exit(2)
    return t,Y,datafile,dataext

def newY1(Y,i):
    nY=Y[...,i]
    return nY

def newY2(Y,i): 
    nY=Y[i]
    return nY

#Test if correct number of arguments
if not(len(sys.argv)==4 or len(sys.argv)==5):
    usage()
    sys.exit()
    
    
#Test if tmp png dir exist, else create it
if not(os.path.isdir('png/')):
       os.mkdir('png/')

t,Y,datafile,dataext=loadsignal()  
  
if (len(sys.argv)==5):
    tstep=int(sys.argv[4])
else:
    tstep=10

#Dealing with varations of variable formats
if t.size==Y.shape[2]:
    yda=0
    ydb=1
    newY=newY1
elif t.size==Y.shape[0]:
    yda=1
    ydb=2
    newY=newY2
else:
    print "Format unknown for Y."
        

#Choose appropriate plot options according to Y dimensions 
#if (Y.shape[yda]*2>Y.shape[ydb]):
#    cbopts=dict(pad=0.1)
#    figy=6    
#else:
#    cbopts=dict(pad=0.1, orientation='horizontal')
#    figy=3


print "Writing png files from "+sys.argv[2]
if showbar:
    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=len(t)).start()

i=0


x,y,z = Y.shape[:-1]


if (len(sys.argv)>=4):
    if sys.argv[3] == '-x':
        inp = raw_input("Enter the coordinates for the visualisation : '(x,y,z)' ")
        exec( '(xmax,ymax,zmax) = ' + inp)
else:
    imax = abs(Y[...,-1]).argmax()
    zmax = imax % z
    ymax = ( (imax - zmax) / z ) % y 
    xmax = (imax -y -z) / y / z
mlab.figure(size=(800,600))
p = mlab.pipeline.scalar_field(Y[...,i])
p.scene.background = (0.9,0.9,0.9)
titl=mlab.title(str("Potential at time: %.0f ms."% t[i]),size=0.5)
s = mlab.pipeline.image_plane_widget( p,
                            plane_orientation='x_axes',
                            slice_index=xmax,
                            vmin = -60,
                            vmax = 10
                        )

s2 = mlab.pipeline.image_plane_widget(p,
                            plane_orientation='y_axes',
                            slice_index=ymax,
                            vmin = -60,
                            vmax = 10
                        )
s3 = mlab.pipeline.image_plane_widget( p,
                            plane_orientation='z_axes',
                            slice_index=zmax,
                            vmin = -60,
                            vmax = 10
                        )

mlab.scalarbar(s,orientation='vertical',nb_labels=4,label_fmt='%.3f')
mlab.outline(color=(1,1,1))

filename = str('png/2F_%04d' % i) + '.png'
mlab.savefig(filename)

for i in range(int(tstep/round(max(t)/len(t))),len(t),int(tstep/round(max(t)/len(t)))) :
    #
    # The next four lines are just like MATLAB.
    #
    p.mlab_source.scalars = Y[...,i]
    titl.text=str("Potential at time: %.0f ms."% t[i])
    filename = str('png/2F_%04d' % i) + '.png'
    mlab.savefig(filename)
    if showbar:
        pbar.update(i)


del Y,t
if showbar:    
    pbar.finish()
# Now that we have graphed images of the dataset, we will stitch them
# together using Mencoder to create a movie.  Each image will become
# a single frame in the movie.
#
# We want to use Python to make what would normally be a command line
# call to Mencoder.  Specifically, the command line call we want to
# emulate is (without the initial '#'):
# mencoder mf://*.png -mf type=png:w=800:h=600:fps=25 -ovc lavc -lavcopts vcodec=mpeg4 -oac copy -o output.avi
# See the MPlayer and Mencoder documentation for details.
#
vidfile=datafile.replace(dataext,'.avi')
command = ('mencoder',
           'mf://png/2F*.png',
           '-mf',
           'type=png:w=800:h=600:fps=25',
          '-ovc',
           'xvid',
           '-xvidencopts',
           'pass=1',
           '-oac',
           'copy',
           '-o',
           vidfile)

#os.spawnvp(os.P_WAIT, 'mencoder', command)

print "\n\nabout to execute:\n%s\n\n" % ' '.join(command)
subprocess.check_call(command)

print "\n\n The movie was written to "+vidfile


#Ask to delete tmp png files
if raw_input('Delete *.png files (y/N)? ')=="y":
    os.popen('rm png/2F_*')

#exists 
