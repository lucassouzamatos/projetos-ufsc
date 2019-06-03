from fetch.fetch_projects import run as fetchProjects
from fetch.fetch_departments import run as fetchDepartments
from fetch.fetch_funders import run as fetchFunders
import argparse

"""
    Commands by cli:
    
    fetch:projects
    fetch:funders
    fetch:departments
"""
def main():
    parser = argparse.ArgumentParser(description='Options Research')
    parser.add_argument('fetch', type=str, help='[fetch:projects, fetch:funders, fetch:departments]')

    args = parser.parse_args()
    if args.fetch == 'fetch:projects':
        fetchProjects()
    if args.fetch == 'fetch:departments':
        fetchDepartments()
    if args.fetch == 'fetch:funders':
        fetchFunders()

if __name__ == '__main__': 
    main()