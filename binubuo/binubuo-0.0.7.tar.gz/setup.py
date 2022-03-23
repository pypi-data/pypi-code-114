from setuptools import setup, find_packages
from pathlib import Path

readme = """# Binubuo

**Binubuo** is a simple and powerful client to the Binubuo API. The API is used to generate fake or synthetic data that is realistic. Simply import the module, and you are good to go. Start generating your data straight away.

If you do not have an account with Binubuo yet, and you do nothing, the first time you call, a temporary access key will be generated for your session automatically.

```python
>>> from binubuo import binubuo
>>> b = binubuo()
>>> print(b.generate('person', 'full_name'))
Andrew Howard
>>> print(b.generate('finance', 'bank_account_id'))
GE02Pu5783332775138823
>>> print(b.generate('consumer', 'food_item'))
Pumpkin Spice, Atlantic Salmon, 2 Bonless Fillets
>>> print(b.generate('time', 'date'))
1945-02-10T17:37:09Z
```

The **Binubuo** API has more than 150+ real life data generators, across 10+ data domains such as person, finance, computer, investment and many more. For full details on what type
of data Binubuo can generate and uder which domains, you can see the full list here: https://binubuo.com/ords/r/binubuo_ui/binubuo/documentation-generators.

The temporary key gives you the same abilities as a real key does, except that its use is limited to 24 hours. So if you create any datasets they will be deleted after 24 hours, and
your tag history and custom settings will also be removed and reset.

To use **Binubuo** and have any created datasets or custom settings be available anytime, you need an API key from Binubuo (or RapidAPI). A full
explanantion of how to enable this API, can be found here: https://binubuo.com/ords/r/binubuo_ui/binubuo/getting-started. Now you are ready to use the API with a real key,
and you can specify that key when you load the class:

```python
>>> from binubuo import binubuo
>>> b = binubuo('<Binubuo key>')
>>> print('Company name: ' + b.generate('business', 'company_name'))
Company name: Lucy Associates
```

You can also play around and test all the generators at: https://rapidapi.com/codemonth/api/binubuo/

## Installing Binubuo client and supported versions

Binubuo is available and installable from PyPI:

    $ python -m pip install binubuo

Binubuo officially supports Python 2.7 & 3.6+.

## Features and Examples

All examples shown here, uses a temporary key. Remeber if you have an API key, to set it when you are intializing the class ```b = binubuo('<Binubuo key>')```. When you use a real
API key instead of a temporary one, you can request larger amount of rows at every dataset request and your datasets are saved across sessions.b = binubuo('<Binubuo key>')

### List all available generators at the prompt

**Binubuo** can list all the currently available generators, by simply calling the list_generators method.

```python
>>> from binubuo import binubuo
>>> b = binubuo()
>>> b.list_generators()
Category:            Function:
===================  =============================
Computer             file_extension
Computer             file_name
Computer             path
Computer             semver
Computer             mimetype
Computer             server_name
Computer             user_agent
Computer             error
Computer             md5
Computer             password
Computer             tld
Computer             domain_name
Computer             email
Computer             ipv4
Computer             ipv6
.........
>>>
```

### Getting multiple generator values in one call

**Binubuo** defaults to only give you one result when you call a generator, but there are times when we need more than one result. For that you can simply
specify the number of results you want, and then a list of results instead of a single value is returned to you.

```python
>>> from binubuo import binubuo
>>> b = binubuo()
>>> print(b.generate('person', 'full_name'))
Addison Watson
>>> b.grows(5) # Set the values count to 5
>>> mylist = b.generate('person', 'full_name')
>>> print(*mylist, sep = "\\n")
Molly King
Charles Phillips
Logan Jackson
David Patterson
Bentley Garcia
```

### "Repeatable" random values

**Binubuo** has a feature called repeatable random. What this feature does, is that it allows you to generate the same random data again, without
persisting the data anywhere in between. This feature is extremely usefull for doing same tests over and over again, with the same test data. Simply "tag"
your data, and you can always go back and get it again.

```python
>>> from binubuo import binubuo
>>> b = binubuo()
>>> b.grows(3)
>>> b.tag('For test A31') # Tag the data
>>> mylist = b.generate('person', 'full_name')
>>> print(*mylist, sep = "\\n")
Caleb Barnes
Daniel Reed
Faith Adams
>>> b.tag() # Reset to empty tag to get new rows.
>>> mylist = b.generate('person', 'full_name')
>>> print(*mylist, sep = "\\n")
Grayson James
Landon Garcia
Makayla Hughes
>>> b.tag('For test A31') # Set the tag back, to generate same rows
>>> mylist = b.generate('person', 'full_name')
>>> print(*mylist, sep = "\\n")
Caleb Barnes
Daniel Reed
Faith Adams
```

### Different locales supported

**Binubuo** supports generating data according to specific locales. For a list of generators and supported locales, see the generator documentation located
at https://binubuo.com/ords/r/binubuo_ui/binubuo/documentation-generators. More and more locales are being added every month. The following example shows how to 
set the locale and swithc it back to default again, as well as showing that both two letter ISO codes and full names are supported.

```python
>>> from binubuo import binubuo
>>> b = binubuo()
>>> print(b.generate('person', 'full_name'))
Khloe Bennett
>>> b.locale('DK') # Set the locale to Denmark
>>> print(b.generate('person', 'full_name'))
Freja Jeppesen
>>> print(b.generate('location', 'city'))
Tønder
>>> print(b.generate('finance', 'bank_account_id'))
DK4883897675725594
>>> b.locale('China') # Set the locale to China
>>> print(b.generate('person', 'full_name'))
Cheng Fù
>>> print(b.generate('location', 'city'))
扬州市
>>> b.locale() # Reset back to default (US)
>>> print(b.generate('person', 'full_name'))
Blake Peterson
>>> print(b.generate('location', 'city'))
Fontana
```

### Calling datasets

**Binubuo** has the ability to get data from not only generators, but also datasets, which support much larger volumes of data, and allows for more advanced ways
of describing and creating your data. Out of the box, Binubuo supplies a couple of standard datasets to get you started in getting larger volumes of data, but you can
also build your very own datasets. For a list of available datasets, you can check the website: https://binubuo.com/ords/r/binubuo_ui/binubuo/documentation-standard-datasets
or you can list them using the list_datasets method.

```python
>>> from binubuo import binubuo
>>> b = binubuo()
>>> b.list_datasets()
Type:      Category:            Dataset:
=========  ===================  =============================
Standard   Demographics         country_people_list
Standard   Finance              credit_card_transactions
Standard   Computer             user_list
Standard   Person               people_list
Standard   Consumer             supermarket_invoice
Standard   Shipping             container_list
Standard   Telecom              cdr_records
Custom                          ot_l_endpoint
Custom                          ot_full
>>> b.dataset('supermarket_invoice', 'standard', 'consumer')
[['Wunder Nuggets, Minty Lentil', 1, 13.77, 0.09], ['Squirt, Citrus Soda', 1, 1.72, 0], ['Hot Bratwurst, Hot', 1, 10.76, 0.12], ['No Sugar Added Mandarin Oranges In Water', 2, 4.55, 0], ['Premium Thai-Style Red Curry Seasoned Mahi Mahi Fillets, Thai-Style', 1, 14.84, 0.15], ['Angus Beef Ground Beef', 1, 8.35, 0.12], ['Frollicks, Crunchy Chickpeas', 4, 7.6, 0], ['Weis, Classic Dressing, Ranch', 4, 15.02, 0], ['Italian Sandwich Thins, Italian', 1, 12.15, 0], ['Sparkling Fruit Tonic', 1, 8.82, 0]]
>>> b.drows(25)
>>> b.dataset('supermarket_invoice', 'standard', 'consumer')
[['Culinary Cuts Seasoned Pork For Fajitas', 1, 15.67, 0], ['Antipasto Platter With Frescatrano Olives, Parmesan Cheese, Uncured Genoa Salami & Uncured Sopressata Salami, Antipasto Platter', 1, 4.47, 0], ['Italian Style Recipe Tomato Paste', 1, 1.53, 0], ['Nova Smoked Sockeye Salmon', 3, 13.84, 0.07], ['Lemon Lime', 1, 4.05, 0], ['Cut Sweet Potatoes In Light Syrup', 3, 8.41, 0.08], ['Extra Cherry Mixed Fruit In A Natural Cherry Flavored Light Syrup', 3, 1.64, 0], ['Sun-Maid Zante Currants 8 Oz Bag', 1, 6.14, 0], ['Better Way, Bread, Whole Grain White', 1, 8.28, 0.09], ['Cranberry Apple Cocktail From Concentrate, Cranberry Apple', 1, 3.61, 0], ['Chili Signature Italian Style Sauce, Chili', 1, 4.45, 0.06], ['Plush With Milk Chocolate Hearts', 5, 6.93, 0.03], ['Italian Peeled Tomatoes In Puree With Basil Leaf', 1, 10.56, 0], ['Creammmy Peanut Butter', 1, 11.82, 0], ['The Good-For-You Ice Cream', 1, 1.71, 0], ['Graham', 1, 7.98, 0], ['Fried Onion Ring Potato Crisps, Fried Onion', 1, 5.52, 0], ['Hidden Veggie, Small Penne Rigate Sweet Corn, Carrot & Squash Pasta Blend', 1, 14.99, 0], ['Lasagna, Brown Rice Pasta', 1, 13.73, 0], ['Diced Pancetta Antipasto', 1, 7.85, 0], ['Weis, Toaster Pastries, Apple Cinnamon', 3, 4.5, 0], ['Plm Mu Straw Blkbry Blue', 1, 11.76, 0], ['Moon Rocks Milk Chocolate Truffle Bar With Popping Candy, Milk Chocolate', 1, 3.85, 0], ['Honey Sriracha Marinade Mix, Honey Sriracha', 1, 5.16, 0], ['Creamed Fillet Of Herring', 2, 5.47, 0]]
```

### Creating CSV files from dataset output

**Binubuo** supports generating output from datasets directly to csv file, for easy data load or manipulation. Simply call the dataset_to_file method.

```python
>>> from binubuo import binubuo
>>> b = binubuo()
>>> b.csv('yes')
>>> b.dataset_to_file(dataset_name = 'supermarket_invoice', dataset_type = 'standard', dataset_category = 'consumer')
```

This will create a file called "supermarket_invoice.csv" in your current directory, with all the data.

```powershell
PS D:\\temp> ls super*.csv


    Directory: D:\\temp


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2/16/2022   4:10 PM            652 supermarket_invoice.csv


PS D:\\temp> cat .\supermarket_invoice.csv
ITEM_NAME,QUANTITY,PRICE,DISCOUNT_RATE
Pepper Marinated Cold Smoked Atlantic Salmon With Creamy Horseradish Sauce, Pepper, Creamy Horseradish Sauce,1,1.75,0
Crumbled Greek Style Feta Cheese, Crumbled Greek Style,1,9.12,0
Tabatchnick, Vegetarian Chili,1,6.98,0
Whipped Horseradish Sour Cream,1,14.7,0
Rustic Potato Sliders,3,1.57,0
Signature Select, Sparkling Soda, Lemonade,1,5.02,0
Cranberry Cinnamon Swirl Demi Loaf,1,10.96,.05
Sweet Sriracha Rubbed Salmon Skewers, Sweet Sriracha Rubbed,5,15.35,0
Bourbon Pepper Flavored Beef Sirloin & Veggie Kabob, Bourbon Pepper,1,12.81,0
Meijer, Crab Deluxe Imitation Crabmeat, Flack Style, Flack Style,1,6.44,0
PS D:\\temp>
```

## Data Features

**Binubuo** supports many data domains and data generators. The below list is just a few examples. Look here for the full list: https://binubuo.com/ords/r/binubuo_ui/binubuo/documentation-generators

* Basic
    * Natural
    * Integer
    * Float
* Business
    * Industry
    * Company Name
* Computer
    * Email
    * Url
    * File Name
    * ipv6
    * Domain Name
* Consumer
    * Food Item
    * Nonfood Item
* Finance
    * Credit Card Number
    * Account Transaction
    * Bank Account ID
    * Transaction Status
* Games
    * Coin Toss
    * Dice Roll
* Investment
    * Fund Name
    * ISIN
    * Swift ID
    * Risk Rating
* Location
    * City
    * Zipcode
    * Address
    * Street Name
* Logistics
    * BIC
    * Container Number
    * Shipping Company
* Medical
    * ICD10
* Person
    * Full name
    * Age
    * Job Title
    * Personal ID
* Phone
    * Phone Number
    * MEID
    * IMSI
    * IMEI
    * Operator Code
* Science
    * Chemical Element
    * Scale
    * Tree
    * Planet
* Text
    * Word
    * Adjective
    * Sentence
* Time
    * Date
    * Day
    * Epoch
    * Timestamp
* Transport
    * License Plate
    * ICAO
    * IMO
"""

packages = ['binubuo']

requires = [
    'requests>=2.0.0; python_version >= "3"'
]

setup(
    name='binubuo',
    version='0.0.7',
    description='Client package for Binubuo synthetic data generator',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://binubuo.com',
    author='Morten',
    author_email='morten@binubuo.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Utilities',
    ],
    keywords='synthetic, testdata, mocking',
    packages=packages,
    package_dir={'binubuo': 'binubuo'},
    install_requires=requires,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
    project_urls={  # Optional
        'Documentation': 'https://binubuo.com/ords/r/binubuo_ui/binubuo/resources',
        'Bug Reports': 'https://github.com/morten-egan/binubuo-python-client/issues/new'
    },
)