import logging

import pynma

import autosubliminal

log = logging.getLogger(__name__)


def test_notify():
    log.debug("Trying to send a notification")
    message = "Test notification by Auto-Subliminal"
    return _send_notify(message)


def send_notify(video, subtitle, language, provider):
    log.debug("Trying to send a notification")
    message = "Subtitle: %s \n Language: %s \n Provider: %s" % (subtitle, language, provider)
    return _send_notify(message)


def _send_notify(message):
    nma_instance = pynma.PyNMA(str(autosubliminal.NMAAPI))
    resp = nma_instance.push('Auto-Subliminal', 'Subtitle download', message)
    try:
        if not resp[str(autosubliminal.NMAAPI)][u'code'] == u'200':
            log.error("Failed to send a notification")
            return False
        else:
            log.info("Notification sent")
            return True
    except:
        log.error("Failed to send a notification")
