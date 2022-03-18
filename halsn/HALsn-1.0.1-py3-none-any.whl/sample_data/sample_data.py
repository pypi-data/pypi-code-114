#! /usr/bin/env python3

'''
MIT License

Copyright (c) 2020 Vikram Seshadri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

data = [
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1035D\r', '$KN200FF\r', '$KN30390\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 1.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1035A\r', '$KN200FF\r', '$KN30394\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 2.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN10359\r', '$KN20100\r', '$KN30398\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 3.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1035B\r', '$KN20101\r', '$KN3039A\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 4.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN10363\r', '$KN200FD\r', '$KN303A1\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 5.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN10370\r', '$KN200FF\r', '$KN303A8\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 6.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1037A\r', '$KN200FF\r', '$KN303A2\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 7.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1037B\r', '$KN20101\r', '$KN30382\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 8.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN10379\r', '$KN200FD\r', '$KN30356\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 9.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1037A\r', '$KN20101\r', '$KN30336\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 10.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1037E\r', '$KN200FD\r', '$KN30339\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 11.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN10385\r', '$KN200FD\r', '$KN30348\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 12.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN10391\r', '$KN20101\r', '$KN3035F\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 13.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN1039C\r', '$KN20101\r', '$KN30384\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 14.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103AB\r', '$KN200FF\r', '$KN303B6\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 15.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103BA\r', '$KN200FF\r', '$KN303D7\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 16.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103C7\r', '$KN20102\r', '$KN303E6\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 17.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D2\r', '$KN20100\r', '$KN303EB\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 18.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103DC\r', '$KN20102\r', '$KN303F0\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 19.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E2\r', '$KN200FD\r', '$KN303F3\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 20.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E9\r', '$KN20101\r', '$KN303F4\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 21.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103EE\r', '$KN200FF\r', '$KN303F4\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 22.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103F1\r', '$KN20100\r', '$KN303F2\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 23.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103F2\r', '$KN200FD\r', '$KN303EE\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 24.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103F0\r', '$KN20100\r', '$KN303DE\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 25.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103EA\r', '$KN200FF\r', '$KN303BC\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 26.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E3\r', '$KN20101\r', '$KN3039B\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 27.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103DC\r', '$KN200FF\r', '$KN30384\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 28.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D6\r', '$KN200FC\r', '$KN3037A\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 29.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D4\r', '$KN20101\r', '$KN30377\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 30.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D0\r', '$KN200FC\r', '$KN3037C\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 31.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D0\r', '$KN200FD\r', '$KN30386\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 32.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D0\r', '$KN200FC\r', '$KN30393\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 33.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D2\r', '$KN200FD\r', '$KN303A1\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 34.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D5\r', '$KN20102\r', '$KN303AE\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 35.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D7\r', '$KN200FC\r', '$KN303BA\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 36.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103DB\r', '$KN200FD\r', '$KN303C4\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 37.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103DE\r', '$KN200FF\r', '$KN303CF\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 38.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E0\r', '$KN200FF\r', '$KN303D4\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 39.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E2\r', '$KN200FF\r', '$KN303D7\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 40.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E4\r', '$KN20102\r', '$KN303DB\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 41.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E5\r', '$KN200FF\r', '$KN303D9\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 42.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103E5\r', '$KN200FF\r', '$KN303D2\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 43.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103DF\r', '$KN20100\r', '$KN303C2\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 44.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106016200BE00\r', '$KM100\r', '$KM200\r', '$KN103D3\r', '$KN200FD\r', '$KN303A5\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 45.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN103C1\r', '$KN20100\r', '$KN3037E\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 46.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN103AE\r', '$KN200FF\r', '$KN30358\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 47.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN10398\r', '$KN200FD\r', '$KN30346\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 48.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN10388\r', '$KN20105\r', '$KN30342\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 49.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN10380\r', '$KN20100\r', '$KN30344\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 50.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN1037B\r', '$KN200FC\r', '$KN30348\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 51.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN10379\r', '$KN200FD\r', '$KN3034C\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 52.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN10379\r', '$KN200FD\r', '$KN3034E\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 53.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN10379\r', '$KN20100\r', '$KN30353\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 54.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC21106020000000A\r', '$KM100\r', '$KM200\r', '$KN1037A\r', '$KN20102\r', '$KN3035A\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 55.0],
['$WX01301A0200001\r', '$DS1\r', '$LT1\r', '$KC000000000000000\r', '$KM100\r', '$KM200\r', '$KN10378\r', '$KN200FD\r', '$KN30363\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 56.0],
['$WX01301A0200001\r', '$DS1\r', '$LT0\r', '$KC000000000000000\r', '$KM100\r', '$KM200\r', '$KN10377\r', '$KN200FF\r', '$KN30369\r', '$KN403E8\r', '$KN503E8\r', '$KR10\r', '$KR20\r', '$SW01\r', '$SW10\r', '$SW20\r', '$SW31\r', '$SW40\r', '$SW51\r', 10.15, 57.0]
]
