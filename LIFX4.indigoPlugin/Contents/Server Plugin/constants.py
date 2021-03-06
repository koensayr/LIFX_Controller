#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# LIFX V4 Controller - Constants © Autolog 2016
#

# plugin Constants

# Number of discoveries to executed at start-up
START_UP_REQUIRED_DISCOVERY_COUNT = 10 

# QUEUE Priorities
QUEUE_PRIORITY_STOP_THREAD   = 0
QUEUE_PRIORITY_WAVEFORM      = 100
QUEUE_PRIORITY_COMMAND       = 200
QUEUE_PRIORITY_STATUS_HIGH   = 300
QUEUE_PRIORITY_STATUS_MEDIUM = 400
QUEUE_PRIORITY_DISCOVERY     = 500
QUEUE_PRIORITY_POLLING       = 600
QUEUE_PRIORITY_LOW           = 700

# LIFX product constants
LIFX_PRODUCTS = {}
#                    Color, Infrared, Multizone, Name
LIFX_PRODUCTS[1]  = (True,  False, False, 'Original 1000')
LIFX_PRODUCTS[3]  = (True,  False, False, 'Color 650')
LIFX_PRODUCTS[10] = (False, False, False, 'White 800 (Low Voltage)')
LIFX_PRODUCTS[11] = (False, False, False, 'White 800 (High Voltage)')
LIFX_PRODUCTS[18] = (False, False, False, 'White 900 BR30 (Low Voltage)')
LIFX_PRODUCTS[20] = (True,  False, False, 'Color 1000 BR30')
LIFX_PRODUCTS[22] = (True,  False, False, 'Color 1000')
LIFX_PRODUCTS[27] = (True,  False, False, 'LIFX A19')
LIFX_PRODUCTS[28] = (True,  False, False, 'LIFX BR30')
LIFX_PRODUCTS[29] = (True,  True,  False, 'LIFX + A19')
LIFX_PRODUCTS[30] = (True,  True,  False, 'LIFX + BR30')
LIFX_PRODUCTS[31] = (True,  False, True,  'LIFX Z')

LIFX_PRODUCT_SUPPORTS_COLOR = 0
LIFX_PRODUCT_SUPPORTS_INFRARED = 1
LIFX_PRODUCT_SUPPORTS_MULTIZONE = 2
LIFX_PRODUCT_NAME = 3


# LIFX Waveform Types
LIFX_WAVEFORMS = {}
LIFX_WAVEFORMS['0'] = 'Saw'
LIFX_WAVEFORMS['1'] = 'Sine'
LIFX_WAVEFORMS['2'] = 'Half-Sine'
LIFX_WAVEFORMS['3'] = 'Triangle'
LIFX_WAVEFORMS['4'] = 'Pulse'

# LIFX Kelvin Descriptions (from iOS LIFX App)
LIFX_KELVINS = {}
LIFX_KELVINS[2500] = ((246,221,184), '2500K Ultra Warm')
LIFX_KELVINS[2750] = ((246,224,184), '2750K Incandescent')
LIFX_KELVINS[3000] = ((248,227,195), '3000K Warm')
LIFX_KELVINS[3200] = ((247,228,198), '3200K Neutral Warm')
LIFX_KELVINS[3500] = ((246,228,201), '3500K Neutral')
LIFX_KELVINS[4000] = ((249,234,210), '4000K Cool')
LIFX_KELVINS[4500] = ((250,238,217), '4500K Cool Daylight')
LIFX_KELVINS[5000] = ((250,239,219), '5000K Soft Daylight')
LIFX_KELVINS[5500] = ((249,240,225), '5500K Daylight')
LIFX_KELVINS[6000] = ((247,241,230), '6000K Noon Daylight')
LIFX_KELVINS[6500] = ((245,242,234), '6500K Bright Daylight')
LIFX_KELVINS[7000] = ((241,240,236), '7000K Cloudy Daylight')
LIFX_KELVINS[7500] = ((236,236,238), '7500K Blue Daylight')
LIFX_KELVINS[8000] = ((237,240,246), '8000K Blue Overcast')
LIFX_KELVINS[8500] = ((236,241,249), '8500K Blue Water')
LIFX_KELVINS[9000] = ((237,243,252), '9000K Blue Ice')






