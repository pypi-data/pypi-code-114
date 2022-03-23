def zalupa(x, y):
    import turtle as tl
    cur_x = x - tl.window_width() // 2
    cur_y = -y + tl.window_height() // 2
    tl.color('white')
    tl.goto(cur_x, cur_y)
    tl.pencolor('green')
    tl.pensize(5)
    tl.forward(100)
    tl.right(125)
    tl.forward(160)
    tl.left(125)
    tl.forward(100)
    tl.exitonclick()

