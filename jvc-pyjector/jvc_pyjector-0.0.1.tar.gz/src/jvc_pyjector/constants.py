from enum import Enum

class Commands(Enum):
    # power
    power_off       = b"\x21\x89\x01PW0\x0A"
    power_on        = b"\x21\x89\x01PW1\x0A"
    power_status    = b"\x3F\x89\x01PW\x0A"

    # hide
    hide_toggle     = b"\x21\x89\x01RC731D\x0A"
    hide_on         = b"\x21\x89\x01RC73D0\x0A"
    hide_off        = b"\x21\x89\x01RC73D1\x0A"

    # navigation
    up              = b"\x21\x89\x01RC7301\x0A"
    down            = b"\x21\x89\x01RC7302\x0A"
    left            = b"\x21\x89\x01RC7336\x0A"
    right           = b"\x21\x89\x01RC7334\x0A"
    ok              = b"\x21\x89\x01RC732F\x0A"
    back            = b"\x21\x89\x01RC7303\x0A"
    menu            = b"\x21\x89\x01RC732E\x0A"

    # input
    input_status    = b"\x3F\x89\x01IP\x0A"
    hdmi1           = b"\x21\x89\x01IP6\x0A"
    hdmi2           = b"\x21\x89\x01IP7\x0A"

class Power(Enum):
    # powered off / on
    powered_off     = b"\x40\x89\x01PW0\x0A"
    powered_on      = b"\x40\x89\x01PW1\x0A"
    
    # powering off / on
    powering_off     = b"\x40\x89\x01PW2\x0A"
    powering_on      = b"\x40\x89\x01PW3\x0A"

    # doom's day
    emergency       = b"\x40\x89\x01PW4\x0A"

class Handshake(Enum):
    request         = b"PJREQ"
    ok              = b"PJ_OK"
    ack             = b"PJACK"

class Values(Enum):
    # used to create expected acks
    prefix          = b"\x06\x89\x01"
    suffix          = b"\x0A"