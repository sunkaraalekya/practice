def TakeScreenshot(driver,name):
    driver.get_screenshot_as_file("/Users/alekya/pyworkspace/Upload/Screenshot" +name+".png")
