


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'LptsPuntFlowtrapProtoIdEnum' : _MetaInfoEnum('LptsPuntFlowtrapProtoIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg',
        {
            'default':'DEFAULT',
            'arp':'ARP',
            'icmp':'ICMP',
            'dhcp':'DHCP',
            'pppoe':'PPPOE',
            'ppp':'PPP',
            'igmp':'IGMP',
            'ipv4':'IPV4',
            'l2tp':'L2TP',
            'unclassified':'UNCLASSIFIED',
        }, 'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg']),
}