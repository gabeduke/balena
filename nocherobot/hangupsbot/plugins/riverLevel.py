#!/usr/bin/env python3

import io
import logging
import os
import requests
import plugins
import urllib.request


logger = logging.getLogger(__name__)


def _initialise(bot):
    plugins.register_user_command(['level'])

def level(bot, event, *args):
    # Gather Data
    url = "https://level-6y4rumxsfq-uc.a.run.app/api/v1/slack"

    req = requests.post(url)
    data = req.json()

    # Parse Latest Reading
    latest = data['text']
    image_uri = data['attachments'][0]['image_url']

    logger.info("getting {}".format(image_uri))

    filename = os.path.basename(image_uri)
    request = urllib.request.Request(image_uri)
    image_response = urllib.request.urlopen(request)

    image_id = yield from bot._client.upload_image(image_response, filename=filename)

    yield from bot.coro_send_message(event.conv.id_, "River Level is: " + latest, None, None)
    yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)
