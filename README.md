# Linker Map Summary
Summarizes the size of objects linked into a binary based on the linker map.
This is useful to see the size impact of different portions of code after the
linker has dropped unneeded sections.

## Use
`python2 analyze_map.py firmware.elf.map`

## Example Output
```
/usr/local/Cellar/arm-none-eabi-gcc/20150921/bin/../lib/gcc/arm-none-eabi/4.9.3/../../../../arm-none-eabi/lib/armv6-m//libm.a(lib_a-kf_rem_pio2.o) 1888
build-arduino_zero/py/mpprint.o 1938
build-arduino_zero/py/objset.o 2018
build-arduino_zero/py/obj.o 2038
build-arduino_zero/py/objarray.o 2122
build-arduino_zero/boards/arduino_zero/pins.o 2144
build-arduino_zero/py/objdict.o 2146
build-arduino_zero/py/objlist.o 2210
build-arduino_zero/py/lexer.o 2405
build-arduino_zero/py/objexcept.o 2466
build-arduino_zero/asf/sam0/drivers/usb/stack_interface/usb_device_udd.o 2692
build-arduino_zero/asf/sam0/drivers/usb/usb_sam_d_r/usb.o 3026
build-arduino_zero/py/emitbc.o 3166
build-arduino_zero/py/modbuiltins.o 3219
build-arduino_zero/py/gc.o 3411
build-arduino_zero/py/objtype.o 3579
build-arduino_zero/py/vm.o 4259
build-arduino_zero/py/runtime.o 4627
build-arduino_zero/py/parse.o 4676
build-arduino_zero/py/qstr.o 6589
build-arduino_zero/py/objstr.o 9070
build-arduino_zero/lib/fatfs/ff.o 10777
build-arduino_zero/py/compile.o 11731
```
