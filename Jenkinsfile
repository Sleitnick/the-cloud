pipeline {
	agent {
		docker {
			image 'python:3.10-slim-bullseye'
			args '-v /tmp:/tmp'
		}
	}
	environment {
		DEV_PID = '7795117711'
		DEV_UID = '3020561179'
		QA_PID = '7795118564'
		QA_UID = '3020561179'
		STAGING_PID = '7795119762'
		STAGING_UID = '3020561179'
		PROD_PID = '7794562029'
		PROD_UID = '3020561179'
		AUTH_COOKIE = credentials('auth-cookie')
		AUTH_KEY = credentials('auth-key')
	}
	stages {
		stage('Deploy Dev -> QA') {
			input {
				message "Deploy to QA?"
				ok "Yes"
			}
			steps {
				sh 'pip install -r requirements.txt --user'
				sh 'python fetch_place.py dev.rbxl "$DEV_PID" "$AUTH_COOKIE"'
			}
			post {
				success {
					archiveArtifacts artifacts: dev.rbxl
				}
			}
		}
		stage('Deploy QA -> Staging') {
			input {
				message "Deploy to Staging?"
				ok "Yes"
			}
			steps {
				echo "Deploying"
			}
		}
	}
}