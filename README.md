# Menu_generator
This project is a console ui generator without any dependencies, only Python is required.

**HOW TO USE**

First you need to create an object of Menu_generator class
```
menu = Menu_generator()
```
You can pass many arguments to the constructor to customize the menu to your liking

**EXAMPLE OF MAIN MENU CREATION**
```
choice = menu.main_menu(**{
    "main": ["Test1", "Test2", "Test3"],
    "side": ["test_side1", "test_side2", "test_side3", "test_side4", "test_side5"]
})
```

![image](https://user-images.githubusercontent.com/65130519/124384741-fcf3a180-dcd2-11eb-8429-9148b7e802f4.png)

**The side menu is dynamically generated based on how much entries you pass to it.**

**EXAMPLE OF SUB MENU CREATION**
```
choice = menu.sub_menu(**{
    "title": ["Test Title"],
    "main": ["test1", "test2", "test3"]
})
```
![image](https://user-images.githubusercontent.com/65130519/124384752-10067180-dcd3-11eb-9237-25b63ad9dad1.png)

Both functions display a choice input for user at the end,
the recommended return value is int but you can use all the other datatypes too.
