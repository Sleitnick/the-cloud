pipeline {
	agent any
	stages {
		stage('Deploy Dev -> QA') {
			input {
				message "Deploy to QA?"
				ok "Yes"
			}
			steps {
				echo "Deploying"
			}
		}
		stage('Deploy QA -> Staging') {
			input {
				message "Deploy to QA?"
				ok "Yes"
			}
			steps {
				echo "Deploying"
			}
		}
	}
}