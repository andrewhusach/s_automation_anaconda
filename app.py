from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! Checing autodeployment....'

@app.route('/github-deploy', methods=['POST'])
def github_deploy():
    try:
        # Change to your project's directory
        os.chdir('/home/agusach/mydir')

        # Pull the latest changes from your GitHub repository
        subprocess.check_call(['git', 'pull'])

        # Touch the WSGI file to reload the web application
        subprocess.check_call(['touch', '/var/www/agusach_pythonanywhere_com_wsgi.py'])

        return 'Deployment script executed successfully.', 200
    except subprocess.CalledProcessError as e:
        # If an error occurs during the subprocess calls, log it or print it.
        # Consider logging the error to a file for production use
        print(f"Error occurred: {e}")
        return 'Failed to execute deployment script.', 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)
