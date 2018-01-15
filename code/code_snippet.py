import dht
import time
my_dht = dht.DHT11(machine.Pin(2))

def measure_humidity(outfile, poll_time_s):
    while True:
        my_dht.measure()
        humidity = my_dht.humidity()
        with open(outfile, 'a') as f:
            f.write(str(humidity) + ",")
        print("humidity: ", humidity)
        time.sleep(poll_time_s)
