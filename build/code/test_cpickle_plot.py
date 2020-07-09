# -*- coding: utf-8 -*-

import cPickle, matplotlib, matplotlib.pyplot, numpy

# Data for plotting
t = numpy.arange(0.0, 2.0, 0.01)
s = 1 + numpy.sin(2 * numpy.pi * t)

fig, ax = matplotlib.pyplot.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

dst = '..\\temp\\test.bin'

fig.set_size_inches(8, 6, forward=True)
fig.tight_layout()

print 'test save'

f = open(dst, 'wb')
cPickle.dump(fig, f)
f.close()

print 'test load'
    
f = open(dst, 'rb')
test = cPickle.load(f)
f.close()

print 'test load 2'

f = open('..\\..\\data\\borders\\blank_map.bin')
test2 = cPickle.load(f)
f.close()

print 'test save 3'

matplotlib.pyplot.savefig('..\\temp\\test.png', bbox_inches='tight')
matplotlib.pyplot.close(fig)
