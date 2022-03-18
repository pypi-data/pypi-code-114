# bulkrequests
# Copyright (C) 2022  Dario Graña, Pau Tallada
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program;  If not, see <https://www.gnu.org/licenses/>.


'''
constants used by bulkrequests
'''

# JSON constants
JSON_CURRENTQOS = 'currentQos'
JSON_CHILDREN = 'children'
JSON_FILENAME = 'fileName'
JSON_FILETYPE = 'fileType'
JSON_FILELOCALITY = 'fileLocality'
JSON_DIR_FILETYPE = 'DIR'
JSON_REGULAR_FILETYPE = 'REGULAR'
JSON_SIZE = 'size'

# QOS constants
DISK_QOS = 'disk'
TAPE_QOS = 'tape'
DISK_TAPE_QOS = 'disk+tape'

# locality constants
ONLINE_LOC = 'ONLINE'
NEARLINE_LOC = 'NEARLINE'
ONLINE_AND_NEARLINE_LOC = 'ONLINE_AND_NEARLINE'
