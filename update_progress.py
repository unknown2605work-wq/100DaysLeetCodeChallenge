#!/usr/bin/env python3
"""
Automated script to scan LeetCode problem solutions and update progress.csv
Detects new problem files and adds them to the CSV with metadata.
"""

import os
import csv
import re
from datetime import datetime
from pathlib import Path

# Problem difficulty mapping - customize based on your folder structure
DIFFICULTY_MAP = {
    'easy': 'Easy',
    'medium': 'Medium',
    'hard': 'Hard'
}

# Mapping of problem numbers to problem names (add more as needed)
PROBLEM_NAMES = {
    '0001': 'Two Sum',
    '0002': 'Add Two Numbers',
    '0003': 'Longest Substring Without Repeating Characters',
    '0004': 'Median of Two Sorted Arrays',
    '0005': 'Longest Palindromic Substring',
    '0006': 'Zigzag Conversion',
    '0007': 'Reverse Integer',
    '0008': 'String to Integer (atoi)',
    '0009': 'Palindrome Number',
    '0010': 'Regular Expression Matching',
    '0011': 'Container With Most Water',
    '0012': 'Integer to Roman',
    '0013': 'Roman to Integer',
    '0014': 'Longest Common Prefix',
    '0015': 'Three Sum',
    '0020': 'Valid Parentheses',
    '0035': 'Search Insert Position',
    '0048': 'Rotate Image',
    '0058': 'Length of Last Word',
    '0066': 'Plus One',
    '0136': 'Single Number',
    '0217': 'Contains Duplicate',
    '0219': 'Contains Duplicate II',
    '0509': 'Fibonacci Number',
    '0788': 'Rotated Digits',
    '0796': 'Rotate String',
    '1137': 'N-th Tribonacci Number',
}

def parse_problem_number_from_filename(filename):
    """Extract problem number from filename (e.g., '0001_two_sum.py' -> '0001')"""
    match = re.match(r'(\d{4})', filename)
    return match.group(1) if match else None

def get_problem_name(problem_num):
    """Get problem name from mapping or generate from filename"""
    return PROBLEM_NAMES.get(problem_num, f'Problem {problem_num}')

def get_difficulty_from_path(file_path):
    """Extract difficulty from directory path"""
    path_lower = file_path.lower()
    for key, value in DIFFICULTY_MAP.items():
        if key in path_lower:
            return value
    return 'Unknown'

def scan_for_new_problems(csv_path='progress.csv', solutions_dir='./'):
    """Scan directory for solution files and find ones not in CSV"""
    
    # Read existing progress
    existing_problems = set()
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_problems.add(row['Problem Number'].strip())
    
    # Find all solution files (adjust extensions as needed)
    solution_extensions = ('.py', '.java', '.cpp', '.js', '.ts', '.go', '.rs', '.c')
    new_problems = []
    
    for root, dirs, files in os.walk(solutions_dir):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', '.idea']]
        
        for file in files:
            if file.endswith(solution_extensions):
                problem_num = parse_problem_number_from_filename(file)
                
                if problem_num and problem_num not in existing_problems:
                    file_path = os.path.join(root, file)
                    difficulty = get_difficulty_from_path(file_path)
                    problem_name = get_problem_name(problem_num)
                    
                    new_problems.append({
                        'Problem Number': problem_num,
                        'Problem Name': problem_name,
                        'Difficulty': difficulty,
                        'Status': 'Completed',
                        'Date Completed': datetime.now().strftime('%Y-%m-%d'),
                        'Notes': f'File: {file}'
                    })
    
    return new_problems

def update_csv(csv_path='progress.csv', new_problems=None):
    """Add new problems to CSV file"""
    if not new_problems:
        return False
    
    fieldnames = ['Problem Number', 'Problem Name', 'Difficulty', 'Status', 'Date Completed', 'Notes']
    
    # Read existing data
    existing_data = []
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_data = list(reader)
    
    # Combine and sort by problem number
    all_data = existing_data + new_problems
    all_data.sort(key=lambda x: int(x['Problem Number']))
    
    # Write back
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
    
    return True

def main():
    """Main execution"""
    print("🔍 Scanning for new LeetCode problems...")
    
    new_problems = scan_for_new_problems()
    
    if new_problems:
        print(f"\n✅ Found {len(new_problems)} new problem(s):")
        for problem in new_problems:
            print(f"  - {problem['Problem Number']}: {problem['Problem Name']} ({problem['Difficulty']})")
        
        if update_csv(new_problems=new_problems):
            print("\n✨ Successfully updated progress.csv!")
            print(f"📅 Updated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("\n❌ Failed to update CSV")
    else:
        print("\n✓ No new problems found. Your progress.csv is up to date!")

if __name__ == '__main__':
    main()
