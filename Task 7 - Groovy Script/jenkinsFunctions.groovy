def checkoutCode(String repoUrl, String branch) {
    checkout([$class: 'GitSCM', branches: [[name: branch]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: repoUrl]]])
}

def buildProject() {
    echo 'Building'
    bat 'pip install -r ./Task 7 - Groovy Script/requirements.txt --break-system-packages'
}

def runTests() {
    echo 'Test'
    bat 'python3 ./Task 7 - Groovy Script/test.py'
}

def deployApplication() {
    echo 'Deploying'
}

return this