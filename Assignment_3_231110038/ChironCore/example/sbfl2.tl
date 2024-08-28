penup
if :x > :y [
	if :y > :z [
		left 60
		forward 50
		right 120
		forward 50
	]
	else [
		backward 80
		right 120
		forward 50
	]
]
else [
	right 60
	forward 80
	right 120
	forward 80
]