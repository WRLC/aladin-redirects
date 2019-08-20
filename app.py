from flask import Flask, redirect, request, render_template, url_for
from urlparse import urlparse
import sys

# for dev/debugging: `export FLASK_ENV=development` before `flask run`
# http://127.0.0.1:5000/Z-WEB/Aladin?inst=AU&url=http://whatismyip.com
# http://127.0.0.1:5000/Z-WEB/Aladin?req=db&key=ALADINPROXY&url=https://erescu.wrlc.org/x/docs/37MATURANI_CUAEDU/ILL42260415.pdf
# http://127.0.0.1:5000/Z-WEB/Aladin?url=http://whatismyip.com

# proxy server URLs
proxies = {
    'AU' : 'https://proxyau.wrlc.org/login?url={}',
    'CU' : 'https://proxycu.wrlc.org/login?url={}',
    'DC' : 'https://proxydc.wrlc.org/login?url={}',
    'GA' : 'https://proxyga.wrlc.org/login?url={}',
    'GM' : 'http://mutex.gmu.edu/login?url={}',
    'GT' : 'http://proxy.library.georgetown.edu/login?url={}',
    'GW' : 'https://proxygw.wrlc.org/login?url={}',
    'HU' : 'https://proxyhu.wrlc.org/login?url={}',
    'MU' : 'https://proxymu.wrlc.org/login?url={}',
    'WR' : 'https://proxywr.wrlc.org/login?url={}',
}

ereses = {
    'erescu.wrlc.org' : 'CU',
    'eresgw.wrlc.org' : 'GW',
    'ereshu.wrlc.org' : 'HU',
}


app = Flask(__name__)

@app.route('/Z-WEB')
def doc():
    vinfo = sys.version_info
    app.logger.debug('Using python version '+str(vinfo[0])+'.'+str(vinfo[1]))
    return('legacy ALADIN redirect service')

@app.route('/Z_WEB/select-inst')
def aladin_select_inst():
    return render_template('inst.html')

@app.route('/Z-WEB/Aladin')
def aladin_redirect():
    # see if an url was specified
    url = request.args.get('url', False)

    # see if an institution was specified
    if request.args.get('inst') and request.args.get('inst').upper() in proxies.keys():
        inst = request.args.get('inst').upper()
    else:
        if url:
            urlparts = urlparse( url )
            if urlparts.hostname in ereses.keys():
                inst = ereses[urlparts.hostname]
            else:
                inst = False
        else:
            inst = False

    if inst:
        proxy = proxies[inst]
    else:
        return redirect('/Z-WEB/select-inst?' + request.query_string)

    if url:
        redurl = proxy.format(url)
    else:
        redurl = proxy.format('/menu')
    app.logger.debug('redirect URL: '+redurl)
    return(redirect( redurl ))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

