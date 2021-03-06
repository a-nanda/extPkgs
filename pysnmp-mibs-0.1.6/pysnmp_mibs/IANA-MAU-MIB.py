#
# PySNMP MIB module IANA-MAU-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IANA-MAU-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:16:01 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( OctetString, Integer, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
( ModuleCompliance, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
( ModuleIdentity, IpAddress, Counter64, NotificationType, Unsigned32, Integer32, Gauge32, MibIdentifier, Counter32, TimeTicks, mib_2, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, ) = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "MibIdentifier", "Counter32", "TimeTicks", "mib-2", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaMauMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 154)).setRevisions(("2011-08-12 00:00", "2010-02-23 00:00", "2007-04-21 00:00",))
if mibBuilder.loadTexts: ianaMauMIB.setLastUpdated('201108120000Z')
if mibBuilder.loadTexts: ianaMauMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaMauMIB.setContactInfo('        Internet Assigned Numbers Authority\n\n                     Postal: ICANN\n                             4676 Admiralty Way, Suite 330\n                             Marina del Rey, CA 90292\n\n                        Tel: +1-310-823-9358\n                      EMail: iana&iana.org')
if mibBuilder.loadTexts: ianaMauMIB.setDescription("This MIB module defines dot3MauType OBJECT-IDENTITIES and\n         IANAifMauListBits, IANAifMauMediaAvailable,\n         IANAifMauAutoNegCapBits, and IANAifJackType\n\n         TEXTUAL-CONVENTIONs, specifying enumerated values of the\n         ifMauTypeListBits, ifMauMediaAvailable / rpMauMediaAvailable,\n         ifMauAutoNegCapabilityBits / ifMauAutoNegCapAdvertisedBits /\n         ifMauAutoNegCapReceivedBits and ifJackType / rpJackType objects\n         respectively, defined in the MAU-MIB.\n\n         It is intended that each new MAU type, Media Availability\n         state, Auto Negotiation capability and/or Jack type defined by\n         the IEEE 802.3 working group and approved for publication in a\n         revision of IEEE Std 802.3 will be added to this MIB module,\n         provided that it is suitable for being managed by the base\n         objects in the MAU-MIB.  An Expert Review, as defined in\n         RFC 2434 [RFC2434], is REQUIRED for such additions.\n\n         The following reference is used throughout this MIB module:\n\n         [IEEE802.3] refers to:\n            IEEE Std 802.3, 2005 Edition: 'IEEE Standard for\n            Information technology - Telecommunications and information\n            exchange between systems - Local and metropolitan area\n            networks - Specific requirements -\n            Part 3: Carrier sense multiple access with collision\n            detection (CSMA/CD) access method and physical layer\n            specifications'.\n\n         This reference should be updated as appropriate when new\n         MAU types, Media Availability states, Auto Negotiation\n         capabilities, and/or Jack types are added to this MIB module.\n\n         Copyright (C) The IETF Trust (2007).\n         The initial version of this MIB module was published in\n         RFC 4836; for full legal notices see the RFC itself.\n         Supplementary information may be available at:\n         http://www.ietf.org/copyrights/ianamib.html")
class IANAifMauTypeListBits(Bits, TextualConvention):
    namedValues = NamedValues(("bOther", 0), ("bAUI", 1), ("b10base5", 2), ("bFoirl", 3), ("b10base2", 4), ("b10baseT", 5), ("b10baseFP", 6), ("b10baseFB", 7), ("b10baseFL", 8), ("b10broad36", 9), ("b10baseTHD", 10), ("b10baseTFD", 11), ("b10baseFLHD", 12), ("b10baseFLFD", 13), ("b100baseT4", 14), ("b100baseTXHD", 15), ("b100baseTXFD", 16), ("b100baseFXHD", 17), ("b100baseFXFD", 18), ("b100baseT2HD", 19), ("b100baseT2FD", 20), ("b1000baseXHD", 21), ("b1000baseXFD", 22), ("b1000baseLXHD", 23), ("b1000baseLXFD", 24), ("b1000baseSXHD", 25), ("b1000baseSXFD", 26), ("b1000baseCXHD", 27), ("b1000baseCXFD", 28), ("b1000baseTHD", 29), ("b1000baseTFD", 30), ("b10GbaseX", 31), ("b10GbaseLX4", 32), ("b10GbaseR", 33), ("b10GbaseER", 34), ("b10GbaseLR", 35), ("b10GbaseSR", 36), ("b10GbaseW", 37), ("b10GbaseEW", 38), ("b10GbaseLW", 39), ("b10GbaseSW", 40), ("b10GbaseCX4", 41), ("b2BaseTL", 42), ("b10PassTS", 43), ("b100BaseBX10D", 44), ("b100BaseBX10U", 45), ("b100BaseLX10", 46), ("b1000BaseBX10D", 47), ("b1000BaseBX10U", 48), ("b1000BaseLX10", 49), ("b1000BasePX10D", 50), ("b1000BasePX10U", 51), ("b1000BasePX20D", 52), ("b1000BasePX20U", 53), ("b10GbaseT", 54), ("b10GbaseLRM", 55), ("b1000baseKX", 56), ("b10GbaseKX4", 57), ("b10GbaseKR", 58), ("b10G1GbasePRXD1", 59), ("b10G1GbasePRXD2", 60), ("b10G1GbasePRXD3", 61), ("b10G1GbasePRXU1", 62), ("b10G1GbasePRXU2", 63), ("b10G1GbasePRXU3", 64), ("b10GbasePRD1", 65), ("b10GbasePRD2", 66), ("b10GbasePRD3", 67), ("b10GbasePRU1", 68), ("b10GbasePRU3", 69), ("b40GbaseKR4", 70), ("b40GbaseCR4", 71), ("b40GbaseSR4", 72), ("b40GbaseFR", 73), ("b40GbaseLR4", 74), ("b100GbaseCR10", 75), ("b100GbaseSR10", 76), ("b100GbaseLR4", 77), ("b100GbaseER4", 78),)

