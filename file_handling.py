import json
import csv

matches = [
    {
        'Team A': 'Portugal',
        'Team B': 'Spain',
        'Score A': 1,
        'Score B': 1,
        'Date': '2024-04-15'
    },
    {
        'Team A': 'Germany',
        'Team B': 'France',
        'Score A': 1,
        'Score B': 3,
        'Date': '2024-04-21'
    }
]

with open('new_matches.csv', 'w') as file:
    writer = csv.DictWriter(file, matches[0].keys())
    writer.writeheader()
    writer.writerows(matches)