#!/bin/bash
#cd to your working directory
# Make executable
chmod +x main.py

# Create global command
sudo ln -sf "$(pwd)/main.py" /usr/local/bin/typingtest

echo "Typing tester installed successfully!"
echo "Run it anytime with:"
echo "typingtest"