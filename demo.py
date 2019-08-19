#! /usr/bin/env python3

import os
import asyncio
import aiohttp
import vcr
import logging

log = logging.getLogger('vcr')
log.setLevel(logging.INFO)


@vcr.use_cassette("test_cassette.yaml")
async def vcr_test():
    results = []
    async with aiohttp.ClientSession() as session:
        async with session.get('https://postman-echo.com/get') as resp:
            results.append(resp.headers)
        async with session.get('https://postman-echo.com/get') as resp:
            results.append(resp.headers)
    return results


async def main():
    # remove cassette file for first run to ensure it's fresh real requests
    try:
        os.remove('test_cassette.yaml')
    except FileNotFoundError:
        pass

    real_results = await vcr_test()
    recorded_results = await vcr_test()

    print("\nreal results:")
    print(real_results[0])
    print(real_results[1])

    print("\nrecorded results:")
    print(recorded_results[0])
    print(recorded_results[1])

    assert real_results == recorded_results

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
