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
and
```
https://patron.wrlc.org/Z-WEB/Aladin?req=db&key=PROXYAUTH&url=https://www.libraries.wrlc.org/
```
becomes
```
https://idp.cua.edu/idp/profile/SAML2/POST/SSO?execution=e1s1
```

## Installation
Clone this repository.
```
git clone git@github.com:WRLC/aladin-redirects.git
```
Set up python virtual environment
```
python3 -m venv aladin-redirects
source venv/bin/activate
pip install -r requirements.txt
deactivate
```
Configure your application service. At WRLC we now run this app in a Green Unicorn Python WSGI HTTP server). The daemon is started and stoped via systemd.
```
mkdir log
sudo cp aladin-redirects.service.example /etc/systemd/system/aladin-redirects.service
sudo vim /etc/systemd/system/aladin-redirects.service  ## edit config to match app path
sudo systemctl start aladin-redirects.service
sudo systemctl enable aladin-redirects.service
```

## Deprecated Docker configuration
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
