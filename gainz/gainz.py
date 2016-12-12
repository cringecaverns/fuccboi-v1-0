# -*- coding: utf-8 -*-
from disco.bot import Bot, Plugin
import requests

display_options = {
            # Pricing Dividends
            u"a": u"Ask",
            u"y": u"Dividend Yield",
            u"b": u"Bid",
            u"d": u"Dividend per Share",
            u"b2": u"Ask (Realtime)",
            u"r1": u"Dividend Pay Date",
            u"b3": u"Bid (Realtime)",
            u"q": u"Ex-Dividend Date",
            u"p": u"Previous Close",
            u"o": u"Open",

            # Date
            u"c1": u"Change",
            u"d1": u"Last Trade Date",
            u"c": u"Change & Percent Change",
            u"d2": u"Trade Date",
            u"c6": u"Change (Realtime)",
            u"t1": u"Last Trade Time",
            u"k2": u"Change Percent (Realtime",
            u"p2": u"Change in Percent",

            # Averages
            u"c8": u"After Hours Change (Realtime)",
            u"m5": u"Change From 200 Day Moving Average",
            u"c3": u"Commission",
            u"m6": u"Percent Change From 200 Day Moving Average",
            u"g": u"Day’s Low",
            u"m7": u"Change From 50 Day Moving Average",
            u"h": u"Day’s High",
            u"m8": u"Percent Change From 50 Day Moving Average",
            u"k1": u"Last Trade (Realtime) With Time",
            u"m3": u"50 Day Moving Average",
            u"l": u"Last Trade (With Time)",
            u"m4": u"200 Day Moving Average",
            u"l1": u"Last Trade (Price Only",
            u"t8": u"1 yr Target Price",

            # Misc
            u"w1": u"Day’s Value Change",
            u"g1": u"Holdings Gain Percent",
            u"w4": u"Day’s Value Change (Realtime)",
            u"g3": u"Annualized Gain",
            u"p1": u"Price Paid",
            u"g4": u"Holdings Gain",
            u"m": u"Day’s Range",
            u"g5": u"Holdings Gain Percent (Realtime)",
            u"m2": u"Day’s Range (Realtime)",
            u"g6": u"Holdings Gain (Realtime)",
            
            #52 Week Pricing Symbol Info
            u"k": u"52 Week High",
            u"i": u"More Info",
            u"j": u"52 week Low",
            u"j1": u"Market Capitalization",
            u"j5": u"Change From 52 Week Low",
            u"j3": u"Market Cap (Realtime)",
            u"k4": u"Change From 52 week High",
            u"f6": u"Float Shares",
            u"j6": u"Percent Change From 52 week Low",
            u"n": u"Name",
            u"k5": u"Percent Change From 52 week High",
            u"n4": u"Notes",
            u"w": u"52 week Range",
            u"s": u"Symbol",
            u"s1": u"Shares Owned",
            u"x": u"Stock Exchange",
            u"j2": u"Shares Outstanding",

            # Volume
            u"v": u"Volume",
            u"a5": u"Ask Size",
            u"b6": u"Bid Size    Misc",
            u"k3": u"Last Trade Size",
            u"t7": u"Ticker Trend",
            u"a2": u"Average Daily Volume",
            u"t6": u"Trade Links",
            u"i5": u"Order Book (Realtime)",

            # Ratios
            u"l2": u"High Limit",
            u"e": u"Earnings per Share",
            u"l3": u"Low Limit",
            u"e7": u"EPS Estimate Current Year",
            u"v1": u"Holdings Value",
            u"e8": u"EPS Estimate Next Year",
            u"v7": u"Holdings Value (Realtime)",
            u"e9": u"EPS Estimate Next Quarter",
            u"s6": u"Revenue",
            u"b4": u"Book Value",
            u"j4": u"EBITDA",
            u"p5": u"Price / Sales",
            u"p6": u"Price / Book",
            u"r": u"P/E Ratio",
            u"r2": u"P/E Ratio (Realtime",
            u"r5": u"PEG Ratio",
            u"r6": u"Price / EPS Estimate Current Year",
            u"r7": u"Price / EPS Estimate Next Year",
            u"s7": u"Short Ratio"
        }

def get_display_str(requested_display):
    display_types = []
    skip = None
    
    for i, c in enumerate(requested_display):
        if i is skip:
            skip = None
            continue
        if c in display_options:
            print(len(requested_display),  i)
            if len(requested_display) > i + 1:
                if requested_display[i + 1].isdigit():
                    display_types.append(c + str(requested_display[i + 1]))
                    skip = i + 1
                    print('SKIP:', skip, c + str(requested_display[i + 1]))
            else:
                display_types.append(c)
        else:
            return 's b2 b3 a2 k j g h f6 w r5 s6'.split()
    return display_types

class Gainz(Plugin):
    @Plugin.command('GAINZ', '<shitpost:str...>')
    def on_gainz_command(self, event, shitpost):
        query = shitpost.split()
        if 'display:' in query[-1]:
            requested_display = list(query.pop().split(':')[-1])
            display_types = get_display_str(requested_display)
        else:
            display_types = 's b2 b3 a2 k j g h f6 w r5 s6'.split()

        result = requests.get("http://download.finance.yahoo.com/d/quotes.csv?s={}&f={}".format('+'.join(query), ''.join(display_types)))
        if not result:
            event.msg.reply('Usage: GAINZ JNUG DMB.ASS')
        else:
            o = ''
            r = result.content.split('\n')
            for gainz in r:
                if gainz:
                    deez_gainz = gainz.split(',')
                    o += "```\n"
                    for d, g in zip([display_options[k] for k in display_types], deez_gainz):
                        o += '{}:\t{}\n'.format(d.encode('utf8'), g.encode('utf8'))
                    o += "\n```"
                    o += 'http://chart.finance.yahoo.com/z?s={}&t=6m&q=l&l=on&z=s&p=m50,m200\n'.format(query.pop(0))            
            event.msg.reply(o)