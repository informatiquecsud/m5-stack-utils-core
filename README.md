# m5-stack-utils-core

Utilities for working with the M5Stack Core in Micropython.

## Terminal

In the `src/terminal` directory, you find a module `terminal.py` usefull for
logging data to the m5stack Core 320x240 screen. It is far from beeing
performant but it does the job. 

The terminal displays 15 lines of text. Contrary to the `lcd.print(message)`
method, the `Terminal.print(message)` method behaves like a real terminal : once
all the lines have been filled, all the lines of text are shifted, the first
line disapears and the last printed data line is displayed on the bottom line.

### Usage

#### Option 1 : copy into UIFlow

The first way to use the Terminal class is to simply copy it in your program into UIFlow.

1.  Copy the content of the `terminal.py` file in UIFlow
2.  Create an instance of the `Terminal` class

    ```python
    ...
    t = Terminal()
    t.print('temperature log')    
    ```

#### Option 2 : importing from external modules

There is also the possibility to import the `Terminal` class from a separated
module. 

1.  Copy the file `terminal.py` onto the M5Stack with UIFlow using the file
    manager (add file tool). Create a file `terminal.py` in the `apps` folder of
    the M5Stack and copy the contents of the `terminal.py` file and save (Ctrl + S) in the browser.

2.  Use an `import` statetement in your program

    ```python
    from terminal import Terminal

    t = Terminal()

    ...

    ```

### Example : logging the data read from the ENV unit

You can find an example using the Terminal class to log data read from the ENV unit in the `src/terminal/env_sensor_log.py` file.
