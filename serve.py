from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        # Handle POST request
        start_cpu_stress()
        return jsonify({'message': 'CPU stress initiated'})

    elif request.method == 'GET':
        # Handle GET request
        private_ip = get_private_ip()
        return jsonify({'private_ip': private_ip})

def start_cpu_stress():
    # Use subprocess.Popen() to run stress_cpu.py in a separate process
    subprocess.Popen(['python3', 'stress_cpu.py'])

def get_private_ip():
    # Use socket.gethostname() to get the private IP address
    myHostName = socket.gethostname()
    print("Name of the localhost is {}".format(myHostName))
    private_ip = socket.gethostbyname(myHostName)
    return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)