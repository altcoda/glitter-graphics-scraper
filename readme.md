<center>

![scraper in terminal](https://i.ibb.co/YQPNNCC/scraper-preview-1.jpg)

![scraper results](https://i.ibb.co/pvDZPRC/scraper-preview-2.png)
</center>

# Glitter-Graphics Scraper

- Download as many pictures as you like from glitter-graphics by selecting a category.
- They are downloaded in full size with their original file extension.
- You can also change the starting page as easily.
- I made this scraper for fun and to learn. If there are any issues you can report them.

# Important

- Selecting a category only works with keypad arrows. This is due to the package used for it.
- It also won't work in in-built pycharm terminal.
- Don't lower the time.sleep() counter as it can overload the site server by creating requests too fast and you could potentially get banned.

# Requirements
- You need to have Python 3.7 or higher.

# Setup & Use

- Clone the repo.
- Install all necessary dependencies with this command

```
   pip install beautifulsoup4 requests inquirer
```

- To run the scraper open the terminal in the directory and enter 'python scraper.py'
- To change starting page change line 12 of scraper.py
- Running the scraper more than once with different starting pages can result in images being overwritten.
