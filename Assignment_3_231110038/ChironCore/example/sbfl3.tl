penup
if :x > :y [
	if :y < 50 [
		if :z > 90[
            left :z]
        else[
            right :z]
        forward 100
	]
]
else [
    if :y < 50 [
		if :z > 90[
            left :z]
        else[
            right :z]
        forward 100
	]
]