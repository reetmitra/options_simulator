#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting Options Simulator Setup and Test Suite${NC}"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo -e "${GREEN}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Create plots directory if it doesn't exist
if [ ! -d "plots" ]; then
    echo -e "${GREEN}Creating plots directory...${NC}"
    mkdir -p plots
fi

# Activate virtual environment
echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

# Install/upgrade pip
echo -e "${GREEN}Upgrading pip...${NC}"
pip install --upgrade pip

# Install requirements
echo -e "${GREEN}Installing requirements...${NC}"
pip install -r requirements.txt

# Install package in development mode
echo -e "${GREEN}Installing package in development mode...${NC}"
pip install -e .

# Run test suite
echo -e "${GREEN}Running test suite...${NC}"
python test_options.py

# Deactivate virtual environment
echo -e "${GREEN}Deactivating virtual environment...${NC}"
deactivate

echo -e "${YELLOW}Setup and testing complete!${NC}" 