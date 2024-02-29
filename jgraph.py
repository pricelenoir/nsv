def jgraph(player_name, start_season, end_season, df):
    print("newgraph")
    # Dimensions for court is x: [-250, 250]; y: [-47.5, 422.5]
    print("xaxis min -300 max 300 size 5 nodraw")
    print("yaxis min -87.5 max 475 size 5 nodraw")

    # 3pt line
    # Extends 23.75 ft to top of the key
    print("newline marktype circle marksize 475 fill 1 pts 0 14")
    print("newline poly color 1 1 1 pts -250 -47.5  -250 92.5  250 92.5  250 -47.5")
    # 22ft to corner 3
    print("newline pts -222 -47.5  -222 92.5")
    print("newline pts 222 -47.5  222 92.5")

    # Center court
    print("newline marktype circle marksize 120 fill 1 pts 0 422.5")
    print("newline marktype circle marksize 40 fill 1 pts 0 422.5")

    # Add court border
    print("newline pts -250 -47.5  -250 422.5  250 422.5  250 -47.5  -250 -47.5")

    # Create backboard
    print("newline pts -30 -12.5  30 -12.5")

    # Create the paint
    print("newline pts -80 -47.5   80 -47.5   80 142.5  -80 142.5  -80 -47.5") # Outer
    print("newline pts -60 -47.5   60 -47.5   60 142.5  -60 142.5  -60 -47.5") # Inner

    # Freethrow arcs
    print("newline marktype circle marksize 120 fill 1 pts 0 142.5")
    print("newline pts -60 142.5  60 142.5")

    # Define counter variables
    fg = 0
    fga = 0
    fg_3 = 0
    fga_3 = 0

    for index, row in df.iterrows():
        fga += 1
        if (row['SHOT_MADE_FLAG'] == 1):
            # Print made shot
            print("newcurve marktype circle color 0.2 1 0.2 marksize 4 pts")
            print(row['LOC_X'], row['LOC_Y'])
            fg += 1
        else:
            # Print missed shot
            print("newcurve marktype circle color 1 0 0 marksize 4 pts")
            print(row['LOC_X'], row['LOC_Y'])

        # Increment 3pt stats
        if (row['SHOT_TYPE'] == 1):
            fga_3 += 1
            if (row['SHOT_MADE_FLAG'] == 1):
                fg_3 += 1

    print("newline poly color 1 1 1 pts -250 424  -250 540  250 540  250 424")
    print("newline poly color 1 1 1 pts -250 -90  -250 -49  250 -49  250 -90")

    # Create hoop 
    print("newline marktype circle marksize 15 fill 1 pts 0 0")

    # Print player info
    print("newstring hjc vjc x 0 y 520 fontsize 1 lcolor 1 1 1 font Courier : .") # Used this to extend the plot without adjusting y axis
    print("newstring hjc vjc x 0 y 495 fontsize 20 font Courier : ", player_name)
    print("newstring hjc vjc x 0 y 465 fontsize 14 font Courier : ", start_season, "-", end_season)
    print("newstring hjc vjc x 0 y 440 fontsize 12 font Courier : FG: {}/{} ({:.1%}) 3FG: {}/{} ({:.1%})".format(fg, fga, fg/fga, fg_3, fga_3, fg_3/fga_3))