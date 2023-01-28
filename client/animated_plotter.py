from connector import *
from animations import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

port = "/dev/rfcomm0"
ser = connect_serial(port)

test = get_samples(ser, 10)

dataList_ypr = [[0,0,0]]
dataList_a = [[0,0,0]]
dataList_g = [[0,0,0]]
dataList_e = [[0,0,0]]
dataList_ar = [[0,0,0]]
dataList_aw = [[0,0,0]]

dataList_q = [[0,0,0,0]]
dataList_hall = [0]

fig1, ((ax_a, ax_r)) = plt.subplots(1, 2)
fig2, ((ax_ypr, ax_e)) = plt.subplots(1, 2)

fig3, ax_hall = plt.subplots(1,1)

ani_ypr = animation.FuncAnimation(fig2, animate_3line, frames=30, fargs=(ax_ypr, dataList_ypr, ser, "ypr"), interval=0.1)
ani_e = animation.FuncAnimation(fig2, animate_3line, frames=30, fargs=(ax_e, dataList_e, ser, "e"), interval=0.1)
ani_a = animation.FuncAnimation(fig1, animate_3line, frames=30, fargs=(ax_a, dataList_a, ser, "a"), interval=0.1)
ani_ar = animation.FuncAnimation(fig1, animate_3line, frames=30, fargs=(ax_r, dataList_ar, ser, "ar"), interval=0.1)

ani_hall = animation.FuncAnimation(fig3, animate_1line, frames=30, fargs=(ax_hall, dataList_hall, ser, "hall"), interval=0.1)

plt.show()

ser.close()
