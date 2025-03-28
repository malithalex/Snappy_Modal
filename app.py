# from flask import Flask, request, jsonify
# import base64
# from io import BytesIO
# from PIL import Image
# import torch

# app = Flask(__name__)

# # Dummy model inference function
# def predict_camera_adjustment(image: Image.Image, bbox: dict, state: dict):
#     """
#     Dummy function: Replace this with your actual model inference code.
#     Uses the image, bounding box and state information to predict the optimal camera settings.
    
#     :param image: PIL Image captured from the camera.
#     :param bbox: Dictionary with keys x, y, width, height of the detected object.
#     :param state: Additional state data (if any).
#     :return: A dictionary with predicted camera angle, zoom level, and feedback text.
#     """
#     # For demonstration, simply return dummy values.
#     return {
#         "angle": 15,            # optimal camera angle adjustment in degrees
#         "zoom": 1.2,            # optimal zoom level (multiplier)
#         "feedback": "Your shot is slightly off-center. Try rotating your camera 15° to the right and zoom in a bit for a balanced composition."
#     }

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()
#         if not data or 'image' not in data or 'bbox' not in data:
#             return jsonify({"error": "Missing required fields: 'image' and 'bbox'"}), 400

#         image_base64 = data['image']
#         bbox = data['bbox']  # expected format: { "x": number, "y": number, "width": number, "height": number }
#         state = data.get("state", {})  # optional extra state data

#         # Decode base64 image to PIL Image
#         image_data = base64.b64decode(image_base64)
#         image = Image.open(BytesIO(image_data)).convert("RGB")

#         # Predict camera adjustment settings
#         prediction = predict_camera_adjustment(image, bbox, state)

#         return jsonify({
#             "success": True,
#             "prediction": prediction
#         })
#     except Exception as e:
#         return jsonify({
#             "success": False,
#             "error": str(e)
#         }), 500

# if __name__ == '__main__':
#     # Run on localhost for testing
#     app.run(host='0.0.0.0', port=5000, debug=True)


# from flask import Flask, request, jsonify
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = '/tmp'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get bounding box parameters from form data
#     x = request.form.get('x')
#     y = request.form.get('y')
#     width = request.form.get('width')
#     height = request.form.get('height')
#     timestamp = request.form.get('timestamp')
    
#     # Check if an image was uploaded
#     if 'image' not in request.files:
#         return jsonify({"error": "No image uploaded"}), 400
#     image = request.files['image']
    
#     # Save image temporarily
#     temp_image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
#     image.save(temp_image_path)
    
#     # Dummy prediction: For demonstration, return the received parameters
#     print("Received parameters:")
#     print("x:", x, "y:", y, "width:", width, "height:", height, "timestamp:", timestamp)
#     print("Image saved temporarily at:", temp_image_path)
    
#     # (Your model logic would go here)
    
#     # Clean up the temporary image file after processing
#     os.remove(temp_image_path)
    
#     return jsonify({
#         "prediction": "dummy",
#         "parameters": {"x": x, "y": y, "width": width, "height": height, "timestamp": timestamp}
#     })

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Parse JSON payload from FE
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400

    # Extract parameters from the JSON payload
    x = data.get('x')
    y = data.get('y')
    width = data.get('width')
    height = data.get('height')
    image_path = data.get('imagePath')

    # Check that all required fields are present
    if None in [x, y, width, height, image_path]:
        return jsonify({"error": "Missing one or more required fields: x, y, width, height, imagePath"}), 400

    # Log the received values for debugging
    print("Received JSON payload:")
    print("x:", x, "y:", y, "width:", width, "height:", height, "imagePath:", image_path)

    # Dummy prediction logic
    dummy_prediction = "object_detected"

    # Return the dummy prediction along with the received parameters
    return jsonify({
        "prediction": dummy_prediction,
        "parameters": {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "imagePath": image_path
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

