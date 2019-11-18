# Socket project
#### By Yuval Saraf

### Develop
* Install python3
* Run in terminal
    ```sh
        py setup.py develop
    ```

### Build
    * Run in terminal
        ```sh
            pip install pyinstaller
        ```
    * Build client
        ```sh
            pyinstaller client/run.py --name client --onefile
        ```
    * Build server
        ```sh
            pyinstaller server/run.py --name server --onefile
        ```