# LIFX message type constants
DEV_GET_SERVICE         = 2    # Hex = 02
DEV_STATE_SERVICE       = 3    # Hex = 03
DEV_GET_HOST_INFO       = 12   # Hex = 0C
DEV_STATE_HOST_INFO     = 13   # Hex = 0D
DEV_GET_HOST_FIRMWARE   = 14   # Hex = 0E
DEV_STATE_HOST_FIRMWARE = 15   # Hex = 0F
DEV_GET_WIFI_INFO       = 16   # Hex = 10
DEV_STATE_WIFI_INFO     = 17   # Hex = 11
DEV_GET_WIFI_FIRMWARE   = 18   # Hex = 12
DEV_STATE_WIFI_FIRMWARE = 19   # Hex = 13
DEV_GET_POWER           = 20   # Hex = 14
DEV_SET_POWER           = 21   # Hex = 15
DEV_STATE_POWER         = 22   # Hex = 16
DEV_GET_LABEL           = 23   # Hex = 17
DEV_SET_LABEL           = 24   # Hex = 18
DEV_STATE_LABEL         = 25   # Hex = 19
DEV_GET_VERSION         = 32   # Hex = 20
DEV_STATE_VERSION       = 33   # Hex = 21
DEV_GET_INFO            = 34   # Hex = 22
DEV_STATE_INFO          = 35   # Hex = 23
DEV_ACKNOWLEDGEMENT     = 45   # Hex = 2D
DEV_GET_LOCATION        = 48   # Hex = 30
DEV_STATE_LOCATION      = 50   # Hex = 32
DEV_GET_GROUP           = 51   # Hex = 33
DEV_STATE_GROUP         = 53   # Hex = 35
DEV_ECHO_REQUEST        = 58   # Hex = 3A
DEV_ECHO_RESPONSE       = 59   # Hex = 3B
LIGHT_GET                = 101  # Hex = 65
LIGHT_SET_COLOR          = 102  # Hex = 66
LIGHT_SET_WAVEFORM       = 103  # Hex = 67 *** Unofficial ***    
LIGHT_STATE              = 107  # Hex = 6B
LIGHT_GET_POWER          = 116  # Hex = 74
LIGHT_SET_POWER          = 117  # Hex = 75
LIGHT_STATE_POWER        = 118  # Hex = 76
LIGHT_GET_INFRARED       = 120  # Hex = 78
LIGHT_STATE_INFRARED     = 121  # Hex = 79
LIGHT_SET_INFRARED       = 122  # Hex = 7A
MZ_SET_COLOR_ZONES      = 501  # Hex = 1F5
MZ_GET_COLOR_ZONES      = 502  # Hex = 1F6
MZ_STATE_ZONE           = 503  # Hex = 1F7 
MZ_STATE_MULTI_ZONE     = 506  # Hex = 1FA

