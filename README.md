# log-tracker
###### Track log files the way you want.

## Requirements

Make sure that you have installed python version 3, and python development packages(referred as **python3-devel** in most distributions).
Then do,

```bash
pip3 install -r requiremnts.txt
```

## Running Log Tracker

First delete all the example data(example.yaml file and entry in Tasks and exampe functions in tasks).
Then follow [the Log Tracker wiki](https://github.com/lpsandaruwan/log-tracker/wiki) to create a new task.
Then,

```
python3 ltrk.py
```

### Run in a docker image

First create a `Dockerfile` with requierements,
```
FROM python:3.5
RUN pip3 install -r requirements.txt
CMD ["python", "ltrk.py"]
```

Then build,
```
docker build -t ltrk .
```

To run,
```
docker run ltrk
```

If custom functions has web services(Flask or something),
```
docker run -p 5000:5000 ltrk
```

## License
Copyright (c) 2017: Lahiru Pathirage lpsandaruwan@gmail.com

Log Tracker is a free application: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Log Tracker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. See COPYING for a copy of the GNU General Public License. If not, see http://www.gnu.org/licenses/.
