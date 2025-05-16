from flask import Flask, render_template, jsonify
import speedtest
import threading
import time

app = Flask(__name__)

# Global variables to store speed test results
speed_results = {
    'download': None,
    'upload': None,
    'ping': None,
    'status': 'idle'
}

def run_speed_test():
    global speed_results
    try:
        speed_results['status'] = 'running'
        st = speedtest.Speedtest()
        
        # Get best server
        st.get_best_server()
        
        # Test download speed
        speed_results['download'] = round(st.download() / 1_000_000, 2)  # Convert to Mbps
        
        # Test upload speed
        speed_results['upload'] = round(st.upload() / 1_000_000, 2)  # Convert to Mbps
        
        # Get ping
        speed_results['ping'] = round(st.results.ping, 2)
        
        speed_results['status'] = 'completed'
    except Exception as e:
        speed_results['status'] = 'error'
        print(f"Error during speed test: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_test')
def start_test():
    global speed_results
    if speed_results['status'] == 'running':
        return jsonify({'status': 'already_running'})
    
    # Reset results
    speed_results = {
        'download': None,
        'upload': None,
        'ping': None,
        'status': 'running'
    }
    
    # Start speed test in a separate thread
    thread = threading.Thread(target=run_speed_test)
    thread.daemon = True
    thread.start()
    
    return jsonify({'status': 'started'})

@app.route('/get_results')
def get_results():
    return jsonify(speed_results)

if __name__ == '__main__':
    app.run(debug=True) 