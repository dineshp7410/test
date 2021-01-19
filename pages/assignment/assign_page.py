import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import utilities.configReader as readFile

class AssignmentPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    employeeName = "//label[text()='Employee Name']/..//input"
    summary = "//span[text()='Write a summary about the employee.']/..//textarea"
    department = "//label[text()='Department']/following-sibling::span//select"
    salary = "//label[text()='Salary']/..//input"
    addLat = "//label[contains(text(),'Lat')]/input"
    addLog = "//label[contains(text(),'Long')]/input"
    workLocation = "//label[text()='Work Location']/following-sibling::span//select"
    dateJoining = "//label[text()='Date of Joining']/following-sibling::span//input"
    employeeStatus = "//label[text()='Yes']/..//input[1]"
    cubicleLength = "(//span[@data-validate='measurement']/input)[1]"
    cubicleLengthUnit = "(//span[@data-validate='measurement']/select)[1]"
    cubicleWidth = "(//span[@data-validate='measurement']/input)[2]"
    cubicleWidthUnit = "(//span[@data-validate='measurement']/select)[2]"
    cubicleColor = "//span[text()='Employee Details']/following-sibling::span//div[@class='TableCell TableCell--edit-mode']//input"

    carDetails1_Brand = "((//span[text()='Car Details']/following-sibling::span//tr)[2]//td//input)[1]"
    carDetails1_Model = "((//span[text()='Car Details']/following-sibling::span//tr)[2]//td//input)[2]"
    carDetails1_Year = "((//span[text()='Car Details']/following-sibling::span//tr)[2]//td//input)[3]"
    carDetails1_Trim = "((//span[text()='Car Details']/following-sibling::span//tr)[2]//td//input)[4]"
    carDetails1_Colour = "((//span[text()='Car Details']/following-sibling::span//tr)[2]//td//input)[5]"
    carDetails1_LicenseNo = "((//span[text()='Car Details']/following-sibling::span//tr)[2]//td//input)[6]"

    carDetails2_Brand = "((//span[text()='Car Details']/following-sibling::span//tr)[3]//td//input)[1]"
    carDetails2_Model = "((//span[text()='Car Details']/following-sibling::span//tr)[3]//td//input)[2]"
    carDetails2_Year = "((//span[text()='Car Details']/following-sibling::span//tr)[3]//td//input)[3]"
    carDetails2_Trim = "((//span[text()='Car Details']/following-sibling::span//tr)[3]//td//input)[4]"
    carDetails2_Colour = "((//span[text()='Car Details']/following-sibling::span//tr)[3]//td//input)[5]"
    carDetails2_LicenseNo = "((//span[text()='Car Details']/following-sibling::span//tr)[3]//td//input)[6]"

    carDetails3_Brand = "((//span[text()='Car Details']/following-sibling::span//tr)[4]//td//input)[1]"
    carDetails3_Model = "((//span[text()='Car Details']/following-sibling::span//tr)[4]//td//input)[2]"
    carDetails3_Year = "((//span[text()='Car Details']/following-sibling::span//tr)[4]//td//input)[3]"
    carDetails3_Trim = "((//span[text()='Car Details']/following-sibling::span//tr)[4]//td//input)[4]"
    carDetails3_Colour = "((//span[text()='Car Details']/following-sibling::span//tr)[4]//td//input)[5]"
    carDetails3_LicenseNo = "((//span[text()='Car Details']/following-sibling::span//tr)[4]//td//input)[6]"

    submitButton = "//button[text() = 'Submit']"

    submittedForm_EmployeeNameHeader = "//h1"
    submittedForm_EmployeeName = "//span[text()='Employee Name']/following-sibling::span"
    submittedForm_Summary="//span[text()='Summary']/following-sibling::span"
    submittedForm_Department="//span[text()='Department']/following-sibling::span"
    submittedForm_Salary="//span[text()='Salary']/following-sibling::span"
    submittedForm_WorkLocation="//span[text()='Work Location']/following-sibling::span"
    submittedForm_Joining="//span[text()='Date of Joining']/following-sibling::span"
    submittedForm_EmployeeStatus="//span[text()='Is the employee still active?']/following-sibling::span"
    submittedForm_Cubicle_length = "(//span[text()='Employee Details']/following-sibling::span//div[contains(@class,'TableCell--measurement')])[1]"
    submittedForm_Cubicle_Width = "(//span[text()='Employee Details']/following-sibling::span//div[contains(@class,'TableCell--measurement')])[2]"
    submittedForm_Address = "//span[text()='Address']/following-sibling::span"
    ############################
    ### Element Interactions ###
    ############################

    def launchApplication(self):
        self.launchUrl(readFile.readConfigData("Application","url"))

    def fillForm(self):
        self.waitForElement(locator=self.employeeName,locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails","EmployeeName"),locator=self.employeeName,locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "Summary"), locator=self.summary,
                      locatorType="xpath")
        self.selectBy(locator=self.department, locatorType="xpath", optionType="Visible Text",value=readFile.readConfigData("UserDetails", "Department"))
        self.sendKeys(readFile.readConfigData("UserDetails", "Salary"), locator=self.salary,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "AddressLat"), locator=self.addLat,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "AddressLog"), locator=self.addLog,
                      locatorType="xpath")
        self.selectBy(locator=self.workLocation, locatorType="xpath", optionType="Visible Text",
                      value=readFile.readConfigData("UserDetails", "WorkLocation"))
        self.sendKeys(readFile.readConfigData("UserDetails", "JoiningDate"), locator=self.dateJoining,
                      locatorType="xpath")
        self.elementClick(locator=self.employeeStatus,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CubicleLength"), locator=self.cubicleLength,
                      locatorType="xpath")
        self.selectBy(locator=self.cubicleLengthUnit, locatorType="xpath", optionType="Visible Text",
                      value=readFile.readConfigData("UserDetails", "CubicleLengthUnit"))
        self.sendKeys(readFile.readConfigData("UserDetails", "CubicleWidth"), locator=self.cubicleWidth,
                      locatorType="xpath")
        self.selectBy(locator=self.cubicleWidthUnit, locatorType="xpath", optionType="Visible Text",
                      value=readFile.readConfigData("UserDetails", "CubicleWidthUnit"))
        self.sendKeys(readFile.readConfigData("UserDetails", "CubicleColor"), locator=self.cubicleColor,
                      locatorType="xpath")
        #Car Details1
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails1Brand"), locator=self.carDetails1_Brand,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails1Model"), locator=self.carDetails1_Model,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails1Year"), locator=self.carDetails1_Year,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails1Trim"), locator=self.carDetails1_Trim,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails1Colour"), locator=self.carDetails1_Colour,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails1License"), locator=self.carDetails1_LicenseNo,
                      locatorType="xpath")
        #Car Details2
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails2Brand"), locator=self.carDetails2_Brand,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails2Model"), locator=self.carDetails2_Model,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails2Year"), locator=self.carDetails2_Year,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails2Trim"), locator=self.carDetails2_Trim,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails2Colour"), locator=self.carDetails2_Colour,
                      locatorType="xpath")
        self.sendKeys(readFile.readConfigData("UserDetails", "CarDetails2License"), locator=self.carDetails2_LicenseNo,
                      locatorType="xpath")

    def submitForm(self):
        self.elementClick(locator=self.submitButton,
                      locatorType="xpath")

    def verifyFormSubmittedLink(self):
        assert self.getCurrentUrl() == readFile.readConfigData("UserDetails", "SubmittedFormLink")

    def verifyDataEnteredMatches(self):
        self.verifyEmployeeNameMatches()
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")
        assert self.getText(locator=self.employeeNameHeader, locatorType="xpath") == readFile.readConfigData(
            "UserDetails", "EmployeeName")

    def verifyEmployeeNameMatches(self):
        assert self.getText(locator=self.submittedForm_EmployeeNameHeader,locatorType="xpath") == readFile.readConfigData("UserDetails", "EmployeeName")

    def verifyAddressMatches(self):
        address = self.getText(locator=self.submittedForm_Address,locatorType="xpath")
        assert readFile.readConfigData("UserDetails", "AddressLat") in address
        assert readFile.readConfigData("UserDetails", "AddressLog") in address


