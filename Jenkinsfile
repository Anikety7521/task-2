pipeline {
    
    agent any
    
    stages {
        stage("SCM") {
            steps {
                git branch: 'main', url: 'https://github.com/Anikety7521/task-2.git'
            }
        }
        

        stage("installing packages") {
            steps {
                sh 'pip install pytest -y && pip install requests'
            }
        }
        
        stage("run the test") {
            steps {
 
                 sh 'pytest test.py'
'
               }
              
        }
        
   
    
}