class IANAifMauMediaAvailable(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("available", 3), ("notAvailable", 4), ("remoteFault", 5), ("invalidSignal", 6), ("remoteJabber", 7), ("remoteLinkLoss", 8), ("remoteTest", 9), ("offline", 10), ("autoNegError", 11), ("pmdLinkFault", 12), ("wisFrameLoss", 13), ("wisSignalLoss", 14), ("pcsLinkFault", 15), ("excessiveBER", 16), ("dxsLinkFault", 17), ("pxsLinkFault", 18), ("availableReduced", 19), ("ready", 20),)

class IANAifMauAutoNegCapBits(Bits, TextualConvention):
    namedValues = NamedValues(("bOther", 0), ("b10baseT", 1), ("b10baseTFD", 2), ("b100baseT4", 3), ("b100baseTX", 4), ("b100baseTXFD", 5), ("b100baseT2", 6), ("b100baseT2FD", 7), ("bFdxPause", 8), ("bFdxAPause", 9), ("bFdxSPause", 10), ("bFdxBPause", 11), ("b1000baseX", 12), ("b1000baseXFD", 13), ("b1000baseT", 14), ("b1000baseTFD", 15), ("b10GbaseT", 16), ("b1000baseKX", 17), ("b10GbaseKX4", 18), ("b10GbaseKR", 19), ("b40GbaseKR4", 20), ("b40GbaseCR4", 21), ("b100GbaseCR10", 22),)

class IANAifJackType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,))
    namedValues = NamedValues(("other", 1), ("rj45", 2), ("rj45S", 3), ("db9", 4), ("bnc", 5), ("fAUI", 6), ("mAUI", 7), ("fiberSC", 8), ("fiberMIC", 9), ("fiberST", 10), ("telco", 11), ("mtrj", 12), ("hssdc", 13), ("fiberLC", 14), ("cx4", 15),)