# LIFX Message Format Dictionary 
messageTypeDict = {}
messageTypeDict[DEV_GET_SERVICE]         = {'name':'GetService',        'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_SERVICE]       = {'name':'StateService',      'payloadLength':5,  'resRequired': '0'}
messageTypeDict[DEV_GET_HOST_INFO]       = {'name':'GetHostInfo',       'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_HOST_INFO]     = {'name':'StateHostInfo',     'payloadLength':14, 'resRequired': '0'}
messageTypeDict[DEV_GET_HOST_FIRMWARE]   = {'name':'GetHostFirmware',   'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_HOST_FIRMWARE] = {'name':'StateHostFirmware', 'payloadLength':20, 'resRequired': '0'}
messageTypeDict[DEV_GET_WIFI_INFO]       = {'name':'GetWifiInfo',       'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_WIFI_INFO]     = {'name':'StateWifiInfo',     'payloadLength':16, 'resRequired': '0'}
messageTypeDict[DEV_GET_WIFI_FIRMWARE]   = {'name':'GetWifiFirmware',   'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_WIFI_FIRMWARE] = {'name':'StateWifiFirmware', 'payloadLength':20, 'resRequired': '0'}
messageTypeDict[DEV_GET_POWER]           = {'name':'GetPower',          'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_SET_POWER]           = {'name':'SetPower',          'payloadLength':2,  'resRequired': '1'}
messageTypeDict[DEV_STATE_POWER]         = {'name':'StatePower',        'payloadLength':2,  'resRequired': '0'}
messageTypeDict[DEV_GET_LABEL]           = {'name':'GetLabel',          'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_SET_LABEL]           = {'name':'SetLabel',          'payloadLength':4,  'resRequired': '1'}
messageTypeDict[DEV_STATE_LABEL]         = {'name':'StateLabel',        'payloadLength':32, 'resRequired': '0'}
messageTypeDict[DEV_GET_VERSION]         = {'name':'GetVersion',        'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_VERSION]       = {'name':'StateVersion',      'payloadLength':12, 'resRequired': '0'}
messageTypeDict[DEV_GET_INFO]            = {'name':'GetInfo',           'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_INFO]          = {'name':'StateInfo',         'payloadLength':24, 'resRequired': '0'}
messageTypeDict[DEV_ACKNOWLEDGEMENT]     = {'name':'Acknowledgement',   'payloadLength':0,  'resRequired': '0'}  ### Is this corect 2016-Nov-19
messageTypeDict[DEV_GET_LOCATION]        = {'name':'GetLocation',       'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_LOCATION]      = {'name':'StateLocatiom',     'payloadLength':56, 'resRequired': '0'}
messageTypeDict[DEV_GET_GROUP]           = {'name':'GetGroup',          'payloadLength':0,  'resRequired': '0'}
messageTypeDict[DEV_STATE_GROUP]         = {'name':'StateGroup',        'payloadLength':56, 'resRequired': '0'}
messageTypeDict[DEV_ECHO_REQUEST]        = {'name':'EchoRequest',       'payloadLength':64, 'resRequired': '0'}
messageTypeDict[DEV_ECHO_RESPONSE]       = {'name':'EchoResponse',      'payloadLength':64, 'resRequired': '0'}
messageTypeDict[LIGHT_GET]               = {'name':'Get',               'payloadLength':0,  'resRequired': '0'}
messageTypeDict[LIGHT_SET_COLOR]         = {'name':'SetColor',          'payloadLength':13, 'resRequired': '1'}
messageTypeDict[LIGHT_SET_WAVEFORM]      = {'name':'SetWaveform',       'payloadLength':0,  'resRequired': '1'}
messageTypeDict[LIGHT_STATE]             = {'name':'State',             'payloadLength':20, 'resRequired': '0'}
messageTypeDict[LIGHT_GET_POWER]         = {'name':'GetPower',          'payloadLength':0,  'resRequired': '0'}
messageTypeDict[LIGHT_SET_POWER]         = {'name':'SetPower',          'payloadLength':6,  'resRequired': '1'}
messageTypeDict[LIGHT_STATE_POWER]       = {'name':'StatePower',        'payloadLength':2,  'resRequired': '0'}
messageTypeDict[LIGHT_GET_INFRARED]      = {'name':'GetInfrared',       'payloadLength':0,  'resRequired': '0'}
messageTypeDict[LIGHT_STATE_INFRARED]    = {'name':'StateInfrared',     'payloadLength':2,  'resRequired': '0'}
messageTypeDict[LIGHT_SET_INFRARED]      = {'name':'SetInfrared',       'payloadLength':2,  'resRequired': '1'}
messageTypeDict[MZ_SET_COLOR_ZONES]      = {'name':'SetColorZones',     'payloadLength':15, 'resRequired': '1'}
messageTypeDict[MZ_GET_COLOR_ZONES]      = {'name':'GetColorZones',     'payloadLength':2,  'resRequired': '0'}
messageTypeDict[MZ_STATE_ZONE]           = {'name':'StateZone',         'payloadLength':10, 'resRequired': '0'}
messageTypeDict[MZ_STATE_MULTI_ZONE]     = {'name':'StateMultiZone',    'payloadLength':66, 'resRequired': '0'}