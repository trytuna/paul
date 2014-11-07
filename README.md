Paul is a simple commandline tool to push notifications to your iOS device that has Prowl.app installed

[Prowl](http://www.prowlapp.com) 
[Prowl.app for iOS](https://itunes.apple.com/de/app/prowl-easy-push-notifications/id320876271?l=en&mt=8)

# Install
```
python3 setup.py install
```

# Usage

```
paul -h
```

```
echo "apikeyhere" > ~/.paul
paul -e "event name" -d "description"
```

```
paul -k "apikeyhere" -e "event name" -d "description"
```