dot3MauType = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4))
dot3MauTypeAUI = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 1))
if mibBuilder.loadTexts: dot3MauTypeAUI.setDescription('no internal MAU, view from AUI')
dot3MauType10Base5 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 2))
if mibBuilder.loadTexts: dot3MauType10Base5.setDescription('thick coax MAU')
dot3MauTypeFoirl = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 3))
if mibBuilder.loadTexts: dot3MauTypeFoirl.setDescription('FOIRL MAU')
dot3MauType10Base2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 4))
if mibBuilder.loadTexts: dot3MauType10Base2.setDescription('thin coax MAU')
dot3MauType10BaseT = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 5))
if mibBuilder.loadTexts: dot3MauType10BaseT.setDescription('UTP MAU.\n                   Note that it is strongly recommended that\n                   agents return either dot3MauType10BaseTHD or\n                   dot3MauType10BaseTFD if the duplex mode is\n                   known.  However, management applications should\n                   be prepared to receive this MAU type value from\n                   older agent implementations.')
dot3MauType10BaseFP = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 6))
if mibBuilder.loadTexts: dot3MauType10BaseFP.setDescription('passive fiber MAU')
dot3MauType10BaseFB = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 7))
if mibBuilder.loadTexts: dot3MauType10BaseFB.setDescription('sync fiber MAU')
dot3MauType10BaseFL = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 8))
if mibBuilder.loadTexts: dot3MauType10BaseFL.setDescription('async fiber MAU.\n                   Note that it is strongly recommended that\n                   agents return either dot3MauType10BaseFLHD or\n                   dot3MauType10BaseFLFD if the duplex mode is\n                   known.  However, management applications should\n                   be prepared to receive this MAU type value from\n                   older agent implementations.')
dot3MauType10Broad36 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 9))
if mibBuilder.loadTexts: dot3MauType10Broad36.setDescription('broadband DTE MAU.\n                   Note that 10BROAD36 MAUs can be attached to\n                   interfaces but not to repeaters.')
dot3MauType10BaseTHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 10))
if mibBuilder.loadTexts: dot3MauType10BaseTHD.setDescription('UTP MAU, half duplex mode')
dot3MauType10BaseTFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 11))
if mibBuilder.loadTexts: dot3MauType10BaseTFD.setDescription('UTP MAU, full duplex mode')
dot3MauType10BaseFLHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 12))
if mibBuilder.loadTexts: dot3MauType10BaseFLHD.setDescription('async fiber MAU, half duplex mode')
dot3MauType10BaseFLFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 13))
if mibBuilder.loadTexts: dot3MauType10BaseFLFD.setDescription('async fiber MAU, full duplex mode')
dot3MauType100BaseT4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 14))
if mibBuilder.loadTexts: dot3MauType100BaseT4.setDescription('4 pair category 3 UTP')
dot3MauType100BaseTXHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 15))
if mibBuilder.loadTexts: dot3MauType100BaseTXHD.setDescription('2 pair category 5 UTP, half duplex mode')
dot3MauType100BaseTXFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 16))
if mibBuilder.loadTexts: dot3MauType100BaseTXFD.setDescription('2 pair category 5 UTP, full duplex mode')
dot3MauType100BaseFXHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 17))
if mibBuilder.loadTexts: dot3MauType100BaseFXHD.setDescription('X fiber over PMT, half duplex mode')
dot3MauType100BaseFXFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 18))
if mibBuilder.loadTexts: dot3MauType100BaseFXFD.setDescription('X fiber over PMT, full duplex mode')
dot3MauType100BaseT2HD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 19))
if mibBuilder.loadTexts: dot3MauType100BaseT2HD.setDescription('2 pair category 3 UTP, half duplex mode')
dot3MauType100BaseT2FD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 20))
if mibBuilder.loadTexts: dot3MauType100BaseT2FD.setDescription('2 pair category 3 UTP, full duplex mode')
dot3MauType1000BaseXHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 21))
if mibBuilder.loadTexts: dot3MauType1000BaseXHD.setDescription('PCS/PMA, unknown PMD, half duplex mode')
dot3MauType1000BaseXFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 22))
if mibBuilder.loadTexts: dot3MauType1000BaseXFD.setDescription('PCS/PMA, unknown PMD, full duplex mode')
dot3MauType1000BaseLXHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 23))
if mibBuilder.loadTexts: dot3MauType1000BaseLXHD.setDescription('Fiber over long-wavelength laser, half duplex\n                   mode')
dot3MauType1000BaseLXFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 24))
if mibBuilder.loadTexts: dot3MauType1000BaseLXFD.setDescription('Fiber over long-wavelength laser, full duplex\n                   mode')
dot3MauType1000BaseSXHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 25))
if mibBuilder.loadTexts: dot3MauType1000BaseSXHD.setDescription('Fiber over short-wavelength laser, half\n                   duplex mode')
dot3MauType1000BaseSXFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 26))
if mibBuilder.loadTexts: dot3MauType1000BaseSXFD.setDescription('Fiber over short-wavelength laser, full\n                   duplex mode')
dot3MauType1000BaseCXHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 27))
if mibBuilder.loadTexts: dot3MauType1000BaseCXHD.setDescription('Copper over 150-Ohm balanced cable, half\n                   duplex mode')
dot3MauType1000BaseCXFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 28))
if mibBuilder.loadTexts: dot3MauType1000BaseCXFD.setDescription('Copper over 150-Ohm balanced cable, full\n\n                   duplex mode')
dot3MauType1000BaseTHD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 29))
if mibBuilder.loadTexts: dot3MauType1000BaseTHD.setDescription('Four-pair Category 5 UTP, half duplex mode')
dot3MauType1000BaseTFD = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 30))
if mibBuilder.loadTexts: dot3MauType1000BaseTFD.setDescription('Four-pair Category 5 UTP, full duplex mode')
dot3MauType10GigBaseX = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 31))
if mibBuilder.loadTexts: dot3MauType10GigBaseX.setDescription('X PCS/PMA, unknown PMD.')
dot3MauType10GigBaseLX4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 32))
if mibBuilder.loadTexts: dot3MauType10GigBaseLX4.setDescription('X fiber over WWDM optics')
dot3MauType10GigBaseR = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 33))
if mibBuilder.loadTexts: dot3MauType10GigBaseR.setDescription('R PCS/PMA, unknown PMD.')
dot3MauType10GigBaseER = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 34))
if mibBuilder.loadTexts: dot3MauType10GigBaseER.setDescription('R fiber over 1550 nm optics')
dot3MauType10GigBaseLR = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 35))
if mibBuilder.loadTexts: dot3MauType10GigBaseLR.setDescription('R fiber over 1310 nm optics')
dot3MauType10GigBaseSR = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 36))
if mibBuilder.loadTexts: dot3MauType10GigBaseSR.setDescription('R fiber over 850 nm optics')
dot3MauType10GigBaseW = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 37))
if mibBuilder.loadTexts: dot3MauType10GigBaseW.setDescription('W PCS/PMA, unknown PMD.')
dot3MauType10GigBaseEW = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 38))
if mibBuilder.loadTexts: dot3MauType10GigBaseEW.setDescription('W fiber over 1550 nm optics')
dot3MauType10GigBaseLW = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 39))
if mibBuilder.loadTexts: dot3MauType10GigBaseLW.setDescription('W fiber over 1310 nm optics')
dot3MauType10GigBaseSW = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 40))
if mibBuilder.loadTexts: dot3MauType10GigBaseSW.setDescription('W fiber over 850 nm optics')
dot3MauType10GigBaseCX4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 41))
if mibBuilder.loadTexts: dot3MauType10GigBaseCX4.setDescription('X copper over 8 pair 100-Ohm balanced cable')
dot3MauType2BaseTL = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 42))
if mibBuilder.loadTexts: dot3MauType2BaseTL.setDescription('Voice grade UTP copper, up to 2700m, optional PAF')
dot3MauType10PassTS = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 43))
if mibBuilder.loadTexts: dot3MauType10PassTS.setDescription('Voice grade UTP copper, up to 750m, optional PAF')
dot3MauType100BaseBX10D = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 44))
if mibBuilder.loadTexts: dot3MauType100BaseBX10D.setDescription('One single-mode fiber OLT, long wavelength, 10km')
dot3MauType100BaseBX10U = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 45))
if mibBuilder.loadTexts: dot3MauType100BaseBX10U.setDescription('One single-mode fiber ONU, long wavelength, 10km')
dot3MauType100BaseLX10 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 46))
if mibBuilder.loadTexts: dot3MauType100BaseLX10.setDescription('Two single-mode fibers, long wavelength, 10km')
dot3MauType1000BaseBX10D = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 47))
if mibBuilder.loadTexts: dot3MauType1000BaseBX10D.setDescription('One single-mode fiber OLT, long wavelength, 10km')
dot3MauType1000BaseBX10U = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 48))
if mibBuilder.loadTexts: dot3MauType1000BaseBX10U.setDescription('One single-mode fiber ONU, long wavelength, 10km')
dot3MauType1000BaseLX10 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 49))
if mibBuilder.loadTexts: dot3MauType1000BaseLX10.setDescription('Two sigle-mode fiber, long wavelength, 10km')
dot3MauType1000BasePX10D = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 50))
if mibBuilder.loadTexts: dot3MauType1000BasePX10D.setDescription('One single-mode fiber EPON OLT, 10km')
dot3MauType1000BasePX10U = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 51))
if mibBuilder.loadTexts: dot3MauType1000BasePX10U.setDescription('One single-mode fiber EPON ONU, 10km')
dot3MauType1000BasePX20D = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 52))
if mibBuilder.loadTexts: dot3MauType1000BasePX20D.setDescription('One single-mode fiber EPON OLT, 20km')
dot3MauType1000BasePX20U = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 53))
if mibBuilder.loadTexts: dot3MauType1000BasePX20U.setDescription('One single-mode fiber EPON ONU, 20km')
dot3MauType10GbaseT = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 54))
if mibBuilder.loadTexts: dot3MauType10GbaseT.setDescription('Four-pair Category 6A or better, full duplex mode only')
dot3MauType10GbaseLRM = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 55))
if mibBuilder.loadTexts: dot3MauType10GbaseLRM.setDescription('R multimode fiber over 1310 nm optics')
dot3MauType1000baseKX = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 56))
if mibBuilder.loadTexts: dot3MauType1000baseKX.setDescription('X backplane, full duplex mode only')
dot3MauType10GbaseKX4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 57))
if mibBuilder.loadTexts: dot3MauType10GbaseKX4.setDescription('4 lane X backplane, full duplex mode only')
dot3MauType10GbaseKR = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 58))
if mibBuilder.loadTexts: dot3MauType10GbaseKR.setDescription('R backplane, full duplex mode only')
dot3MauType10G1GbasePRXD1 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 59))
if mibBuilder.loadTexts: dot3MauType10G1GbasePRXD1.setDescription('One single-mode fiber asymmetric-rate EPON OLT, supporting low\n                    power budget (PRX10)')
dot3MauType10G1GbasePRXD2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 60))
if mibBuilder.loadTexts: dot3MauType10G1GbasePRXD2.setDescription('One single-mode fiber asymmetric-rate EPON OLT, supporting\n                   medium power budget (PRX20)')
dot3MauType10G1GbasePRXD3 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 61))
if mibBuilder.loadTexts: dot3MauType10G1GbasePRXD3.setDescription('One single-mode fiber asymmetric-rate EPON OLT, supporting high\n                   power budget (PRX30)')
dot3MauType10G1GbasePRXU1 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 62))
if mibBuilder.loadTexts: dot3MauType10G1GbasePRXU1.setDescription('One single-mode fiber asymmetric-rate EPON ONU, supporting low\n                   power budget (PRX10)')
dot3MauType10G1GbasePRXU2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 63))
if mibBuilder.loadTexts: dot3MauType10G1GbasePRXU2.setDescription('One single-mode fiber asymmetric-rate EPON ONU, supporting\n                   medium power budget (PRX20)')
dot3MauType10G1GbasePRXU3 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 64))
if mibBuilder.loadTexts: dot3MauType10G1GbasePRXU3.setDescription('One single-mode fiber asymmetric-rate EPON ONU, supporting high\n                   power budget (PRX30)')
dot3MauType10GbasePRD1 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 65))
if mibBuilder.loadTexts: dot3MauType10GbasePRD1.setDescription('One single-mode fiber symmetric-rate EPON OLT, supporting low\n                   power budget (PR10)')
dot3MauType10GbasePRD2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 66))
if mibBuilder.loadTexts: dot3MauType10GbasePRD2.setDescription('One single-mode fiber symmetric-rate EPON OLT, supporting\n                   medium power budget (PR20)')
dot3MauType10GbasePRD3 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 67))
if mibBuilder.loadTexts: dot3MauType10GbasePRD3.setDescription('One single-mode fiber symmetric-rate EPON OLT, supporting high\n                   power budget (PR30)')
dot3MauType10GbasePRU1 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 68))
if mibBuilder.loadTexts: dot3MauType10GbasePRU1.setDescription('One single-mode fiber symmetric-rate EPON ONU, supporting\n                   low and medium power budget (PR10 and PR20)')
dot3MauType10GbasePRU3 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 69))
if mibBuilder.loadTexts: dot3MauType10GbasePRU3.setDescription('One single-mode fiber symmetric-rate EPON ONU, supporting high\n                   power budget (PR30)')
dot3MauType40GbaseKR4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 70))
if mibBuilder.loadTexts: dot3MauType40GbaseKR4.setDescription('40GBASE-R PCS/PMA over an electrical \n                      backplane')
dot3MauType40GbaseCR4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 71))
if mibBuilder.loadTexts: dot3MauType40GbaseCR4.setDescription('40GBASE-R PCS/PMA over 4 lane shielded \n                      copper balanced cable')
dot3MauType40GbaseSR4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 72))
if mibBuilder.loadTexts: dot3MauType40GbaseSR4.setDescription('40GBASE-R PCS/PMA over 4 lane multimode \n                      fiber')
dot3MauType40GbaseFR = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 73))
if mibBuilder.loadTexts: dot3MauType40GbaseFR.setDescription('40GBASE-R PCS/PMA over single mode \n                      fiber')
dot3MauType40GbaseLR4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 74))
if mibBuilder.loadTexts: dot3MauType40GbaseLR4.setDescription('40GBASE-R PCS/PMA over 4 WDM lane \n                      single mode fiber')
dot3MauType100GbaseCR10 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 75))
if mibBuilder.loadTexts: dot3MauType100GbaseCR10.setDescription('100GBASE-R PCS/PMA over 10 lane \n                      shielded copper balanced cable')
dot3MauType100GbaseSR10 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 76))
if mibBuilder.loadTexts: dot3MauType100GbaseSR10.setDescription('100GBASE-R PCS/PMA over 10 lane \n                      multimode fiber')
dot3MauType100GbaseLR4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 77))
if mibBuilder.loadTexts: dot3MauType100GbaseLR4.setDescription('100GBASE-R PCS/PMA over 4 WDM lane \n                      single mode fiber, long reach')
dot3MauType100GbaseER4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 26, 4, 78))
if mibBuilder.loadTexts: dot3MauType100GbaseER4.setDescription('100GBASE-R PCS/PMA over 4 WDM lane \n                      single mode fiber PMD, extended reach')
mibBuilder.exportSymbols("IANA-MAU-MIB", dot3MauType10BaseFP=dot3MauType10BaseFP, dot3MauType1000BaseSXHD=dot3MauType1000BaseSXHD, dot3MauType10G1GbasePRXD1=dot3MauType10G1GbasePRXD1, IANAifMauMediaAvailable=IANAifMauMediaAvailable, dot3MauType10BaseFLFD=dot3MauType10BaseFLFD, dot3MauType10GigBaseX=dot3MauType10GigBaseX, dot3MauType10GigBaseW=dot3MauType10GigBaseW, dot3MauType10GigBaseCX4=dot3MauType10GigBaseCX4, dot3MauType1000BaseLX10=dot3MauType1000BaseLX10, dot3MauType1000BaseXHD=dot3MauType1000BaseXHD, dot3MauType1000BasePX20D=dot3MauType1000BasePX20D, dot3MauType10GigBaseLR=dot3MauType10GigBaseLR, dot3MauType10GigBaseLX4=dot3MauType10GigBaseLX4, dot3MauType2BaseTL=dot3MauType2BaseTL, dot3MauType10GbaseKR=dot3MauType10GbaseKR, dot3MauType10GigBaseSW=dot3MauType10GigBaseSW, dot3MauType1000BaseBX10U=dot3MauType1000BaseBX10U, PYSNMP_MODULE_ID=ianaMauMIB, dot3MauType100GbaseER4=dot3MauType100GbaseER4, dot3MauType40GbaseCR4=dot3MauType40GbaseCR4, dot3MauType10GbasePRU1=dot3MauType10GbasePRU1, dot3MauType100BaseBX10D=dot3MauType100BaseBX10D, dot3MauType1000BasePX10U=dot3MauType1000BasePX10U, dot3MauType10BaseFB=dot3MauType10BaseFB, dot3MauType10GigBaseLW=dot3MauType10GigBaseLW, dot3MauType=dot3MauType, dot3MauType100GbaseSR10=dot3MauType100GbaseSR10, dot3MauType100GbaseLR4=dot3MauType100GbaseLR4, IANAifMauAutoNegCapBits=IANAifMauAutoNegCapBits, dot3MauType1000BaseXFD=dot3MauType1000BaseXFD, dot3MauType1000BasePX10D=dot3MauType1000BasePX10D, ianaMauMIB=ianaMauMIB, dot3MauType10Broad36=dot3MauType10Broad36, dot3MauType40GbaseFR=dot3MauType40GbaseFR, dot3MauType10GbasePRD3=dot3MauType10GbasePRD3, dot3MauType100BaseTXHD=dot3MauType100BaseTXHD, dot3MauType10BaseFLHD=dot3MauType10BaseFLHD, dot3MauType10BaseFL=dot3MauType10BaseFL, dot3MauType100BaseFXHD=dot3MauType100BaseFXHD, dot3MauType1000BaseBX10D=dot3MauType1000BaseBX10D, dot3MauType10GigBaseER=dot3MauType10GigBaseER, dot3MauType1000BasePX20U=dot3MauType1000BasePX20U, dot3MauType10Base2=dot3MauType10Base2, dot3MauType10GbaseT=dot3MauType10GbaseT, dot3MauType10G1GbasePRXU1=dot3MauType10G1GbasePRXU1, dot3MauType10GbasePRD2=dot3MauType10GbasePRD2, IANAifMauTypeListBits=IANAifMauTypeListBits, dot3MauType1000BaseTFD=dot3MauType1000BaseTFD, dot3MauType10PassTS=dot3MauType10PassTS, dot3MauType40GbaseKR4=dot3MauType40GbaseKR4, IANAifJackType=IANAifJackType, dot3MauType10GbaseLRM=dot3MauType10GbaseLRM, dot3MauType10Base5=dot3MauType10Base5, dot3MauType100BaseLX10=dot3MauType100BaseLX10, dot3MauType10GigBaseR=dot3MauType10GigBaseR, dot3MauType100BaseT2FD=dot3MauType100BaseT2FD, dot3MauType100GbaseCR10=dot3MauType100GbaseCR10, dot3MauType1000BaseCXHD=dot3MauType1000BaseCXHD, dot3MauType10GigBaseSR=dot3MauType10GigBaseSR, dot3MauType10G1GbasePRXU2=dot3MauType10G1GbasePRXU2, dot3MauType10BaseT=dot3MauType10BaseT, dot3MauType10GigBaseEW=dot3MauType10GigBaseEW, dot3MauType10BaseTFD=dot3MauType10BaseTFD, dot3MauType100BaseT4=dot3MauType100BaseT4, dot3MauType100BaseFXFD=dot3MauType100BaseFXFD, dot3MauType1000BaseCXFD=dot3MauType1000BaseCXFD, dot3MauType10GbasePRD1=dot3MauType10GbasePRD1, dot3MauType40GbaseLR4=dot3MauType40GbaseLR4, dot3MauType1000BaseLXHD=dot3MauType1000BaseLXHD, dot3MauType40GbaseSR4=dot3MauType40GbaseSR4, dot3MauType1000BaseLXFD=dot3MauType1000BaseLXFD, dot3MauTypeFoirl=dot3MauTypeFoirl, dot3MauType10BaseTHD=dot3MauType10BaseTHD, dot3MauType100BaseT2HD=dot3MauType100BaseT2HD, dot3MauType1000BaseSXFD=dot3MauType1000BaseSXFD, dot3MauType10G1GbasePRXD3=dot3MauType10G1GbasePRXD3, dot3MauType100BaseBX10U=dot3MauType100BaseBX10U, dot3MauType10GbaseKX4=dot3MauType10GbaseKX4, dot3MauType10G1GbasePRXD2=dot3MauType10G1GbasePRXD2, dot3MauType1000baseKX=dot3MauType1000baseKX, dot3MauType10G1GbasePRXU3=dot3MauType10G1GbasePRXU3, dot3MauTypeAUI=dot3MauTypeAUI, dot3MauType10GbasePRU3=dot3MauType10GbasePRU3, dot3MauType100BaseTXFD=dot3MauType100BaseTXFD, dot3MauType1000BaseTHD=dot3MauType1000BaseTHD)
