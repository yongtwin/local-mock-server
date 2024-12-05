from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/matching', methods=['POST'])
def log_post_request():
    # Print request method and path
    print(f"Received POST request to: {request.path}")
    
    # Print request headers
    print("Request Headers:")
    for header, value in request.headers:
        print(f"{header}: {value}")
    
    # Print request body
    print("\nRequest Body:")
    print(request.get_data(as_text=True))
    
    # Print JSON body if it exists
    try:
        json_data = request.get_json()
        print("\nJSON Body:")
        print(json_data)
    except Exception:
        pass
    
    # Print form data if it exists
    if request.form:
        print("\nForm Data:")
        for key, value in request.form.items():
            print(f"{key}: {value}")
    
    # Return a simple response
    return jsonify({"status": "received", "message": "POST request logged successfully"}), 200

if __name__ == '__main__':
    print("Server started. Listening for POST requests on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=8888)