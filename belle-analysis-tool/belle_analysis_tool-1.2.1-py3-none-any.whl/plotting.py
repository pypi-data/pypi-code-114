def pretty_draw(frame):
    frame.GetXaxis().CenterTitle()
    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetMaxDigits(3)
    frame.Draw()
