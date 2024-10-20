import machine, onewire, ds18x20, time
ds_pin = machine.Pin(0)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
#print('Found DS18B20 : ', roms)
print(roms)
time.sleep(10)
while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
      temperature = ds_sensor.read_temp(rom)
      print("Temp",end =' ')
      print(temperature)
      time.sleep(2)

