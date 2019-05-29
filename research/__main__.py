from migrate import Migrate
from fetch.fetch_projects import FetchProjects

def main():
    Migrate('./docs/projetos_.xls')
 
if __name__ == '__main__': 
    main()