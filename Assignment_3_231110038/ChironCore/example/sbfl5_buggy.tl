penup
if :x < 50 [
	if :z < :y [
        if :z > 0[
            left 30
		    forward 100
        ]
        else[ 
            left 60
		    forward 10
        ]
	]
    else [
        if :z > 0[
            left 180
		    forward 100
        ]
        else[ 
            left 120
		    forward 100
        ]
    ]
]
else [
    if :z < :y [
        if :z > 0[
            right 30
		    forward 100
        ]
        else[ 
            right 60
		    forward 100
        ]
	]
    else [
        if :z > 0[
            right 90
		    forward 100
        ]
        else[ 
            right 10
		    forward 100
        ]
    ]
]