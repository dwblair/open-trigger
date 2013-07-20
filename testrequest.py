## latlong2uscensus.py
## Given US lat/long return US Census (2010) Block FIPS
## Michael Ash and Don Blair, May 2013, mash@econs.umass.edu
## With help from Ryan Acton, David Arbour, and Klara Zwickl

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


## Read comma-delimited input file with label,latitude,longitude
## Get census block fips for the lat/long from FCC
## http://www.broadbandmap.gov/developer/api/census-api-by-coordinates
## Output label, latitude, longitude, fips

# reference for requests library: http://www.python-requests.org/en/latest/user/quickstart/

# Usage:
# python latlong2uscensus.py [inputFilename] [trialNumber]
# Example:
# python latlong2uscensus.py sampleInput.txt 3

import json, requests, pprint, sys

timeout=1

url = 'https://api.xively.com/v2/feeds/103261'
data=requests.get(url=url, auth=('dwblair', 'cosmcat999'))
#requests.get(url=url, params=params, timeout=timeout)
binary = data.content
output_json = json.loads(binary)
print output_json

