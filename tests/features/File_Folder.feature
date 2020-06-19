# Created by sgoel at 17/06/2020
Feature: SearchFiles and Folders
  Tests that validate search criteria


  Scenario: Validate that the CSV has the correct columns
    Given I open the application
    When I run search according to mission statement
    Then I validate that the search output csv file has the following attributes "Folder Path,File Name,Creation Date,Modified date,Date Accessed"


  Scenario Outline: Validate that the CSV has the correct search results
    Given I open the application
    When I search for <File_a> , <File_b> , <Dir_a> and <Dir_b>
    Then I validate that the search output csv file has the following text "<Text>"

    Examples:
      | File_a   | File_b | Dir_a    | Dir_b   | Text                             |
      | XT.ec    | !!!!!! | XT.ec    | !!!!!!! | C:\Windows\addins\FXSEXT.ecf     |
      | AcGenral | !!!!!! | AcGenral | !!!!!!  | C:\Windows\SysWOW64\AcGenral.dll |
