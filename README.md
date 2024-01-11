## UI and API Testing Project using the AutomationExercise Test E-commerce Service

> <a target="_blank" href="https://automationexercise.com/">AutomationExercise</a>

![This is an image](images/screenshots/site_main.png)

### Project features

- Project build in Jenkins
- Execution of UI tests on a remote browser in Selenoid
- Reports with video, screenshot, logs for better debugging
- Comprehensive logging of requests and responses in API tests for better debugging
- Allure reports
- Integration with Allure TestOps
- Integration with Jira
- Test run notifications in Telegram

### List of tests implemented in the project

#### UI

- [x] Login with an existing user account
- [x] Logout from an existing user account
- [x] Creation of a new user account
- [x] Deletion of a user account
- [x] Product search
- [x] Filtering
- [x] End-to-End product purchase

#### API

- [x] Login verification (positive and negative parametrized test)
- [x] Creation of a new user account
- [x] Editing of a user account
- [x] Retrieval of user account information
- [x] Deletion of a user account

### The project is implemented using the following tools:

<p  align="center">
  <code><img width="5%" title="Pycharm" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/pycharm.png"></code>
  <code><img width="5%" title="Python" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/python.png"></code>
  <code><img width="5%" title="Pytest" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/pytest.png"></code>
  <code><img width="5%" title="Selene" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/selene.png"></code>
  <code><img width="5%" title="Selenium" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/github.png"></code>
  <code><img width="5%" title="Jenkins" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/allure.png"></code>
  <code><img width="5%" title="Allure TestOps" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/allure_testops.png"></code>
  <code><img width="5%" title="Telegram" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/jira.png"></code>
<code><img width="5%" title="Telegram" src="https://github.com/shadowkatja/qa_guru_python_8_final_work/blob/master/images/icons/telegram.png"></code>
</p>

### Automated tests are executed on the Jenkins server
> <a target="_blank" href="https://jenkins.autotests.cloud/job/goldinova_qa_guru_final_work/">Ссылка на проект в Jenkins</a>

### Build parameters

* `ENVIRONMENT` - defines the environment for testing, defaults to STAGE
* `COMMENT` - comment to the build
* `BROWSER_VERSION` - desired version of Google Chrome browser, 100 by default

### To execute automated tests in Jenkins:

1. Open the <a target="_blank" href="https://jenkins.autotests.cloud/job/goldinova_qa_guru_final_work/">project</a>
2. Select the `Build with Parameters` option
3. Choose the environment from the ENVIRONMENT dropdown list
4. Enter a comment in the COMMENT field
5. Specify the browser version in the BROWSER_VERSION field (optional)
6. Press the `Build` button

![This is an image](images/screenshots/jenkins.png)

### Viewing results in Allure Report

Viewing overall test launch results

![This is an image](images/screenshots/allure_report_main.png)

Viewing test cases with execution report

![This is an image](images/screenshots/allure_report_cases.png)

### Integration with Allure TestOps

Storing all test cases

![This is an image](images/screenshots/allure_testOPS_testcases.png)

Dashboard with statistics

![This is an image](images/screenshots/allure_testOPS_main.png)

Comprehensive information on launches with attachments

![This is an image](images/screenshots/allure_testOPS_launch.png)

### Integration with Jira

Attached test cases and launches

![This is an image](images/screenshots/jira.png)

### Integration with Telegram

Sending test run reports to Telegram

![This is an image](images/screenshots/telegram.png)

### Video report of test execution demonstrating a product purchase

![report_gif](images/screenshots/video.gif)