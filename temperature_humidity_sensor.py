import machine  # type: ignore
import utime as time  # type: ignore
import dht  # type: ignore

# DHT11センサーのピン番号を指定
dht_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

# DHT11センサーを初期化
sensor = dht.DHT11(dht_pin)

try:
    time.sleep(3)

    while True:
        try:
            # 温度と湿度を測定
            sensor.measure()
            temp = sensor.temperature()  # 温度を取得
            humidity = sensor.humidity()  # 湿度を取得

            string = f"Temperature: {temp}degree\nHumidity: {humidity}%"
            print(string)
            time.sleep(4)

        except OSError as e:
            if e.args[0] == 110:  # ETIMEDOUT
                print("Timeout occurred. Retrying...")
                time.sleep(1)
            else:
                print("An OSError occurred:", str(e))

        except Exception as e:
            print("An unexpected error occurred:", str(e))

except KeyboardInterrupt:
    print("\nProgram interrupted by user")
