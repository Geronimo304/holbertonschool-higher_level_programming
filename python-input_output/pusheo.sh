#!/bin/bash

# Add all changes
git add .

# Ask for a commit message
read -p "Enter commit message: " commit_message

# Commit changes
git commit -m "$commit_message"

# Push to current branch
git push origin "$(git branch --show-current)"

echo "Changes have been pushed successfully!"