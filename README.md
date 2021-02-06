# This Person Does Not Exist But Has Age And Gender

Python package for getting the person with requested gender and age from 
[This Person Does Not Exist](https://thispersondoesnotexist.com/) website.

It's getting right person, by downloading image of a randomly generated person from 
[This Person Does Not Exist](https://thispersondoesnotexist.com/) and then checking gender and age of that person,
with use of OpenCV library.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install this_person_does_not_exist_but_has_age_and_gender
```

## Usage

```python
from this_person_does_not_exist_but_has_age_and_gender import get_person

get_person("male", 30) # returns filename of downloaded picture of a person
```

It can be also used from command line
```bash 
python this_person_does_not_exist_but_has_age_and_gender.py male 30
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)