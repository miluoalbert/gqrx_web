# GQRX_WEB_CONTROL
GQRX_WEB_CONTROL is a web dashboard for GQRX. The frequency and squelch of GQRX can be remotely controlled via this website.

## Requirements
- Gqrx >= v2.3
- python 3

## Use
install flask and all requirement.
```sh
export FLASK_APP=flaskr
flask run --host=0.0.0.0 --port=5080
```
Dashboard will start at http://localhost:5080

## Reference
- [Controlling gqrx from a remote host](https://gqrx.dk/doc/remote-control)

--------------------------------------------------------------------------------
GQRX_WEB_CONTROL用于在局域网内建立一个远程控制GQRX的界面。通过这个界面可以远程控制GQRX的频率、静噪阈值
