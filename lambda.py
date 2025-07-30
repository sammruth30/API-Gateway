import json

def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "Guest")
    message = f"Hello, {name}! Welcome to the API Gateway demo!"
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",     # Allow all origins (CORS)
            "Access-Control-Allow-Methods": "GET", # Allowed methods
            "Access-Control-Allow-Headers": "*"    # Allowed headers
        },
        "body": json.dumps({"message": message})  # Return JSON string
    }
