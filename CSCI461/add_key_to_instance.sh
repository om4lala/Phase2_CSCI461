#!/bin/bash
# Script to add SSH public key to EC2 instance
# Run this ON the EC2 instance after SSHing in

PUBLIC_KEY="ssh-ed25519 N9BWtpEgcsW+yUnqtJsrmsEr9iwuEDvGNPFoWp/vWLU="

echo "Setting up SSH key for GitHub Actions..."

# Create .ssh directory if it doesn't exist
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Add public key to authorized_keys (avoid duplicates)
if ! grep -q "$PUBLIC_KEY" ~/.ssh/authorized_keys 2>/dev/null; then
    echo "$PUBLIC_KEY" >> ~/.ssh/authorized_keys
    echo "✅ Public key added to authorized_keys"
else
    echo "⚠️  Public key already exists in authorized_keys"
fi

# Set correct permissions
chmod 600 ~/.ssh/authorized_keys

# Verify
echo ""
echo "Current authorized_keys content:"
cat ~/.ssh/authorized_keys

echo ""
echo "✅ Setup complete! The instance is now ready for GitHub Actions."

