penup
if :x > :y [
	if :y > 0 [
        forward 50
        left 90
        forward 50
    ]
    else[
        backward 100
    ]
]
else [
    if :y < 0 [
        backward 50
        left 90
        forward 50
    ]
    else[
        forward 100
    ]
]