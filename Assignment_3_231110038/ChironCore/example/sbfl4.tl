penup
if :x < 0 [
	if :z < :x [
        if :y > 0[
            left 90
            forward 40
        ]
        else[
            right 90
            forward 80
        ]
	]
    else [
        backward 80
    ]
]
else [
	if :z < :x [
        if :y > 0[
            left 60
            forward 20
        ]
        else[
            right 60
            forward 40
        ]
	]
    else [
        forward 80
    ]
]