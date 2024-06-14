import json
import os
from pathlib import Path


class App:
    def __init__(self):
        print('started')
        self.working = 0
        self.id = 0

    def start(self):
        self.working = 1
        temp_id = 0
        limit = 100
        while True:
            if temp_id > limit:
                break
            try:
                path = str(Path(__file__).parent.absolute())
                if not os.path.exists(f'{path}\\songs\\song{temp_id}\\data.json'):
                    continue
                with open(f'{path}\\songs\\song{temp_id}\\data.json', 'r') as f:
                    data = json.loads(f.read())
                    print(f'Song №{temp_id}')
                    for key, val in data.items():
                        print(f'{key} - {val}')
                    print('---------------------------------')
                    self.id = temp_id + 1
            except Exception:
                continue
            finally:
                temp_id += 1
        while (self.working):
            self.loop()

    def loop(self):
        command = input('Input command (type /help):')
        if command.startswith('/help'):
            print('List of commands:\n/exit - end program\n/add - add song to directory\n/list - show all '
                  'songs\n/remove - delete song by id\n/get - find songs with criteria')
        if command.startswith('/exit'):
            self.working = 0
        if command.startswith('/add'):
            try:
                path = str(Path(__file__).parent.absolute())
                os.makedirs(f'{path}\\songs\\song{self.id}', mode=0o777, exist_ok=True)
                data = input('Input in format {Name} {Author} {Year} {Cover} {Rate}: ').split()
                ans = {"Name": data[0], "Author": data[1], "Year": data[2], "Cover": data[3], "Rate": data[4]}
                with open(f'{path}\\songs\\song{self.id}\\data.json', 'w') as f:
                    json.dump(ans, f)
                    self.id += 1
            except Exception:
                print('invalid input')
        if command.startswith('/list'):
            temp_id = 0
            limit = 100
            while True:
                if temp_id > limit:
                    break
                try:
                    path = str(Path(__file__).parent.absolute())
                    if not os.path.exists(f'{path}\\songs\\song{temp_id}\\data.json'):
                        continue
                    with open(f'{path}\\songs\\song{temp_id}\\data.json', 'r') as f:
                        data = json.loads(f.read())
                        print(f'Song №{temp_id}')
                        for key, val in data.items():
                            print(f'{key} - {val}')
                        print('---------------------------------')
                        self.id = temp_id + 1
                except Exception:
                    continue
                finally:
                    temp_id += 1
        if command.startswith('/remove'):
            try:
                kom = command.split()
                path = str(Path(__file__).parent.absolute())
                if os.path.exists(f'{path}\\songs\\song{kom[1]}\\data.json'):
                    os.remove(f'{path}\\songs\\song{kom[1]}\\data.json')
                    os.rmdir(f'{path}\\songs\\song{kom[1]}')
                    print('deleted')
                else:
                    print('there is no such a id')
            except Exception:
                print('invalid input, try /remove {id}')
        if command.startswith('/get'):
            try:
                kom = command.split()
                if kom[1].lower() in ['name', 'author', 'year', 'cover', 'rate']:
                    temp_id = 0
                    limit = 100
                    while True:
                        if temp_id > limit:
                            break
                        try:
                            path = str(Path(__file__).parent.absolute())
                            if not os.path.exists(f'{path}\\songs\\song{temp_id}\\data.json'):
                                continue
                            with open(f'{path}\\songs\\song{temp_id}\\data.json', 'r') as f:
                                data = json.loads(f.read())
                                ans = f'Song №{temp_id}\n'
                                flag = 0
                                for key, val in data.items():
                                    ans += f'{key} - {val}\n'
                                    if kom[1].capitalize() == key and kom[2].lower() in val.lower():
                                        # print(f'test - {kom[2].lower()} - {val.lower()}')
                                        flag = 1
                                ans += '---------------------------------'
                                if flag == 1:
                                    print(ans)
                        except Exception:
                            # print('invalid error, try /get (name|author|year|cover|rate) {search}')
                            continue
                        finally:
                            temp_id += 1
            except Exception:
                print('invalid input, try /get (name|author|year|cover|rate) {search}')