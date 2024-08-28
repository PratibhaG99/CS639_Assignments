penup
if :x > :y [
	if :y < 50 [
		if :z > 100[
            left :z]
        else[
            right :z]
        forward 100
	]
]
else [
    if :y < 50 [
		if :z > 80[
            left :z]
        else[
            right :z]
        forward 50
	]
]