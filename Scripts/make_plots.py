from pylab import *

# Make the mel scale plot
f = arange(0., 20001., 1.)
m = 1125*log(1+f/700.0)
plot(f, m, linewidth=2.0, color='red')
axis([0,20000,0, 4000])

xlabel('Frequency (Hz)')
ylabel('Mel scale (mel)')
grid(True)
savefig('mel-scale.pdf', format='pdf')
#show()


# Make the window function
def w(n):
    return 1 - abs((n - ((N-1)/2))/(N/2))

t = linspace(0,8000,8000)
N = 2
top = (n - ((N-1)/2))
bottom = ((N-1)/2)
plot(n, w(n), linewidth=2.0, color='red')

xlabel('Frequency (Hz)')
ylabel('Mel scale (mel)')
grid(True)
savefig('make-window.pdf', format='pdf')

