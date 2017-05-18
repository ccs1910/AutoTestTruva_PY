Feature: True Value Meter (TVM)



Scenario: Querying list of car brands

    When I submit an AJAX request with action truva_market_get_all_brand
    Then I receive a JSON response containing a list of all car brands



Scenario: Querying list of car models from a random brand

    When I pick a random brand as the brand AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_model
    Then I receive a JSON response containing the list of car models



Scenario Outline: Querying list of car models from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_model
    Then I receive a JSON response containing the list of car models
    Examples:
        | brand    |
        | Toyota   |
        | Honda    |
        | Daihatsu |
        | Nissan   |
        | Ford     |



Scenario Outline: Querying list of car years from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I pick <model> as model AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_year
    Then I receive a JSON response containing the list of car years
    Examples:
        | brand    | model        |
        | Toyota   | Avanza       |
        | Daihatsu | Xenia        |
        | Honda    | Jazz         |
        | Nissan   | Grand Livina |
        | Isuzu    | New Panther  |



Scenario Outline: Querying list of car variants from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I pick <model> as model AJAX parameter
        And I pick <year> as year AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_variant
    Then I receive a JSON response containing the list of car variants
    Examples:
        | brand      | model        | year |
        | Toyota     | Avanza       | 2014 |
        | Toyota     | Avanza       | 2010 |
        | Isuzu      | New Panther  | 2013 |
        | Mitsubishi | Pajero Sport | 2014 |
        | Suzuki     | Ertiga       | 2012 |



Scenario Outline: Querying price range from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I pick <model> as model AJAX parameter
        And I pick <year> as year AJAX parameter
        And I pick <variant> as variant AJAX parameter
        And I submit an AJAX request with action truva_market_get_single_price
    Then I receive a JSON response containing the minimum and maximum price
    Examples:
        | brand      | model                | year | variant           |
        | Toyota     | Avanza               | 2014 | All New Veloz A/T |
        | Honda      | Civic                | 2007 | New 2.0 A/T       |
        | Honda      | Jazz                 | 2013 | RS A/T Facelift   |
        | Toyota     | Fortuner             | 2014 | 2.5 G Diesel TRD  |
        | Toyota     | Kijang Innova Bensin | 2010 | G A/T             |
