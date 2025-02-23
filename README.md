# CI/CD INTEGRATION

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : MOUMONI ROY

*INTERN ID* : CT08MZR

*DOMAIN* : AUTOMATION TESTING

*DURATION* : 4 WEEKS

*MENTOR* :  NEELA SANTOSH

# CI/CD Pipeline for Flask API

## 📌 Task Overview
This project integrates **automated tests** into a **CI/CD pipeline** using **GitHub Actions**. The pipeline ensures that the Flask API is tested after every code change, improving stability and reliability while reducing manual testing efforts.  

## 🚀 Solution  
The **GitHub Actions** workflow follows these steps:  

1. **Trigger Conditions**  
   - The pipeline runs on **push** and **pull request** events to the `main` branch.  

2. **Setup Environment**  
   - Runs on **Ubuntu-latest**  
   - Installs **Python 3.12** and dependencies from `requirements.txt`  

3. **Start Flask API**  
   - The Flask app (`app.py`) is launched before running tests.  
   - A short delay ensures the server is running before tests execute.  

4. **Run Automated Tests**  
   - Uses **pytest** to execute `test_app.py`.  
   - Generates test reports in **JUnit XML format (`results_ci.xml`)**.  

5. **Upload Test Results**  
   - Test results are saved as GitHub **artifacts** for easy review.  

This ensures that only **tested and validated code** gets merged into the repository.  

## ✅ Test Execution and Results  

The test suite consists of three main test cases:  

| **Test Case**         | **Status** |
|----------------------|-----------|
| `test_home`         | ✅ Passed  |
| `test_add`          | ✅ Passed  |
| `test_invalid_input`| ✅ Passed  |

- **Total Tests:** 3  
- **Failures:** 0  
- **Errors:** 0  
- **Skipped:** 0  
- **Execution Time:** 0.099 seconds  

![Image](https://github.com/user-attachments/assets/a4440113-e119-48ac-952d-632d30929d7a)

## 🛠 Technologies Used  
- **Flask** (Python Web Framework)  
- **GitHub Actions** (CI/CD Automation)  
- **pytest** (Testing Framework)  
- **JUnit XML Reports** (Test Result Storage)  

## 🎯 Outcome & Benefits  
✅ **Automated Testing:** Ensures API stability after every change.  
✅ **Continuous Integration:** Code is tested before merging.  
✅ **Structured Test Reports:** Easy debugging via `results_ci.xml`.  

This pipeline improves **software reliability** and supports **continuous deployment** with structured automation. 🚀  
