import turtle as t
import colorsys as c
t.speed(0)
t.bgcolor('black')
for j in range(1,40):
	for i in range (1,11):
		t.pencolor(c.hsv_to_rgb(j/40,i/(10),1))
		t.fd(100+3.333333333291563*j)
		t.circle((30+j),213.3985)
		t.fd(100+3.333333333291563*j)
		t.rt(177.3985)
	t.setposition(0,0)
t.position()