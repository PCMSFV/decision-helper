#!/usr/bin/env python3
"""
🎯 Decision Helper - A simple tool for choice paralysis
Helps you make decisions by randomly selecting from your options
"""

import random
import sys

def decide(options, weights=None):
    """
    Make a decision from the given options.
    
    Args:
        options: List of choices to select from
        weights: Optional list of weights for weighted random selection
    
    Returns:
        The selected option
    """
    if not options:
        return "Please provide at least one option!"
    
    if len(options) == 1:
        return f"Well, there's only one choice: {options[0]}"
    
    if weights:
        if len(weights) != len(options):
            return "Error: Number of weights must match number of options"
        choice = random.choices(options, weights=weights, k=1)[0]
    else:
        choice = random.choice(options)
    
    return f" The universe says: {choice}"

def main():
    """Main function to run the decision helper."""
    print("🎯 Decision Helper - Beat choice paralysis!\n")
    
    if len(sys.argv) > 1:
        # Options provided via command line
        options = sys.argv[1:]
        print(f"Options: {', '.join(options)}")
        print(decide(options))
    else:
        # Interactive mode
        print("Enter your options (one per line). Empty line to finish:")
        options = []
        while True:
            opt = input(f"Option {len(options)+1}: ").strip()
            if not opt:
                break
            options.append(opt)
        
        if options:
            print(f"\n{decide(options)}")
        else:
            print("\nNo options provided. Try again!")

if __name__ == "__main__":
    main()























































