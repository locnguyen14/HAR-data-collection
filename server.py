def listen_once():
    import matplotlib.pyplot as plt
    import socket
    from collections import defaultdict
    import json

    # Get host from Wireless LAN adapter wi-fi ipv4.
    # Standard loopback interface address (localhost)
    # HOST = socket.gethostbyname(socket.gethostname())
    HOST = '192.168.1.4'
    PORT = 60230  # Port to listen on (non-privileged ports are > 1023)
    print("Listening on " + str(HOST) + ":" + str(PORT))

    x_arr, y_arr, z_arr = [], [], []
    accelerometerDict = defaultdict(list)
    sampling_point = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        fig = plt.figure()
        with conn:
            print('Connected by client with ip address: ', addr)
            while True and sampling_point < 200:
                data = conn.recv(1024)
                if data.decode('utf-8') != "":
                    data = data.decode('utf-8')
                    print("sampling Point {}".format(sampling_point))
                    print(data)
                    split = data.replace(")", "").replace(
                        "(", "").split(",")
                    try:
                        x, y, z = float(split[0]), float(
                            split[1]), float(split[2])
                        accelerometerDict['x'].append(x)
                        accelerometerDict['y'].append(y)
                        accelerometerDict['z'].append(z)
                    except:
                        continue

                    if len(x_arr) > 20:
                        x_arr.pop(0)
                    x_arr.append(x)
                    if len(y_arr) > 20:
                        y_arr.pop(0)
                    y_arr.append(y)
                    if len(z_arr) > 20:
                        z_arr.pop(0)
                    z_arr.append(z)
                    i = list(range(len(x_arr)))
                    plt.clf()
                    # Limit the gyro values to max of +/- 1 because we don't want to destroy the wheel
                    if y < -1:
                        y = -1
                    if y > 1:
                        y = 1
                    if z < -1:
                        z = -1
                    if z > 1:
                        z = 1
                    # line = ""
                    # if y <= 0:
                    #     line += "ACCELERATE %.2f\t" % abs(y)
                    # if y > 0:
                    #     line += "BREAK      %.2f\t" % y
                    # if z <= 0:
                    #     line += "RIGHT %.2f" % z
                    # if z > 0:
                    #     line += "LEFT  %.2f" % abs(z)
                    # print(line)
                    # plt.plot(i, x_arr, 'r-')
                    plt.plot(i, y_arr, 'b-')
                    plt.plot(i, z_arr, 'k-')

                    plt.pause(.02)
                    sampling_point += 1
            conn.close()
        s.close()

    # Dump it to json file
    json_file = json.dumps(accelerometerDict)
    f = open("AccelerometerData.json", "w")
    f.write(json_file)
    f.close()


if __name__ == "__main__":
    listen_once()
