def measure_mqtt(poll_time_s, broker_ip, client_id, topic):
    p = MQTTClient(client_id, broker_ip)
    try :
        p.connect()
    except Exception as ex:
        print('exception in measure_mqtt trying to connect to broker ' + str(ex))

    while True:
        humidity = 51
        temp = 13
        try:
            my_dht.measure()
            humidity = my_dht.humidity()
            temp = my_dht.temperature()
        except Exception as ex:
            print('exception in measure function' + str(ex))

        gc.collect()
        temp_topic = topic + '/temp/' + client_id
        humid_topic =  topic + '/humidity/' + client_id
        print('publishing to: ' + temp_topic + '  value: ' + str(temp))
        print('publishing to: ' + humid_topic + '  value: ' + str(humidity))

        try :
            p.publish(temp_topic, str(temp))
            p.publish(humid_topic, str(humidity))
        except Exception as ex:
            print('exception in measure_mqtt publish: ' + str(ex))
            print('retrying connect')
            try :
                p.connect()
            except Exception as ex:
                print('exception in measure_mqtt trying to connect to broker ' + str(ex))

        gc.collect()
        time.sleep(poll_time_s)
