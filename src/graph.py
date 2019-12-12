import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

fig = plt.figure()
ax = plt.axes()
line, = ax.plot([],[], lw=2)
data = []
xd = []
yd = []

def init():
	line.set_data([],[])
	return line,

def animate(frame):
	yd.append(data[frame])
	xd.append(frame)
	line.set_data(xd,yd)
	return line,

def graph(file):
	global data, line, ax

	plt.xlabel('Time (seconds)')
	plt.ylabel('Bandwidth (Mbit/s)')
	plt.title('TCP fairness experiment')

	file_c = open(file,'r').read()
	data = [int(x) for x in file_c.split(' Mbit/s\n') if x != '']

	ax = plt.axes(xlim=(0,int(len(data))), ylim=(0,int(max(data))))
	line, = ax.plot([],[], lw=2)
	ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(data), interval=1000, blit=True) # 1 second
	ani.save('../results/res_{}.gif'.format(file), writer='imagemagick')
	#plt.show()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Plotter of bandwidth test.')
	parser.add_argument('-f', '--file', type=str, help='log file', required=True)
	args = parser.parse_args()

	graph(args.file)
