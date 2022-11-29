Feature: Events module from BookMyShow

  Scenario Outline: Book an Event
    Given launch chrome browser
    When Open the BookMyShow browser
    Then Choose location
    And Click on Events Button
    And Click on Browser By Venue
    And Choose a Venue
    And Choose an Event
    And Click on book
    And Choose a Location
    And Click on Add
    And Click on Proceed
    And Enter Name "<Name>"
    And Enter Number "<PhoneNo>"
    And Enter Email "<Email>"
    And Click on checkbox1
    And Click on checkbox2
    And Click on submit
    And Click on Login to Proceed
    And Close Browser
      Examples:
      |Name      |PhoneNo   |Email                   |
      | Jyothi   |7995296813|kumbajyothi134@gmail.com|
      | Lavanya  |7995296613|Lavanyapesala134@gmail.com|

