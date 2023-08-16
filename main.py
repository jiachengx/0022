def controlMoto(text: str):
    if text == "L":
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    elif text == "R":
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    elif text == "F":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
    elif text == "D":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 50)
    elif text == "A":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 90)
    elif text == "B":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 90)
    elif text == "AB":
        maqueen.motor_stop(maqueen.Motors.ALL)
    else:
        pass

def on_received_string(receivedString):
    global recvData
    recvData = receivedString
    if recvData == "00":
        controlMoto("D")
        basic.show_arrow(ArrowNames.SOUTH)
    elif recvData == "01":
        controlMoto("R")
        basic.show_arrow(ArrowNames.EAST)
    elif recvData == "10":
        basic.show_arrow(ArrowNames.WEST)
        controlMoto("L")
    elif recvData == "11":
        basic.show_arrow(ArrowNames.NORTH)
        controlMoto("F")
    elif recvData == "A":
        basic.show_string("A")
        controlMoto("A")
    elif recvData == "B":
        basic.show_string("B")
        controlMoto("B")
    elif recvData == "AB":
        basic.show_string("AB")
        controlMoto("AB")
    else:
        basic.clear_screen()
radio.on_received_string(on_received_string)

recvData = ""
radio.set_group(20)
basic.show_arrow(ArrowNames.SOUTH_WEST)

def on_forever():
    pass
basic.forever(on_forever)
