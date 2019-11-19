# Socket project
#### By Yuval Saraf

### Develop
* Install python3
* Run in terminal
    ```sh
        python3 setup.py develop
    ```

### Build
    * Run in terminal
        ```sh
            python3 -m pip install pyinstaller
        ```
    * Build client
        ```sh
            pyinstaller client/main.py --name client --onefile
        ```
    * Build server
        ```sh
            pyinstaller server/main.py --name server --onefile
        ```
