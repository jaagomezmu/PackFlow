#!/bin/bash

echo "Executing curl requests..."

# Get list of customers and their details
echo "Fetching list of customers..."
curl -X GET http://localhost:3000/customers

# Get list of packages and their details
echo "Fetching list of packages..."
curl -X GET http://localhost:3000/packages

# Get list of carriers and their details
echo "Fetching list of carriers..."
curl -X GET http://localhost:3000/carriers

# Update delivery status of a package
echo "Updating delivery status of a package..."
curl -X PUT -H "Content-Type: application/json" -d '{"delivery_status": "In Transit"}' http://localhost:3000/packages/1

echo "Curl requests executed successfully!"
