Feature: Car credit and insurance calculator API



Scenario Outline: Buana car credit calculator

    Given I pick <price> as price AJAX parameter
        And I pick <year> as year AJAX parameter
        And I pick <brand> as brand AJAX parameter
        And I pick <duration> as duration AJAX parameter
    When I submit an AJAX request with action credit_buana
    Then I receive a JSON response
        And JSON field downPayment is equal to <down_payment>
        And JSON field installment is equal to <installment>
    Examples:
        | price     | year | brand  | duration | down_payment  | installment  |
        | 100000000 | 2010 | Toyota |        4 |  Rp24.985.000 |  Rp2.543.392 |
        | 150000000 | 2011 | Honda  |        3 |  Rp35.785.000 |  Rp4.445.493 |
        | 250000000 | 2012 | Nissan |        2 |  Rp57.385.000 | Rp10.106.075 |
        | 350000000 | 2013 | Suzuki |        1 |  Rp78.985.000 | Rp25.736.290 |
        | 550000000 | 2014 | Mazda  |        2 | Rp122.185.000 | Rp22.211.292 |
        | 650000000 | 2015 | BMW    |        3 | Rp175.635.000 | Rp18.128.974 |
        | 850000000 | 2016 | Ford   |        4 | Rp228.635.000 | Rp20.026.992 |



Scenario Outline: Oto car credit calculator

    Given I pick <price> as price AJAX parameter
        And I pick <year> as year AJAX parameter
        And I pick <brand> as brand AJAX parameter
        And I pick <duration> as duration AJAX parameter
    When I submit an AJAX request with action credit_oto
    Then I receive a JSON response
        And JSON field downPayment is equal to <down_payment>
        And JSON field installment is equal to <installment>
    Examples:
        | price     | year | brand  | duration | down_payment  | installment  |
        | 100000000 | 2010 | Toyota |        4 |  Rp24.405.000 |  Rp2.495.208 |
        | 150000000 | 2011 | Honda  |        3 |  Rp35.205.000 |  Rp4.379.421 |
        | 250000000 | 2012 | Nissan |        2 |  Rp56.805.000 |  Rp9.988.563 |
        | 350000000 | 2013 | Suzuki |        1 |  Rp78.405.000 | Rp25.584.074 |
        | 550000000 | 2014 | Mazda  |        2 | Rp121.605.000 | Rp21.953.021 |
        | 650000000 | 2015 | BMW    |        3 | Rp143.205.000 | Rp19.019.429 |
        | 850000000 | 2016 | Ford   |        4 | Rp186.405.000 | Rp20.918.783 |



Scenario Outline: ABDA car insurance calculator

    Given I pick <price> as price AJAX parameter
        And I pick <year> as year AJAX parameter
    When I submit an AJAX request with action insurance_abda
    Then I receive a plain text response <premium>
    Examples:
        | price     | year | premium     |
        | 100000000 | 2011 | Rp3.790.500 |
        | 150000000 | 2012 | Rp3.892.500 |
        | 250000000 | 2013 | Rp4.487.500 |
        | 350000000 | 2014 | Rp6.282.500 |



Scenario Outline: Autocillin car insurance calculator

    Given I pick <price> as price AJAX parameter
        And I pick <year> as year AJAX parameter
    When I submit an AJAX request with action insurance_autocillin
    Then I receive a plain text response <premium>
    Examples:
        | price     | year | premium     |
        | 100000000 | 2011 | Rp3.675.000 |
        | 150000000 | 2012 | Rp4.050.000 |
        | 250000000 | 2013 | Rp4.825.000 |
        | 350000000 | 2014 | Rp6.755.000 |
