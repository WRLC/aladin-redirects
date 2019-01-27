# WRLC Legacy Aladin Redirect Service
This application takes ALADIN database URLs and redirects to the appropriate EZproxy URL.

## Examples
EReserves (cls-prod.wrlc.org aka erescu , eresgw , ereshu)
```
http://www.aladin.wrlc.org/Z-WEB/Aladin?req=db&key=ALADINPROXY&url=https://erescu.wrlc.org/x/docs/37MATURANI_CUAEDU/ILL42260415.pdf
```
should become this:
```
https://proxycu.wrlc.org/login?url=https://erescu.wrlc.org/x/docs/37MATURANI_CUAEDU/ILL42260415.pdf
```

```
https://patron.wrlc.org/Z-WEB/Aladin?req=db&key=PROXYAUTH&url=https://www.libraries.wrlc.org/
```
becomes
```
TBD: need some WAYF menu
```

## configuration
All hard-coded for now.
```
docker pull wrlc/aladin-redirects
docker run -d -p 5000:5000 wrlc/aladin-redirects
```
### With docker compose:
create a docker-compose.yml file that looks like this:
```
version: "3"
services:
  aladin-redirects:
    image: wrlc/aladin-redirects
    ports:
      - 5000:5000
    restart: always
```
Run your service:
```
docker-compose up -d
```
