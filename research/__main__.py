from fetch.fetch_projects import run as fetchProjects
# from fetch.fetch_funders import FetchFunders
import argparse

def main():
    parser = argparse.ArgumentParser(description='Options Research')
    parser.add_argument('fetch', type=str, help='[fetch:projects, fetch:funders]')

    args = parser.parse_args()
    if args.fetch == 'fetch:projects':
        fetchProjects()

if __name__ == '__main__': 
    main()