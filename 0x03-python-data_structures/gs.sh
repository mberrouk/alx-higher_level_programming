#!/bin/bash

# Retrieve GitHub username and token from environment variables
GITHUB_USERNAME=$GUSER
GITHUB_TOKEN=$GTOK

# Construct the repository URL with the token
REPO_URL="https://$GITHUB_USERNAME:$GITHUB_TOKEN@github.com/mberrouk/alx-higher_level_programming.git"

# Change to your project directory
cd .

# Add all changes and commit with a message
git add .
read -p "Enter commit message: " commit_message
git commit -m "$commit_message"

# Push to the remote repository using the constructed URL
git push "$REPO_URL" master  # Change 'main' to 'master' if you're using the older branch name

echo "Push to GitHub completed!"

