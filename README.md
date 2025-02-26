# github-dvc-practice
Assignment for practicing GitHub and DVC foundations on system

'''
bash

1. Created repo github-dvc-practice
2. Cloned repo github-dvc-practice locally
3. Created python script
4. Commited and pushed changes
    1. git add analysis.py
    2. git commit -m "Add analysis script"
    3. git push origin main 
5. Created a new feature branch and modified the code
    1. git checkout -b feature/greeting
    2. git add analysis.py
    3. git commit -m "Add farewell function"
    4. git push origin feature/greeting
    5. Pull request and merge done in github online - Learning: Everytime there is a change/add new feature we need to create a pull request and merge it into main branch and can then delete the feature 
    6. We can also merge via CLI by following the steps below
        1. Clone the repository or update your local repository with the latest changes.
                git pull origin main
        2. Switch to the base branch of the pull request.
                git checkout main
        3. Merge the head branch into the base branch.
                git merge feature/greeting
        4. Push the changes.
                git push -u origin main
6. Installed DVC for the first time - pip install dvc was throwing issue thats why installed dvc via downloading executable file from online which added to the path variable
7. Initializing DVC on local
    1. dvc init
    2. created a folder dvc remote on local directory and added the remote folder to dvc
    3. dvc remote add -d myremote <location of dvc remote folder>
    4. pushed the DVC config to remote
          git add .dvc/config .dvc/.gitignore // gitignore was present inside .dvc folder
           git commit -m "Configure DVC remote storage"
           git push origin main
    6. Tracked dataset data/sample_data.csv
          dvc add data/sample_data.csv
          git add data/sample_data.csv.dvc .gitignore
          git commit -m "Track sample dataset with DVC"
           git push origin main
    8. Added new row in data and then updated the dvc tracking and commit and pushed the changes
    9. Pushed updated data to remote storage
          dvc push
    10. Created a new folder as Collaborator
    11. Cloned the repo
      git clone https://github.com/abhiseknayak169/github-dvc-practice.git collaborator
    12. Pull the lastest changes
    13. Pull the latest data changes using DVC
    14. Made changes according to the requirement
    15. Staged, Commit and Pushed changes

'''
